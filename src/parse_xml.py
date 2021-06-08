import xml.etree.ElementTree as ET
from collections import OrderedDict

def parse_xml(file):
    
    # Set an XML-tree and its root.
    tree = ET.parse(file_name)
    root = tree.getroot()

    # Create an empty list to store the dictionary entries in and create a counter for each entry.
    vocab = []
    counter = 0

    # Start iterating over all the entries.
    for LexicalEntry in root.iter('LexicalEntry'):
        for feat in LexicalEntry.findall('feat'):
            if feat.get('val') == '단어':
                # If an entry is a word create a list to store its data in.
                vocab.append([])
                vocab[counter] = [{'hangul': LexicalEntry.find('Lemma').find('feat').get('val')}]
                vocab[counter][0]['id'] = LexicalEntry.get('val')
                vocab[counter][0]['vocabularyLevel'] = LexicalEntry.findall('feat')[-3].get('val')
                vocab[counter][0]['subjectCategory'] = LexicalEntry.findall('feat')[-2].get('val')
                vocab[counter][0]['wordForm'] = [vocab[counter][0]['hangul']]
                vocab[counter].append([])

                for i in range(1, len(LexicalEntry.findall('WordForm'))):
                    wf = LexicalEntry.findall('WordForm')[i].findall('feat')[1].get('val')
                    vocab[counter][0]['wordForm'].append(wf)

                senses = 0
                for Sense in LexicalEntry.findall('Sense'):
                    vocab[counter][1].append({})
                    vocab[counter][1][senses]['sense_id'] = Sense.get('val')
                    vocab[counter][1][senses]['translation'] = Sense.find('Equivalent').findall('feat')[1].get('val')
                    vocab[counter][1][senses]['definition'] = Sense.find('Equivalent').findall('feat')[2].get('val')
                    vocab[counter][1][senses]['krDefintion'] = Sense.find('feat').get('val')
                    vocab[counter][1][senses]['example'] = []

                    for SenseExample in LexicalEntry.find('Sense').findall('SenseExample'):
                        if SenseExample.find('feat').get('val') == "구" or SenseExample.find('feat').get('val') == "대화":                              
                            if SenseExample.find('feat').get('val') == "대화":
                                for word in vocab[counter][0]['wordForm']:
                                    example_1 = f'    <li>나: {SenseExample.findall("feat")[1].get("val")}</li>'
                                    example_1 = example_1.replace(word, f'<span style="color: #9400D3">{word}</span>')
                                    vocab[counter][1][senses]['example'].append(example_1)
                                    example_2 = f'    <li>너: {SenseExample.findall("feat")[2].get("val")}</li>'
                                    example_2 = example_2.replace(word, f'<span style="color: #9400D3">{word}</span>')
                                    vocab[counter][1][senses]['example'].append(example_2)
                                    break
                            else:
                                for word in vocab[counter][0]['wordForm']:
                                    if word in SenseExample.findall("feat")[1].get("val"):
                                        example_3 = f'    <li>{SenseExample.findall("feat")[1].get("val")}</li>'
                                        example_3 = example_3.replace(word, f'<span style="color: #9400D3">{word}</span>')
                                        vocab[counter][1][senses]['example'].append(example_3)
                                        
                    examples = '\n'.join(vocab[counter][1][senses]['example'])
                    vocab[counter][1][senses]['example'] = examples
                    senses += 1
                counter += 1

    return vocab
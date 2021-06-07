import xml.etree.ElementTree as ET
from pprint import pprint
from collections import OrderedDict
from pprint import pprint


class Parse:
    
    def parse_vocab(self, file):
        
        tree = ET.parse(file)
        root = tree.getroot()

        vocab = []
        counter = 0

        for LexicalEntry in root.iter('LexicalEntry'):
            for feat in LexicalEntry.findall('feat'):
                if feat.get('val') == '단어':
                    vocab.append([])
                    vocab[counter] = [{'hangul': LexicalEntry.find('Lemma').find('feat').get('val')}]
                    vocab[counter][0]['id'] = LexicalEntry.get('val')
                    vocab[counter][0]['vocabularyLevel'] = LexicalEntry.findall('feat')[-3].get('val')
                    vocab[counter][0]['subjectCategory'] = LexicalEntry.findall('feat')[-2].get('val')
                    vocab[counter].append([])
                    c = 0
                    for Sense in LexicalEntry.findall('Sense'):
                        vocab[counter][1].append({})
                        vocab[counter][1][c]['sense_id'] = Sense.get('val')
                        vocab[counter][1][c]['translation'] = Sense.find('Equivalent').findall('feat')[1].get('val')
                        vocab[counter][1][c]['definition'] = Sense.find('Equivalent').findall('feat')[2].get('val')
                        vocab[counter][1][c]['krDefintion'] = Sense.find('feat').get('val')
                        vocab[counter][1][c]['example'] = ''
                        vocab[counter][1][c]['example'] = []
                        for SenseExample in LexicalEntry.find('Sense').findall('SenseExample'):
                            feat = SenseExample.findall('feat')
                            vocab[counter][1][c]['example'].append(f'    <li>{feat[1].get("val")}</li>\n')
                        examples = ' '.join(vocab[counter][1][c]['example'])
                        vocab[counter][1][c]['example'] = examples
                        c += 1
                    counter += 1
        return vocab







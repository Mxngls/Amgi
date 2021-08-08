import xml.etree.ElementTree as ET
from src.get_wav import download_wav
from collections import OrderedDict
from tqdm import tqdm
from pprint import pprint


def parser(file):

    # Set an XML-tree and its root
    tree = ET.parse(file)
    root = tree.getroot()

    # Set an index for the different senses of a word
    sense_id_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

    # Create an empty list to store the dictionary entries in and create a counter for each entry
    vocab = []
    counter = 0

    # Start iterating over all the entries.
    for LexicalEntry in tqdm(root.iter('LexicalEntry')):
        # Add a list for every entry
        # Check if the entry is an idiomatic phrase or a proverb
        for feat in LexicalEntry:
            if feat.get('val') == '관용구':
                # Create an empty dictionary to store the information
                # and add the necessary fields to it
                for sense_id, sense in enumerate(LexicalEntry.findall('Sense')):
                    vocab.append({})
                    vocab[counter][
                        'link'
                    ] = f"""https://krdict.korean.go.kr/eng/dicSearch/SearchView?wordMatchFlag=N&mainSearchWord=%EB%B9%84%EB%B9%84%EB%8B%A4&currentPage=1&sort=W&searchType=W&proverbType=&exaType=&ParaWordNo={LexicalEntry.get('val')}&nation=eng&nationCode=6&viewType=A&blockCount=10&viewTypes=on"""
                    vocab[counter]['hangul'] = (
                        LexicalEntry.find('Lemma').find('feat').get('val')
                    )
                    vocab[counter]['id'] = LexicalEntry.get('val')
                    vocab[counter]['pronounciation'] = vocab[counter]['hangul']
                    vocab[counter]['homonym_number'] = ''
                    vocab[counter]['sense_id'] = str(sense_id)
                    vocab[counter]['wav_name'] = ''
                    vocab[counter]['translation'] = (
                        sense.find('Equivalent').findall('feat')[1].get('val')
                    )
                    vocab[counter]['definition'] = (
                        sense.find('Equivalent').findall('feat')[2].get('val')
                    )
                    for i in range(0, len(sense.findall('feat'))):
                        if sense.findall('feat')[i].get('att') == 'definition':
                            vocab[counter]['krDefintion'] = sense.findall('feat')[
                                i
                            ].get('val')
                    vocab[counter]['semantic_category'] = vocab[counter - 1][
                        'semantic_category'
                    ]
                    vocab[counter]['subject_category'] = vocab[counter - 1][
                        'subject_category'
                    ]
                    vocab[counter]['vocabulary_level'] = vocab[counter - 1][
                        'vocabulary_level'
                    ]
                    vocab[counter]['lexical_unit'] = LexicalEntry.find('feat').get(
                        'val'
                    )
                    vocab[counter]['examples'] = []

                    # Add the different examples into our list of examples
                    for sense_example in sense.findall('SenseExample'):
                        if (
                            sense_example.find('feat').get('val') == '구'
                            or sense_example.find('feat').get('val') == '문장'
                        ):
                            vocab[counter]['examples'].append(
                                f"<li>{sense_example.findall('feat')[1].get('val')}</li>"
                            )
                        elif sense_example.find('feat').get('val') == '대화':
                            part_1 = (
                                '    <li>나:'
                                f' {sense_example.findall("feat")[1].get("val")}'
                            )
                            part_2 = (
                                '    너:'
                                f' {sense_example.findall("feat")[2].get("val")}</li>'
                            )
                            example = part_1 + '</br>' + part_2
                            vocab[counter]['examples'].append(example)

                    examples = '\n'.join(vocab[counter]['examples'])
                    vocab[counter]['examples'] = examples
                    if not vocab[counter]:
                        vocab.pop(vocab[counter])
                    counter += 1

        # Check if the entry is a word or grammatical expression
        for feat in LexicalEntry:
            if feat.get('val') == '단어' or feat.get('val') == '문법‧표현':
                # Create an empty dictionary to store the information
                # and add the necessary fields to it
                for sense_id, sense in enumerate(LexicalEntry.findall('Sense')):
                    vocab.append({})
                    vocab[counter][
                        'link'
                    ] = f"""https://krdict.korean.go.kr/eng/dicSearch/SearchView?wordMatchFlag=N&mainSearchWord=%EB%B9%84%EB%B9%84%EB%8B%A4&currentPage=1&sort=W&searchType=W&proverbType=&exaType=&ParaWordNo={LexicalEntry.get('val')}&nation=eng&nationCode=6&viewType=A&blockCount=10&viewTypes=on"""
                    vocab.append({})

                    if int(LexicalEntry.find('feat').get('val')) > 0:
                        vocab[counter]['hangul'] = (
                            "<span>"
                            + LexicalEntry.find('Lemma').find('feat').get('val')
                            + f"""<sub style='font-size: 60%; line-height:45%'>{LexicalEntry.findall('feat')[0].get('val')}{sense_id_alphabet[sense_id]}</sub>"""
                            + "</span>"
                        )
                    else:
                        vocab[counter]['hangul'] = (
                            "<span>"
                            + LexicalEntry.find('Lemma').find('feat').get('val')
                            + f"""<sub style='font-size: 60%; line-height: 45%'>{sense_id_alphabet[sense_id]}</sub>"""
                            + "</span>"
                        )

                    vocab[counter]['id'] = LexicalEntry.get('val')
                    vocab[counter]['homonym_number'] = LexicalEntry.find('feat').get(
                        'val'
                    )
                    if LexicalEntry.find('WordForm') is not None:
                        if (
                            LexicalEntry.find('WordForm').findall('feat')[1].get('val')
                            is None
                        ):
                            vocab[counter]['pronounciation'] = (
                                LexicalEntry.find('Lemma').find('feat').get('val')
                            )
                        else:
                            vocab[counter]['pronounciation'] = (
                                LexicalEntry.find('WordForm')
                                .findall('feat')[1]
                                .get('val')
                            )
                        vocab[counter][
                            'wav_name'
                        ] = f"[sound:{vocab[counter]['id']}.wav]"
                        download_wav(
                            LexicalEntry.find('WordForm').findall('feat')[2].get('val'),
                            vocab[counter]['id'],
                        )
                    else:
                        vocab[counter]['pronounciation'] = (
                            LexicalEntry.find('Lemma').find('feat').get('val')
                        )
                        vocab[counter]['wav_name'] = ''
                    # vocab[counter]['pronounciation'] = ''
                    # vocab[counter]['wav_name'] = ''
                    vocab[counter]['sense_id'] = str(sense_id)
                    vocab[counter]['translation'] = (
                        sense.find('Equivalent').findall('feat')[1].get('val')
                    )
                    vocab[counter]['definition'] = (
                        sense.find('Equivalent').findall('feat')[2].get('val')
                    )
                    for i in range(0, len(sense.findall('feat'))):
                        if sense.findall('feat')[i].get('att') == 'definition':
                            vocab[counter]['krDefintion'] = sense.findall('feat')[
                                i
                            ].get('val')
                    vocab[counter]['subject_category'] = ['없음']
                    vocab[counter]['semantic_category'] = ['없음']
                    for i in range(0, len(LexicalEntry.findall('feat'))):
                        if (
                            LexicalEntry.findall('feat')[i].get('att')
                            == 'vocabularyLevel'
                        ):
                            vocab[counter]['vocabulary_level'] = LexicalEntry.findall(
                                'feat'
                            )[i].get('val')
                        elif (
                            LexicalEntry.findall('feat')[i].get('att')
                            == 'semanticCategory'
                        ):
                            vocab[counter]['semantic_category'].pop()
                            vocab[counter]['semantic_category'].append(
                                LexicalEntry.findall('feat')[i].get('val')
                            )
                        elif (
                            LexicalEntry.findall('feat')[i].get('att')
                            == 'subjectCategiory'
                        ):
                            vocab[counter]['subject_category'].pop()
                            vocab[counter]['subject_category'].append(
                                LexicalEntry.findall('feat')[i].get('val')
                            )
                        elif (
                            LexicalEntry.findall('feat')[i].get('att') == 'lexicalUnit'
                        ):
                            vocab[counter]['lexical_unit'] = LexicalEntry.findall(
                                'feat'
                            )[i].get('val')

                    vocab[counter]['wordForm'] = [
                        LexicalEntry.find('Lemma').find('feat').get('val')
                    ]
                    vocab[counter]['examples'] = []

                    for i in range(1, len(LexicalEntry.findall('WordForm'))):
                        wf = (
                            LexicalEntry.findall('WordForm')[i]
                            .findall('feat')[1]
                            .get('val')
                        )
                        vocab[counter]['wordForm'].append(wf)

                    for sense_example in sense.findall('SenseExample'):
                        if sense_example.find('feat').get('val') == "대화":
                            for word in vocab[counter]['wordForm']:
                                part_1 = (
                                    '    <li>나:'
                                    f' {sense_example.findall("feat")[1].get("val")}'
                                )
                                part_1 = part_1.replace(
                                    word,
                                    '<span style="color: #28da6d; text-decoration:'
                                    f' bold">{word}</span>',
                                )
                                part_2 = (
                                    '    너:'
                                    f' {sense_example.findall("feat")[2].get("val")}</li>'
                                )
                                part_2 = part_2.replace(
                                    word,
                                    '<span style="color: #28da6d; text-decoration:'
                                    f' bold">{word}</span>',
                                )
                                example = part_1 + '</br>' + part_2
                                vocab[counter]['examples'].append(example)
                                break
                        else:
                            for word in vocab[counter]['wordForm']:
                                if word in vocab[counter]['wordForm']:
                                    example = f'<li>{sense_example.findall("feat")[1].get("val")}</li>'
                                    example = example.replace(
                                        word,
                                        '<span style="color: #28da6d; text-decoration:'
                                        f' bold">{word}</span>',
                                    )
                                    vocab[counter]['examples'].append(example)
                                    break

                    examples = '\n'.join(vocab[counter]['examples'])
                    vocab[counter]['examples'] = examples
                    counter += 1
                    if sense_id > 2:
                        break

    vocab = [word for word in vocab if word]

    for i, word in enumerate(vocab):
        pprint(vocab[i])
    return vocab

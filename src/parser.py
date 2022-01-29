import xml.etree.ElementTree as ET
from get_wav import download_wav
from tqdm import tqdm


def parser(file):

    # Set an XML-tree and its root
    tree = ET.parse(file)
    root = tree.getroot()

    # Create an empty list to store the dictionary entries in and create a counter for each entry
    vocab = []
    counter = 0

    # Start iterating over all the entries.
    for LexicalEntry in tqdm(root.iter('LexicalEntry')):
        vocab.append({})

        for feat in LexicalEntry:
            if feat.get('val') == '단어':
                # Create an empty dictionary to store the information
                # and add the necessary fields to it

                vocab[counter]['senses'] = []

                vocab[counter][
                    'link'
                ] = f"""https://krdict.korean.go.kr/eng/dicSearch/SearchView?wordMatchFlag=N&mainSearchWord=%EB%B9%84%EB%B9%84%EB%8B%A4&currentPage=1&sort=W&searchType=W&proverbType=&exaType=&ParaWordNo={LexicalEntry.get('val')}&nation=eng&nationCode=6&viewType=A&blockCount=10&viewTypes=on"""

                if int(LexicalEntry.find('feat').get('val')) > 0:
                    vocab[counter]['hangul'] = (
                        "<span>"
                        + LexicalEntry.find('Lemma').find('feat').get('val')
                        + f"""<sub style='font-size: 60%; line-height:45%'>{LexicalEntry.findall('feat')[0].get('val')}</sub>"""
                        + "</span>"
                    )
                else:
                    vocab[counter]['hangul'] = (
                        LexicalEntry.find('Lemma').find('feat').get('val')
                    )

                vocab[counter]['id'] = LexicalEntry.get('val')
                vocab[counter]['homonym_number'] = LexicalEntry.find(
                    'feat').get('val')
                if LexicalEntry.find('WordForm') is not None:
                    if (
                        LexicalEntry.find('WordForm').findall(
                            'feat')[1].get('val')
                        is None
                    ):
                        vocab[counter]['pronounciation'] = (
                            LexicalEntry.find('Lemma').find('feat').get('val')
                        )
                    else:
                        vocab[counter]['pronounciation'] = (
                            LexicalEntry.find('WordForm').findall(
                                'feat')[1].get('val')
                        )
                        vocab[counter][
                            'wav_name'
                        ] = f"[sound:{vocab[counter]['id']}.wav]"
                        pronounciation_link = (
                            LexicalEntry.find('WordForm').findall(
                                'feat')[-1].get('val')
                        )
                        if pronounciation_link[0:5] == "https":
                            download_wav(
                                LexicalEntry.find('WordForm')
                                .findall('feat')[2]
                                .get('val'),
                                vocab[counter]['id'],
                            )
                else:
                    vocab[counter]['pronounciation'] = (
                        LexicalEntry.find('Lemma').find('feat').get('val')
                    )
                    vocab[counter]['wav_name'] = ''
                # vocab[counter]['pronounciation'] = ''
                # vocab[counter]['wav_name'] = ''

                vocab[counter]['subject_category'] = ['없음']
                vocab[counter]['semantic_category'] = ['없음']
                for i in range(0, len(LexicalEntry.findall('feat'))):
                    if LexicalEntry.findall('feat')[i].get('att') == 'vocabularyLevel':
                        vocab[counter]['vocabulary_level'] = LexicalEntry.findall(
                            'feat'
                        )[i].get('val')
                    elif (
                        LexicalEntry.findall('feat')[i].get(
                            'att') == 'semanticCategory'
                    ):
                        vocab[counter]['semantic_category'].pop()
                        vocab[counter]['semantic_category'].append(
                            LexicalEntry.findall('feat')[i].get('val')
                        )
                    elif (
                        LexicalEntry.findall('feat')[i].get(
                            'att') == 'subjectCategiory'
                    ):
                        vocab[counter]['subject_category'].pop()
                        vocab[counter]['subject_category'].append(
                            LexicalEntry.findall('feat')[i].get('val')
                        )
                    elif LexicalEntry.findall('feat')[i].get('att') == 'lexicalUnit':
                        vocab[counter]['lexical_unit'] = LexicalEntry.findall('feat')[
                            i
                        ].get('val')

                vocab[counter]['wordForm'] = [
                    LexicalEntry.find('Lemma').find('feat').get('val')
                ]

                for i in range(1, len(LexicalEntry.findall('WordForm'))):
                    wf = (
                        LexicalEntry.findall('WordForm')[i]
                        .findall('feat')[1]
                        .get('val')
                    )
                    vocab[counter]['wordForm'].append(wf)

                # iterate over all the senses
                for sense_id, sense in enumerate(LexicalEntry.findall('Sense')):

                    vocab[counter]['senses'].append({})
                    vocab[counter]['senses'][sense_id]['examples'] = []
                    vocab[counter]['senses'][sense_id]['sense_id'] = str(
                        sense_id)
                    vocab[counter]['senses'][sense_id]['translation'] = (
                        sense.find('Equivalent').findall('feat')[1].get('val')
                    )
                    vocab[counter]['senses'][sense_id]['definition'] = (
                        sense.find('Equivalent').findall('feat')[2].get('val')
                    )
                    for i in range(0, len(sense.findall('feat'))):
                        if sense.findall('feat')[i].get('att') == 'definition':
                            vocab[counter]['senses'][sense_id][
                                'krDefintion'
                            ] = sense.findall('feat')[i].get('val')

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
                                vocab[counter]['senses'][sense_id]['examples'].append(
                                    example
                                )
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
                                    vocab[counter]['senses'][sense_id][
                                        'examples'
                                    ].append(example)
                                    break

                    examples = '\n'.join(
                        vocab[counter]['senses'][sense_id]['examples'])
                    vocab[counter]['senses'][sense_id]['examples'] = examples

                if sense_id > 5:
                    break

        counter += 1

    vocab = [word for word in vocab if word]

    return vocab

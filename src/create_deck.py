import genanki
from model import *


def create_deck(vocab, file_name, is_grammar):

    anki_deck_title = file_name.replace('.xml', '')
    if is_grammar is True:
        deck_id = 1628542422876
    else:
        deck_id = 2182019230123
    anki_deck = genanki.Deck(deck_id, anki_deck_title)

    for i, word in enumerate(vocab):
        # Format the tags according to the standard
        # of Genanki
        tags = []
        tags.append(word['vocabulary_level'].replace(" ", ""))
        tags.append(word['lexical_unit'].replace(" ", ""))
        for category in word['subject_category']:
            tags.append(category.replace(" ", ""))
        for category in word['semantic_category']:
            tags.append(category.replace(" ", ""))
        word['subject_category'] = (' | ').join(word['subject_category'])
        word['semantic_category'] = (' | ').join(word['semantic_category'])
        if is_grammar == True:
            anki_model = grammar_model
        else:
            anki_model = vocab_model
        senses = []
        for j in range(0, 6):
            senses.append({})
            if j >= len(word['senses']):
                senses[j]['translation'] = ''
                senses[j]['definition'] = ''
                senses[j]['krDefintion'] = ''
                senses[j]['examples'] = ''
            else:
                senses[j]['translation'] = word['senses'][j]['translation']
                senses[j]['definition'] = word['senses'][j]['definition']
                senses[j]['krDefintion'] = word['senses'][j]['krDefintion']
                senses[j]['examples'] = word['senses'][j]['examples']

        anki_note = genanki.Note(
            model=anki_model,
            fields=[
                word['hangul'],
                word['id'],
                word['link'],
                word['homonym_number'],
                word['pronounciation'],
                word['wav_name'],
                senses[0]['translation'],
                senses[0]['definition'],
                senses[0]['krDefintion'],
                senses[0]['examples'],
                senses[1]['translation'],
                senses[1]['definition'],
                senses[1]['krDefintion'],
                senses[1]['examples'],
                senses[2]['translation'],
                senses[2]['definition'],
                senses[2]['krDefintion'],
                senses[2]['examples'],
                senses[3]['translation'],
                senses[3]['definition'],
                senses[3]['krDefintion'],
                senses[3]['examples'],
                senses[4]['translation'],
                senses[4]['definition'],
                senses[4]['krDefintion'],
                senses[4]['examples'],
                senses[5]['translation'],
                senses[5]['definition'],
                senses[5]['krDefintion'],
                senses[5]['examples'],
                word['subject_category']
                + ' | '
                + word['semantic_category']
                + ' | '
                + word['vocabulary_level']
                + ' | '
                + word['lexical_unit'], 
            ],
            tags=tags,
            due=i,
        )
        anki_deck.add_note(anki_note)

    new_deck = genanki.Package(anki_deck)
    new_deck.media_files = [
        '/users/max/Library/Application Support/Anki2/Max/collection.media'
    ]
    new_deck.write_to_file(f'data/apkg_files/{anki_deck_title}.apkg')

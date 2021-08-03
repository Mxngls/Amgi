import genanki
from src.models import *
import os
from pprint import pprint


def create_deck(vocab, file_name, is_grammar):

    deck_filename = "data/apkg_files/" + file_name
    anki_deck_title = file_name.replace('.xml', '')
    if is_grammar is True:
        deck_id = 461152559
    else:
        deck_id = 929174285
    anki_deck = genanki.Deck(deck_id, anki_deck_title)

    # {"name": "hangul"},
    # {"name": "id"},
    # {"name": "link"},
    # {"name": "homonym_number"},
    # {"name": "sense_id"},
    # {"name": "pronounciation"},
    # {"name": "wav_src"},
    # {"name": "translation"},
    # {"name": "definition"},
    # {"name": "krDefinition"},
    # {"name": "examples"},
    # {"name": "tags"},

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
        anki_note = genanki.Note(
            model=anki_model,
            fields=[
                word['hangul'],  # hangul
                word['id'],  # id
                word['link'],  # link
                word['homonym_number'],  # homonym_number
                word['sense_id'],  # sense_id
                word['pronounciation'],  # pronounciation
                word['wav_name'],  # wav_src
                word['translation'],  # translation
                word['definition'],  # definition
                word['krDefintion'],  # krDefintion
                word['examples'],  # examples
                word['subject_category']
                + ' | '
                + word['semantic_category']
                + ' | '
                + word['vocabulary_level']
                + ' | '
                + word['lexical_unit'],  # tags
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

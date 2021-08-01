import genanki
from src.models import *
import os


def create_deck(vocab, file_name, is_grammar):

    deck_filename = "data/apkg_files/" + file_name
    anki_deck_title = file_name.replace('.xml', '')
    if is_grammar is True:
        deck_id = 461152559
    else:
        deck_id = 929174285
    anki_deck = genanki.Deck(deck_id, anki_deck_title)

    # style = open('src/card_style.css', 'r').read()
    # vocab_model = genanki.Model(
    #     1449579167,
    #     "Korean Learner's Dictionary-Grammar",
    #     fields=[
    #         {"name": "hangul"},
    #         {"name": "pronounciation"},
    #         {"name": "wav_src"},
    #         {"name": "translation"},
    #         {"name": "definition"},
    #         {"name": "examples"},
    #         {"name": "tags"},
    #     ],
    #     templates=[
    #         {
    #             "name": "hangul > translation",
    #             "qfmt": '<p class="hangul">{{hangul}}</p>',
    #             "afmt": '''
    #         {{FrontSide}}
    #         </br>
    #         {{wav_src}}
    #         </br>
    #         <p>【{{pronounciation}}】</p>
    #         <hr id="answer">
    #         <div
    #             <p class="translation">{{translation}}</p>
    #             <p class="definition">{{definition}}</p>
    #             <a id="Link" onclick="expander()">+ Examples</a>
    #             </br>
    #             <div id="Examples">
    #                 <ul>
    #                 {{examples}}
    #                 </ul>
    #             </div>
    #             <p class="tags">{{tags}}</p>
    #         </div>
    #         <script>
    #         function expander() {
    #             let e = document.getElementById("Examples");
    #             let p = document.getElementById("Link");
    #             if (e.style.display === "block") {
    #                 p.innerHTML = "+ Examples"
    #                 e.style.display = "none"
    #             } else {
    #                 p.innerHTML = "- Examples"
    #                 e.style.display = "block"
    #             }
    #         }
    #         function playAudio() {
    #             audio = document.getElementById("Audio")
    #             audio.play()
    #         }
    #         </script>
    #     ''',
    #         }
    #     ],
    #     css=style,
    # )

    # grammar_model = genanki.Model(
    #     1448492665,
    #     "Korean Learner's Dictionary",
    #     fields=[
    #         {"name": "hangul"},
    #         {"name": "pronounciation"},
    #         {"name": "wav_src"},
    #         {"name": "translation"},
    #         {"name": "definition"},
    #         {"name": "examples"},
    #         {"name": "tags"},
    #     ],
    #     templates=[
    #         {
    #             "name": "hangul > translation",
    #             "qfmt": '<p class="hangul">{{hangul}}</p>',
    #             "afmt": '''
    #         {{FrontSide}}
    #         </br>
    #         {{wav_src}}
    #         </br>
    #         <p>【{{pronounciation}}】</p>
    #         <hr id="answer">
    #         <div
    #             <p class="translation">{{translation}}</p>
    #             <p class="definition">{{definition}}</p>
    #             <a id="Link" onclick="expander()">+ Examples</a>
    #             </br>
    #             <div id="Examples">
    #                 <ul>
    #                 {{examples}}
    #                 </ul>
    #             </div>
    #             <p class="tags">{{tags}}</p>
    #         </div>
    #         <script>
    #         function expander() {
    #             let e = document.getElementById("Examples");
    #             let p = document.getElementById("Link");
    #             if (e.style.display === "block") {
    #                 p.innerHTML = "+ Examples"
    #                 e.style.display = "none"
    #             } else {
    #                 p.innerHTML = "- Examples"
    #                 e.style.display = "block"
    #             }
    #         }
    #         function playAudio() {
    #             audio = document.getElementById("Audio")
    #             audio.play()
    #         }
    #         </script>
    #     ''',
    #         },
    #         {
    #             "name": "translation > hangul",
    #             "qfmt": '<p class="translation">{{translation}}</p>',
    #             "afmt": '''
    #         {{FrontSide}}
    #         </br>
    #         {{wav_src}}
    #         </br>
    #         <p>【{{pronounciation}}】</p>
    #         <hr id="answer">
    #         <div
    #             <p class="translation">{{hangul}}</p>
    #             <p class="definition">{{definition}}</p>
    #             <a id="Link" onclick="expander()">+ Examples</a>
    #             </br>
    #             <div id="Examples">
    #                 <ul>
    #                 {{examples}}
    #                 </ul>
    #             </div>
    #             <p class="tags">{{tags}}</p>
    #         </div>
    #         <script>
    #         function expander() {
    #             let e = document.getElementById("Examples");
    #             let p = document.getElementById("Link");
    #             if (e.style.display === "block") {
    #                 p.innerHTML = "+ Examples"
    #                 e.style.display = "none"
    #             } else {
    #                 p.innerHTML = "- Examples"
    #                 e.style.display = "block"
    #             }
    #         }
    #         function playAudio() {
    #             audio = document.getElementById("Audio")
    #             audio.play()
    #         }
    #         </script>
    #     ''',
    #         },
    #     ],
    #     css=style,
    # )

    # 0 'hangul',
    # 1 ('id'),
    # 2 ('homonym_number'),
    # 3 ('pronunciation'),
    # 4 ('wav_name'),
    # 5 ('sense_id'),
    # 6 ('translation'),
    # 7 ('definition'),
    # 8 ('krDefintion'),
    # 9 ('vocabulary_level'),
    # 10 ('semantic_category')
    # 10 ('subject_category'),
    # 11 ('wordForm'),
    # 12 ('examples')

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
                word['pronounciation'],  # pronounciation
                word['wav_name'],  # wav_src
                word['translation'],  # translation
                word['definition'],  # definition
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
        # print(word['wav_name'])
    new_deck = genanki.Package(anki_deck)
    new_deck.media_files = [
        '/users/max/Library/Application Support/Anki2/Max/collection.media'
    ]
    new_deck.write_to_file(f'data/apkg_files/{anki_deck_title}.apkg')

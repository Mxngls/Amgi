import genanki
import random
import csv

def create_deck(file):

    deck_filename = f'{(file.replace(".csv",".apkg").replace("data/csv_files/", "data/apkg_files/"))}'
    anki_deck_title = f'{deck_filename.replace(".apkg", "")}'.replace('data/apkg_files/', "")
    anki_model_name = 'Basic English Dictionary'
    model_id = random.randrange(1 << 30, 1 << 31)
    style = open('src/card_style.css', 'r').read()
    anki_notes = []

    anki_model = genanki.Model(
        model_id,
        anki_model_name,
        fields=[{"name": "hangul"}, 
                {"name": "translation"},
                {"name": "definition"}, 
                {"name": "examples"},
                {"name": "tags"}],
        templates=[
            {
                "name": "hangul > translation",
                "qfmt": '<p class="hangul">{{hangul}}</p>',
                "afmt": 
    ''' 
        {{FrontSide}}<hr id="answer">
        <div 
            <p class="translation">{{translation}}</p>
            <p class="definition">{{definition}}</p>
            <a id="Link" onclick="expander()">+ Examples</a>
            </br>
            <div id="Examples">
                <ul>
                {{examples}}
                </ul>
            </div>
            <p class="tags">{{tags}}</p>
        </div>
        <script> 
        function expander() {
            let e = document.getElementById("Examples");
            let p = document.getElementById("Link");
            if (e.style.display === "block") {
                p.innerHTML = "+ Examples"
                e.style.display = "none"
            } else {
                p.innerHTML = "- Examples"
                e.style.display = "block"
            }
        }                            
        </script>
    ''',
            },
            {
                "name": "translation > hangul",
                "qfmt": '<p class="translation">{{translation}}</p>',
                "afmt": 
    ''' 
        {{FrontSide}}<hr id="answer">
        <div 
            <p class="translation">{{hangul}}</p>
            <p class="definition">{{definition}}</p>
            <a id="Link" onclick="expander()">+ Examples</a>
            </br>
            <div id="Examples">
                <ul>
                {{examples}}
                </ul>
            </div>
            <p class="tags">{{tags}}</p>
        </div>
        <script> 
        function expander() {
            let e = document.getElementById("Examples");
            let p = document.getElementById("Link");
            if (e.style.display === "block") {
                p.innerHTML = "+ Examples"
                e.style.display = "none"
            } else {
                p.innerHTML = "- Examples"
                e.style.display = "block"
            }
        }                            
        </script>
    ''',      
            },
        ],
        css=style,
    )

    data = open(file, 'r')
    filereader = csv.reader(data, delimiter=',', quotechar='|')
    for row in filereader:
        anki_note = genanki.Note(
            model=anki_model,
            fields=[row[3], row[5], row[6], row[8], row[1] + ' | ' + row[2]],
            tags=[row[1].replace(" ", ""), row[2].replace(" ", "")]
        )
        anki_notes.append(anki_note)
    anki_notes.pop(0)   

    with open(deck_filename, 'wb') as deck:
        anki_deck = genanki.Deck(model_id, anki_deck_title)
        anki_package = genanki.Package(anki_deck)
        for anki_note in anki_notes:
            anki_deck.add_note(anki_note)
        anki_package.write_to_file(deck)


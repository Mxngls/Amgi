import genanki

style = open('card_style.css', 'r').read()

with open('template_front.html', 'r') as f:
    front = f.read()
with open('template_back.html', 'r') as f:
    back = f.read()

grammar_model = genanki.Model(
    1449579168,
    "Korean Learner's Dictionary-Grammar",
    fields=[
        {"name": "hangul"},
        {"name": "id"},
        {"name": "link"},
        {"name": "homonym_number"},
        {"name": "sense_id"},
        {"name": "pronounciation"},
        {"name": "wav_src"},
        {"name": "translation"},
        {"name": "definition"},
        {"name": "krDefinition"},
        {"name": "examples"},
        {"name": "tags"},
    ],
    templates=[
        {
            "name": "hangul > translation",
            "qfmt": '<a class="hangul" href="{{link}}">{{hangul}}</a>',
            "afmt": '''
                    {{FrontSide}}
        </br>
        </br>
        {{wav_src}}
        </br>
        <p>【{{pronounciation}}】</p>
        <hr id="answer">
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
        function playAudio() {
            audio = document.getElementById("Audio")
            audio.play()
        }
        </script>
    ''',
        }
    ],
    css=style,
)

vocab_model = genanki.Model(
    1635586141297,
    "Korean Learner's Dictionary V2",
    fields=[
        {"name": "hangul"},
        {"name": "id"},
        {"name": "link"},
        {"name": "homonym_number"},
        {"name": "pronounciation"},
        {"name": "wav_src"},
        {"name": "translation1"},
        {"name": "definition1"},
        {"name": "krDefinition1"},
        {"name": "examples1"},
        {"name": "translation2"},
        {"name": "definition2"},
        {"name": "krDefinition2"},
        {"name": "examples2"},
        {"name": "translation3"},
        {"name": "definition3"},
        {"name": "krDefinition3"},
        {"name": "examples3"},
        {"name": "translation4"},
        {"name": "definition4"},
        {"name": "krDefinition4"},
        {"name": "examples4"},
        {"name": "translation5"},
        {"name": "definition5"},
        {"name": "krDefinition5"},
        {"name": "examples5"},
        {"name": "translation6"},
        {"name": "definition6"},
        {"name": "krDefinition6"},
        {"name": "examples6"},
        {"name": "tags"},
    ],
    templates=[
        {
            "name": "hangul > translation",
            "qfmt": '<a class="hangul" href="{{link}}">{{hangul}}</a>',
            "afmt": f'''
            {front}
    ''',
        },
        {
            "name": "translation > hangul",
            "qfmt": '''<p class="translation">
            {{translation1}}{{translation2}}
            {{translation3}}{{translation4}}
            {{translation5}}{{translation6}}</p>''',
            "afmt": f'''
            {back}
    ''',
        },
    ],
    css=style,
)

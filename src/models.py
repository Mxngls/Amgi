import genanki

style = open('src/card_style.css', 'r').read()

grammar_model = genanki.Model(
    1449579167,
    "Korean Learner's Dictionary-Grammar",
    # 0 ('hangul'),
    # 1 ('id'),
    # 2 '(link)'
    # 3 ('homonym_number'),
    # 4 ('pronunciation'),
    # 5 ('wav_name'),
    # 6 ('sense_id'),
    # 7 ('translation'),
    # 8 ('definition'),
    # 9 ('krDefintion'),
    # 10 ('vocabulary_level'),
    # 11 ('semantic_category')
    # 12 ('subject_category'),
    # 13 ('wordForm'),
    # 14 ('examples')
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
    1448492665,
    "Korean Learner's Dictionary",
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
        <div id="audio" style="display:none">{{wav_src}}</div>
        <div class="pronounciation" onclick="playAudio()">【{{pronounciation}}】</div>
        <hr id="answer">
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
            audioDiv = document.getElementById("audio")
            audio = audioDiv.getElementsByTagName("*");
            audio[0].click();
        }
        </script>
    ''',
        },
        {
            "name": "translation > hangul",
            "qfmt": '<p class="translation" href="{{link}}">{{translation}}</p>',
            "afmt": '''
        {{FrontSide}}
        <div id="audio" style="display:none">{{wav_src}}</div>
        <p class="pronounciation" onclick="playAudio()">【{{pronounciation}}】</p>
        <hr id="answer">
        <div class="hangul">{{hangul}}</div>
        <p class="definition">{{definition}}</p>
        <a id="Link" onclick="expander()">+ Examples</a>
        </br>
        <div id="Examples">
            <ul>
                {{examples}}
            </ul>
        </div>
        <p class="tags">{{tags}}</p>
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
            audioDiv = document.getElementById("audio")
            audio = audioDiv.getElementsByTagName("*");
            audio[0].click();
        }
        </script>
    ''',
        },
    ],
    css=style,
)

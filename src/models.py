import genanki

style = open('src/card_style.css', 'r').read()

vocab_model = genanki.Model(
    1449579167,
    "Korean Learner's Dictionary-Grammar",
    fields=[
        {"name": "hangul"},
        {"name": "pronounciation"},
        {"name": "wav_src"},
        {"name": "translation"},
        {"name": "definition"},
        {"name": "examples"},
        {"name": "tags"},
    ],
    templates=[
        {
            "name": "hangul > translation",
            "qfmt": '<p class="hangul">{{hangul}}</p>',
            "afmt": '''
        {{FrontSide}}
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

grammar_model = genanki.Model(
    1448492665,
    "Korean Learner's Dictionary",
    fields=[
        {"name": "hangul"},
        {"name": "pronounciation"},
        {"name": "wav_src"},
        {"name": "translation"},
        {"name": "definition"},
        {"name": "examples"},
        {"name": "tags"},
    ],
    templates=[
        {
            "name": "hangul > translation",
            "qfmt": '<p class="hangul">{{hangul}}</p>',
            "afmt": '''
        {{FrontSide}}
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
        },
        {
            "name": "translation > hangul",
            "qfmt": '<p class="translation">{{translation}}</p>',
            "afmt": '''
        {{FrontSide}}
        </br>
        {{wav_src}}
        </br>
        <p>【{{pronounciation}}】</p>
        <hr id="answer">
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
        function playAudio() {
            audio = document.getElementById("Audio")
            audio.play()
        }
        </script>
    ''',
        },
    ],
    css=style,
)

# import genanki

# import uuid

# model_id = uuid.uuid1()
# anki_model_name = 'Basic English Dictionary'
# style = open('src/card_style.css', 'r').read()
# anki_deck_title = file_name
# anki_deck = genanki.Deck(model_id, anki_deck_title)

# anki_model = genanki.Model(
#     model_id,
#     anki_model_name,
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
import requests


def download_wav(url, id):
    response = requests.get(url, allow_redirects=True)
    open(
        f'/users/max/Library/Application Support/Anki2/Max/collection.media/{id}.wav',
        'wb',
    ).write(response.content)

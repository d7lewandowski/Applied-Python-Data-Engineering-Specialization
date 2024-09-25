from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching for name: {name}")
    print(wikipedia.search(name))
    if name not in wikipedia.search(name):

        return wikipedia.search(name)[0]

    return wikipedia.search(name)


def summrize_wikipedia(name):
    """Summerize wikipedia"""

    print(f"Finding wikipedia summry for name: {name}")

    return wikipedia.summary(name)


def get_textblob(text):
    """Getting text blob object and returns"""
    blob = TextBlob(text)

    return blob


def get_phrases(name):
    """Find wikipedia name and return back phrases"""
    text = summrize_wikipedia(name)
    blob = get_textblob(text)
    phrases = blob.noun_phrases

    return phrases

from spellchecker import SpellChecker
from textblob import TextBlob

text = '''
We can connect this sacredness inherent in traditional craftsmanship to the world of knowledge work. To do so, there are two key ovservationss we must first make. The first might be obvious but requires emphasis: There's is nothing intrinsic about the manual trades when it comes to generating this particular source of meaning. Any persuit - be it physical or cognitive - that supports high levels of skill can also generate a sense of sacredness.
'''

def spell_checker():
    spell = SpellChecker()
    words = text.split()
    corrected_words = {word: spell.correction(word) for word in words}
    print(corrected_words)

def text_blob():
    blob = TextBlob(text)
    corrected_text = blob.correct()
    print(corrected_text)






if __name__ == '__main__':
    text_blob()
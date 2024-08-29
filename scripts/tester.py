from db_manager.db_client import DB_CLIENT
from textblob import TextBlob

db = DB_CLIENT()

text = '''
We can connect this sacredness inherent in traditional craftsmanship to the world of knowledge work. To do so, there are two key ovservationss we must first make. The first might be obvious but requires emphasis: There's is nothing intrinsic about the manual trades when it comes to generating this particular source of meaning. Any persuit - be it physical or cognitive - that supports high levels of skill can also generate a sense of sacredness.
'''

def spell_checker():
    #textblob was more appropriate for my use case
    #spell = SpellChecker()
    words = text.split()
    corrected_words = {word: spell.correction(word) for word in words}
    print(corrected_words)

def text_blob():
    print(text)
    blob = TextBlob(text.strip())
    corrected_text = blob.correct()
    print("corrected:\n")
    print(corrected_text)


def find_missing_row():
    quotes = db.get_all_quotes()
    id_set = set()

    for row in quotes:
        id = row[5]
        id_set.add(id)

    print(len(id_set))

    for i in range(1, 267):
        #id_set.remove(i) 
        pass
        
    print(id_set)



if __name__ == '__main__':
    find_missing_row()
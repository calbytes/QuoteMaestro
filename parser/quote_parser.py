import os
import json
 
directory = 'Quotes'

def get_meta_data(str):
    data = json.loads(str)
    title = data.get('title')
    author = data.get('author')
    metadata = title, author
    print(metadata)
    return metadata

for filename in os.scandir(directory):
    if filename.is_file():
        print("filename: " + filename.name)
        file = open(filename, 'r')
        Lines = file.readlines()
        metadata = get_meta_data(Lines[0])






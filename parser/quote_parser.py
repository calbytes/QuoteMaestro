import os
import json
import re
from .quote_entry import QuoteEntry

directory = 'parser/Quotes'

def get_page_number(string):
    digits = re.findall(r'\d+', string)
    if digits:
        return int(digits[0])
    return None

def get_meta_data(str):
    data = json.loads(str)
    title = data.get('title')
    author = data.get('author')
    metadata = title, author
    return metadata

def get_quote(lines, closing_brackets):
    cur = closing_brackets[0] + 1
    end = closing_brackets[1]
    quote = ''
    while cur < end:
        if lines[cur].strip() != "":
            quote += lines[cur]
            
        cur += 1

    return quote

for filename in os.scandir(directory):
    if filename.is_file():
        #print("filename: " + filename.name)
        file = open(filename, 'r')
        Lines = file.readlines()
        metadata = get_meta_data(Lines[0])

        quotes = []
        closing_brackets = [0, 0]
        line_num = 1

        while line_num < len(Lines) : 
            line = Lines[line_num].strip()

            if line == "":
                pass
            elif line == "{":
                closing_brackets[0] = line_num
            elif line[0] == "}":
                closing_brackets[1] = line_num

            if closing_brackets[0] < closing_brackets[1]:
                quote_text = get_quote(Lines, closing_brackets)
                page_number = get_page_number(line)
                quote_entry = QuoteEntry(quote_text, metadata[0], metadata[0], page_number)
                quotes.append(quote_entry)
                closing_brackets[0] = line_num

            line_num += 1

        print(str(len(quotes)) + ' quotes found in ' + filename.name)






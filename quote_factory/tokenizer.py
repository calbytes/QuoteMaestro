import os
import json
import re
from .quote_entry import QuoteEntry

DIR = 'C:/Users/CAL/Documents/quotes_data'

def get_page_number(string):
    digits = re.findall(r'\d+', string)
    if digits:
        return int(digits[0])
    return 0

def get_meta_data(meta_data):
    #print(meta_data)
    data = json.loads(meta_data)
    title = data.get('title')
    author = data.get('author')
    return title, author

def get_quote(lines, closing_brackets):
    cur = closing_brackets[0] + 1
    end = closing_brackets[1]

    quote = ''
    while cur < end:
        quote += lines[cur]
        cur += 1

    return quote.strip()

def get_quote_entries():
    quotes = []
    for filename in os.scandir(DIR):
        if filename.is_file():
            file = open(filename, 'r')
            Lines = file.readlines()
            title, author = get_meta_data(Lines[0].strip())

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
                    quote_entry = QuoteEntry(quote_text, title, author, page_number)
                    quotes.append(quote_entry)
                    closing_brackets[0] = line_num

                line_num += 1

    return quotes

if __name__ == '__main__':
    quotes = get_quote_entries()
    print('quote files tokenized: ' + str(len(quotes)))

    i=1
    for entry in quotes:
        pass
        print(i)
        i+=1
        entry.print()

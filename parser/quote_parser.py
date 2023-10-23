import os
import json
import re
import Quote_Entry
 
directory = 'Quotes'

def get_page_number(string):
    numbers = re.findall(r'\d+', string)
    return [int(num) for num in numbers]

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
        print(" filename: " + filename.name)
        file = open(filename, 'r')
        Lines = file.readlines()
        metadata = get_meta_data(Lines[0])

        print(metadata)

        quotes = []
        closing_brackets = [0, 0]
        line_num = 1

        while line_num < len(Lines) : 
            print(">>> " + Lines[line_num])
            line = Lines[line_num].strip()

            if line == "":
                break
            elif line == "{":
                closing_brackets[0] = line_num
            elif line[0] == "}":
                closing_brackets[1] == line_num
            
            if closing_brackets[0] < closing_brackets[1]: #
                quote_text = get_quote(Lines, closing_brackets)
                quote_entry = Quote_Entry(quote_text, metadata.get(0), metadata.get(1))
                quote_page_num = get_page_number(closing_brackets[1])

                quotes.append(quote_entry)
                closing_brackets[0] == line_num

            line_num += 1

        print(quotes)
        exit(0)







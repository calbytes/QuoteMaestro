class QuoteEntry:
    def __init__(self, quote, title, author, page):
        self.quote = quote
        self.title = title
        self.author = author
        self.page = page

    def print(self):
        print("title: " + self.title)
        print("author: " + self.author)
        print("quote: " + self.quote)
        print("page: " + str(self.page))
        
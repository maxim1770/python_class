class Book:

    def __init__(self, name, author, number_pages):
        self.name = name
        self.author = author
        self.number_pages = number_pages

    def print(self):
        print(self.name, self.author, self.number_pages, end=" ")

    def SetName(self, name):
        self.name = name

    def Price(self, price_of_printing_one_page):
        return price_of_printing_one_page * self.number_pages


class PublishingHouse(Book):

    def __init__(self, name, author, number_pages, circulation, language):
        super().__init__(name, author, number_pages)
        self.circulation = circulation
        self.language = language

    def print(self):
        super().print()
        print(self.circulation, self.language, end=" ")

    def SetPr(self, circulation):
        self.circulation = circulation

    def SetLanguage(self, language):
        self.language = language

    def PriceAll(self, price_of_printing_one_page):
        return self.circulation * super().Price(price_of_printing_one_page)


ph = PublishingHouse('book_name', 'я автор', 100, 4, "русский")
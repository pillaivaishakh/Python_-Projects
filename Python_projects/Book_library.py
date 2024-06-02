class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, format, pages):
        super().__init__(title, author)
        self.format = format
        self.pages = pages
        if self.format not in ["PDF", "EPUB", "MOBI", "AZW"]:
            raise ValueError("Invalid Format")

    def __str__(self):
        return "Title: {0}\nAuthor: {1}\nFormat: {2}\nPages: {3}".format(self.title, self.author, self.format, self.pages)

class AudioBook(Book):
    def __init__(self, title, author, format, track_length):
        super().__init__(title, author)
        self.format = format
        self.track_length = track_length
        if self.format not in ["MP3", "WMA", "WAV"]:
            raise ValueError("Invalid Format")

    def __str__(self):
        return "Title: {0}\nAuthor: {1}\nFormat: {2}\nTrack Length: {3}".format(self.title, self.author, self.format, self.track_length)

# Testing the classes
try:
    e = EBook("Python", "John", "PDF", 100)
    print(e)
except ValueError as ve:
    print(ve)

try:
    a = AudioBook("Python", "John", "MP3", 100)
    print(a)
except ValueError as ve:
    print(ve)


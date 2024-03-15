import unittest
from books.book import Book

class TestBook(unittest.TestCase):
    def test_book_attributes(self):
        # Menguji atribut book
        book = Book("Python Programming", "Guido van Rossum", 2022)
        self.assertEqual(book.title, "Python Programming")
        self.assertEqual(book.author, "Guido van Rossum")
        self.assertEqual(book.year, 2022)

if __name__ == "__main__":
    unittest.main()

from books.book import Book
import json

def load_books_from_file(file_path):
    with open(file_path, 'r') as file:
        books_data = json.load(file)
    return [Book(book['title'], book['author'], book['year']) for book in books_data]

def save_books_to_file(file_path, books):
    books_data = [{'title': book.title, 'author': book.author, 'year': book.year} for book in books]
    with open(file_path, 'w') as file:
        json.dump(books_data, file, indent=4)

def add_book(books, title, author, year):
    books.append(Book(title, author, year))
    save_books_to_file('data/books.json', books)
    print('Book added successfully!')

def search_book(books, title):
    found_books = [book for book in books if book.title.lower() == title.lower()]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print('Book not found.')

def display_books(books):
    if books:
        for book in books:
            print(book)
    else:
        print('No books available.')

def main():
    books = load_books_from_file('data/books.json')
    
    while True:
        print("\nBook Catalog Menu:")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display All Books")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            add_book(books, title, author, year)
        elif choice == '2':
            title = input("Enter title to search: ")
            search_book(books, title)
        elif choice == '3':
            display_books(books)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

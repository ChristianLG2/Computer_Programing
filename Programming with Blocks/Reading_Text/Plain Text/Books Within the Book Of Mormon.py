with open("books.txt") as Book_of_Mormon:
    for books in Book_of_Mormon:
        books = books.strip()
        print(books)
    

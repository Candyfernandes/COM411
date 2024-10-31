def search_books(file_path):
    print("searching...")
    sections = ""
    books = "Books:\n"
    try:
        with open(file_path) as books_file:
            for line in books_file:


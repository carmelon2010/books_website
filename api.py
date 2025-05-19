from googlesearch import search

def find_book_link(book_name):
    query = f"{book_name} read online"
    results = search(query, num_results=1)
    for i in results:
        return i
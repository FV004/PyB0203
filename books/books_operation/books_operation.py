def add_book():
    book = {}
    book['title'] = input('Enter title : ')
    book['author'] = input('Enter author : ')
    book['pages'] = int(input('Enter number of pages : '))
    book['price'] = int(input('Enter price : '))
    book['isbn'] = input('Enter ISBN : ')
    books.append(book)
def list_book():
    for book in books :
        print(book)
def find_book():
    isbn = input('Enter ISBN to find : ')
    for book in books:
        if isbn == book['isbn']:
            print(book)
    else :
        print('This book did not find')
def delete_book():
    isbn = input('Enter ISBN to find : ')
    for book in books:
        if isbn == book['isbn']:
            books.remove(book)
            print('The book has been deleted')
            break
    else :
       print('This book did not find')
books = []
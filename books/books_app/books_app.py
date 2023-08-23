# V 1.0.0
import books_operation as bo
# ----------------------------main------------------------------
while True :
    print('===================================')
    print('Press A to add book')
    print('Press L to list all books')
    print('Press F to find a book')
    print('Press D to delete a book')
    print('press Q to quit app')
    print('===================================')
    choice = input('Enter your choice : ').upper()
    if choice == 'A':
        bo.add_book()
    elif choice == 'L':
        bo.list_book()
    elif choice == 'F':
        bo.find_book()
    elif choice == 'D':
        bo.delete_book()
    elif choice == 'Q':
        print('Bay baby')
        break
    else :
        print('Wrong choice !')
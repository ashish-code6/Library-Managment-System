def show_menu():
    print("********Librarry Mangment System**********")
    print("1.Add books")
    print("2.Display books")
    print("3.Search books")
    print("4.Borrow books")
    print("5.Return Books")
    print("6.Display Borrowed Books")
    print("7.Edit Books")
    print("8.Delete Book")
    print("9.Exit")
# ------------------------------------------------------
books = []
borrow_book = []

def add_book():
    book_name = input("Enter book name: ")
    book_author = input("Enter book author: ")
    book_id = int(input("Enter book ID: "))

    book_exist = False

    for x in books:
        if book_id == x["id"]:
            book_exist = True
            break

    book = {
        "name": book_name,
        "author": book_author,
        "id": book_id
    }

    if book_exist != True:
        books.append(book)
        print("Book added successfully!")
    else:
        print("Book ID already exists!")
# ------------------------------------------------
def display_books():
    len_books = len(books)
    if len_books == 0:
        print("No books found.")
        return
    for x in books:
        print("book id: ", x["id"])
        print("book name: ", x["name"].upper())
        print("book author: ", x["author"].upper())
        print("-----------------------------")
print("Books displayed successfully!")
#-------------------------------------------------------
def search_book():
    book_name = input("Search book name: ")

    for x in books:
        if book_name == x["name"]:
            print("Book Found")
            return

    print("Book Not Found")
#----------------------------------------------------------
def borrow(): 
    book_rent=input("Enter the book name U want to Rent:\n")
    for x in books:
        if book_rent == x["name"] and len(books) != 0:
              borrow_book.append(x)
              books.remove(x)
              return
            # print("hello")
       
    print("Book Does not Exist!!!!")
#-------------------------------------------------------------
def return_book():
    book_return=input("Enter the book name U want to Return:\n")
    for x in borrow_book:
        if book_return == x["name"] and len(borrow_book) != 0:
              books.append(x)
              borrow_book.remove(x)
            # print("hello")
        else:
              print("Book Does not Exist!!!!")
#-------------------------------------------------------------
def display_borrowed_books():
    len_borrow_book = len(borrow_book)
    if len_borrow_book == 0:
        print("No books found.")
        return
    for x in borrow_book:
        print("book id: ", x["id"])
        print("book name: ", x["name"].upper())
        print("book author: ", x["author"].upper())
        print("-----------------------------")
print("Borrowed Books displayed successfully!")

#-------------------------------------------------------------
def edit_books():
    book_id = int(input("Enter the book ID: "))

    for x in books:
        if book_id == x["id"]:
            new_name = input("Enter new book name: ")
            new_author = input("Enter new author name: ")

            x["name"] = new_name
            x["author"] = new_author

            print("Book updated successfully")
            return

    print("Book ID not found")

def delete_book():
    book_id = int(input("Enter the book ID: "))

    for x in books:
        if book_id == x["id"]:
            books.remove(x)
            print("Book deleted successfully")
            return

    print("Book ID not found")
# -----------------------------------------------------------
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        borrow()
    elif choice == '5':
        return_book()
    elif choice == '6':
        display_borrowed_books()
    elif choice == '7':
        edit_books()
    elif choice == '8':
        delete_book()
    elif choice == '9':
        print('exit')
        break
    else:
        print("Invalid choice. Please try again.")

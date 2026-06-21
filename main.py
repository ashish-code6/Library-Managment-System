def show_menu():
    print("********Librarry Mangment System**********")
    print("1.Add books")
    print("2.Display books")
    print("3.Search books")
    print("4.Borrow books")
    print("5.Return Books")
    print("6.delete books")
    print("7.Exit")

# ------------------------------------------------------
books = []
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
	book_name= input("Search book name: ")
	for x in books:
		if book_name==x["name"]:
			print ("book found")
		else:
			print("books not found")
#-------------------------------------------------------
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '7':
        print('exit')
        break
    else:
        print("Invalid choice. Please try again.")
    


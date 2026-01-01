# Library Book Management & Analysis System

library = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category (Fiction / Science / History): ")
    copies = int(input("Enter Number of Copies: "))

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "copies": copies
    }

    library.append(book)
    print("✅ Book added successfully!\n")


def view_books():
    if not library:
        print("❌ No books available.\n")
        return

    print("\n📚 Library Books")
    for book in library:
        print("----------------------------")
        print("ID      :", book["book_id"])
        print("Title   :", book["title"])
        print("Author  :", book["author"])
        print("Category:", book["category"])
        print("Copies  :", book["copies"])
    print()


def total_books():
    total = 0
    for book in library:
        total += book["copies"]

    print("📊 Total Books in Library:", total, "\n")


def category_wise_books():
    category_count = {}

    for book in library:
        cat = book["category"]
        copies = book["copies"]

        if cat in category_count:
            category_count[cat] += copies
        else:
            category_count[cat] = copies

    print("\n📊 Category-wise Book Count")
    for cat, count in category_count.items():
        print(cat, ":", count)
    print()


def search_book():
    search_title = input("Enter book title to search: ")

    found = False
    for book in library:
        if book["title"].lower() == search_title.lower():
            print("\n🔍 Book Found")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Copies:", book["copies"])
            found = True
            break

    if not found:
        print("❌ Book not found.\n")



while True:
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Total Books Count")
    print("4. Category-wise Book Count")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        total_books()
    elif choice == "4":
        category_wise_books()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print("👋 Exiting Library System")
        break
    else:
        print("❌ Invalid choice. Try again.\n")

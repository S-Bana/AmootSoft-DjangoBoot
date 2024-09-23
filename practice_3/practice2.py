class Book:
    def __init__(self):
        self.title = None
        self.author = None
        self.shabk = None
        self.available_versions = None
        


class Member:
    def __init__(self, name, membership_number, borrowed_books):
        self.name = name
        self.membership_number = membership_number
        self.borrowed_books = borrowed_books


class Library(Book):
    def __init__(self):
        super().__init__()
    def add_book(self):
        self.author = input('Enter auther name : ')
        self.title = input('Enter title : ')
        self.shabk = input('Enter shabk : ')
        self.available_versions = input('Enter available_versions : ')
    

def main():
    manager = Library()
    while True:
        print("\n1. Add book")
        print("2. Remove book")
        print("3. Return book")
        print("4. Lend book")
        print("5. List available book")
        print("6. Search books")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            manager.add_book()
        elif choice == '2':
            manager.delete_expense()
        elif choice == '3':
            manager.total_expense()
        elif choice == '4':
            manager.list_expenses_by_date()
        elif choice == '5':
            manager.generate_report()
        elif choice == '6':
            manager.Search_books()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

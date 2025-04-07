class student:
    def _init_(self,student_Name,ID,Std,Email):
        self.student_name=student_Name
        self.ID=ID
        self.Std=Std
        self.Email=Email
class book:
    def _init_(self,Book_name,Book_id,Author):
        self.Book_name=Book_name
        self.Book_Id=Book_id
        self.Author=Author
class library:
    def _init_(self):
        students={}
        books={}
print("library_management_System_menu:")
print("1.Book issue")
print("2.Book Deposit")
print("3.Administration Menu")
print("4.Exit")
choice=input("Enter your choice from the above:")
if input=="1":
    def issue_book(self):
        book_id = input("Enter book ID: ")
        student_id = input("Enter student ID: ")
        if book_id in self.books and student_id in self.students:
            book = self.books[book_id]
            if not book.issued:
                book.issued = True
                print("Book issued successfully!")
            else:
                print("Book is already issued!")
        else:
            print("Book or student record not found!")
elif input=="2":
    def deposit_book(self):
        book_id = input("Enter book ID: ")
        if book_id in self.books:
            book = self.books[book_id]
            if book.issued:
                book.issued = False
                print("Book deposited successfully!")
            else:
                print("Book is not issued!")
elif input=="3":
    print("Admin menu\n")
    print("Select options from the below\n")
    print("1.Create students record\n")
    print("2.Display all students records\n")
    print("3.Display specific zstudents records\n")
    print("4.Modify student record\n")
    print("5.Delete student record\n")
    print("6.Create book\n")
    print("7.Display all books\n")
    print("8.Display specific book\n")
    print("9.Modify book\n")
    print("10.Delete book record\n")
    admin_choice = input("Enter your choice from the above:")
    if input=="1":
        def create_student(self):
            id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            email = input("Enter student email: ")
            std=input("Enter student standard:")
            self.students[student.id] = student(student.id, student_name, email,std)
            print("Student record created successfully!")
    elif input=="2":
        def display_all_students(self):
            if not self.students:
                print("No student records found!")
            else:
                for student in self.students.values():
                    print(f"Student ID: {student.id}, Name: {student.name}, Email: {student.email}")
    elif input=="3":
        def display_specific_student(self):
            student_id = input("Enter student ID: ")
            if student_id in self.students:
                student = self.students[student_id]
                print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}")
            else:
                print("Student record not found!")
    elif input=="4":
        def modify_student(self):
            student_id = input("Enter student ID: ")
            if student_id in self.students:
                student = self.students[student_id]
                print("Enter new details (press enter to skip):")
                student.name = input(f"Name ({student.name}): ")
                student.email = input(f"Email ({student.email}): ")
                print("Student record modified successfully!")
            else:
                print("Student record not found!")
    elif input=="5":
        def delete_student(self):
            student_id = input("Enter student ID: ")
            if student_id in self.students:
                del self.students[student_id]
                print("Student record deleted successfully!")
            else:
                print("Student record not found!")
    elif input=="6":
        def create_book(self):
            book_id = input("Enter book ID: ")
            book_name = input("Enter book title: ")
            author = input("Enter book author: ")
            self.books[book_id] = book(book_id, book_name, author)
            print("Book record created successfully!")
    elif input=="7":
        def display_all_books(self):
            if not self.books:
                print("No book records found!")
            else:
                for book in self.books.values():
                    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Issued: {book.issued}")

    elif input=="8":
        def display_specific_book(self):
            book_id = input("Enter book ID: ")
            if book_id in self.books:
                book = self.books[book_id]
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Issued: {book.issued}")
            else:
                print("Book record not found!")
    elif input=="9":
        def modify_book(self):
            book_id = input("Enter book ID: ")
            if book_id in self.books:
                book = self.books[book_id]
                print("Enter new details (press enter to skip):")
                book.title = input(f"Title ({book.title}): ") or book.title
                book.author = input(f"Author ({book.author}): ") or book.author
                print("Book record modified successfully!")
            else:
                print("Book record not found!")
elif input == "10":
    def delete_book(self):
        book_id = input("Enter book ID: ")
        if book_id in self.books:
            del self.books[book_id]
            print("Book record deleted successfully!")
        else:
            print("Book record not found!")
else:
    print("You have existed the system.")


















































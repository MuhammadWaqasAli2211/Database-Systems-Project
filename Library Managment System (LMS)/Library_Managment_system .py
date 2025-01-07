import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 
from PIL import ImageTk, Image
from datetime import datetime, timedelta

db = mysql.connector.connect(
    host = "localhost", 
    user = "root",             
    password = "##umardb71@@", 
    database = "LibraryManagement"
)
cursor = db.cursor()

#login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("1550x800")
login_window.config(bg="lightpink")

try:
    image = Image.open("icons8-library-64.png")
    photo = ImageTk.PhotoImage(image)
    login_window.iconphoto(True, photo)

except Exception as e:
    print(f"Error loading image: {e}")

header_label = tk.Label(login_window, text="Library Management System", font=("times new roman", 45 , "bold"), bg="purple", fg="white", bd=3)
header_label.pack(fill=tk.X, pady=7)
header_label = tk.Label(login_window, text="Login", font=("times new roman", 45 , "bold"), bg="lightpink", fg="black", bd=3)
header_label.pack(fill=tk.X, pady=7)
button_frame = tk.Frame(login_window, bd=4, bg="lightpink")
button_frame.place(relx=0.5, rely=0.5, anchor="center")

button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_rowconfigure(1, weight=1)
button_frame.grid_rowconfigure(2, weight=1)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)


lbl_username = tk.Label(button_frame, text="Username:", font=("times new roman", 23, "bold"),bg="lightpink", fg="black")
lbl_username.grid(row=1, column=1, padx= 10, pady=10, sticky=tk.W)
entry_username = tk.Entry(button_frame)
entry_username.grid(row=1, column=2, padx= 10, pady=10, sticky=tk.W, columnspan=2)


lbl_password = tk.Label(button_frame, text="Password:", font=("times new roman", 23, "bold"), bg="lightpink", fg="black")
lbl_password.grid(row=2, column=1, padx= 10, pady=10, sticky=tk.W)
entry_password = tk.Entry(button_frame, show="*") 
entry_password.grid(row=2, column=2, padx= 10, pady=10, sticky=tk.W, columnspan=2)


def create_main_window():
    # Create the main window
    main_window = tk.Tk()
    main_window.title("Library Management System")
    main_window.geometry("1550x800")
    main_window.config(bg="lightpink")
    

    # Heading label
    header_label = tk.Label(main_window, text="Library Management System", font=("times new roman", 35, "bold"), fg="white", bg="darkblue")
    header_label.pack(fill=tk.X, pady=20)
    
    button_frame = tk.Frame(main_window, bd=4, bg="lightpink")
    button_frame.place(x=100, y=100, width=1150, height=600)
    

    # Button to Add Member
    btn_add_member = tk.Button(button_frame, text="Add Member", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3 , command=lambda: insert_member())
    btn_add_member.grid(row=0, column=0, padx= 30, pady=30)

    # Button to Add Book
    btn_add_book = tk.Button(button_frame, text="Add Book", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3 ,  command=lambda: insert_book())
    btn_add_book.grid(row=0, column=1, padx= 30, pady=30)

    # Button to Update Member
    btn_update_member = tk.Button(button_frame, text="Update Member", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3, command=lambda: update_member())
    btn_update_member.grid(row=0, column=2, padx= 30, pady=30)

    # Button to Update Book
    btn_update_book = tk.Button(button_frame, text="Update Book", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3,  command=lambda: update_book())
    btn_update_book.grid(row=0, column=3, padx= 30, pady=30)

    # Button to Delete Member
    btn_delete_member = tk.Button(button_frame, text="Delete Member", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3 ,  command=lambda: delete_member())
    btn_delete_member.grid(row=1, column=0, padx= 30, pady=30)

    # Button to Delete Book
    btn_delete_book = tk.Button(button_frame, text="Delete Book", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3 , command=lambda: delete_book())
    btn_delete_book.grid(row=1, column=1, padx= 30, pady=30)

    # Button to Borrow Book
    btn_borrow = tk.Button(button_frame, text="Borrow Book",font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3, command=lambda: borrow_book())
    btn_borrow.grid(row=1, column=2, padx= 30, pady=30)

    # Button to Return Book
    btn_return = tk.Button(button_frame, text="Return Book", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3, command=lambda: return_book())
    btn_return.grid(row=1, column=3, padx= 30, pady=30)

    # Button to View Member
    btn_view_member = tk.Button(button_frame, text="View Member", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3, command=lambda: load_members())
    btn_view_member.grid(row=2, column=0, padx= 30, pady=30)
    
# Button to search Member
    btn_search_member = tk.Button(button_frame, text="Search Member", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3, command= search_member)
    btn_search_member.grid(row=2, column=1, padx= 30, pady=30)

    # Button to Search Books
    btn_search_books = tk.Button(button_frame, text="Search Books", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3 , command=lambda: search_book())
    btn_search_books.grid(row=2, column=2, padx= 30, pady=30)
    
    # Button to view Books
    btn_view_books = tk.Button(button_frame, text="View Books", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3 , command=lambda: load_books())
    btn_view_books.grid(row=2, column=3, padx= 30, pady=30)
    
    # Button to view Transactions 
    btn_transaction = tk.Button(button_frame, text="View Transaction", font=("times new roman", 17, "bold"), bg="purple", fg="white", width=15, height=3 , command=lambda: view_transactions())
    btn_transaction.grid(row=3, column=1, padx= 30, pady=17, columnspan=2)

def validate_login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "admin" and password == "password123":
            messagebox.showinfo("Login Success", "Login Successful! Welcome to the Library Management System.")
            login_window.destroy()  
            create_main_window() 
        else:
            messagebox.showerror("Login Error", "Invalid username or password. Please try again.")

    # Login Button
btn_login = tk.Button(button_frame, text="Login", font=("times new roman", 20, "bold"), bg="purple", fg="white", command=validate_login)
btn_login.grid(row=6, column=1, pady=35, padx=35, columnspan=2)

#Functions for every button in the main window 
def load_books():
    # Create a new window
    ViewBooksWindow = tk.Toplevel()
    ViewBooksWindow.title("Books")
    ViewBooksWindow.geometry("600x400")  # Adjust the size as needed

    TitleLabel = tk.Label(ViewBooksWindow, text="Books", font=("Arial", 20, "bold"), bg="darkblue", fg="white", padx=10, pady=5)
    TitleLabel.pack(fill=tk.X)

    style = ttk.Style()
    style.theme_use("default")

    style.configure(
    "Treeview.Heading",
    background="lightblue", 
    foreground="black",     
    font=("Arial", 12, "bold")
)

    bookframe = tk.Frame(ViewBooksWindow, bd=4, relief=tk.RIDGE, bg="lightblue")
    bookframe.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    
    booktable = ttk.Treeview(bookframe, columns=("ID", "Title", "Author", "Publisher", "Quantity"), show="headings",style="Treeview")
    booktable.pack(fill=tk.BOTH, expand=True)

    for col in ("ID", "Title", "Author", "Publisher", "Quantity"):
        booktable.heading(col, text=col)
        booktable.column(col, width=100, anchor=tk.CENTER)

    
    cursor.execute("SELECT * FROM Books")
    booktable.delete(*booktable.get_children())  
    for row in cursor.fetchall():
        booktable.insert("", tk.END, values=row)


# View members table new code 
def load_members():
    # Create a new window
    ViewMembersWindow = tk.Toplevel()
    ViewMembersWindow.title("Members")
    ViewMembersWindow.geometry("600x400")  
    

    # Add a title label at the top
    TitleLabel = tk.Label(ViewMembersWindow, text="Members", font=("Arial", 20, "bold"), bg="lightgreen", fg="black", padx=10, pady=5)
    TitleLabel.pack(fill=tk.X)


    style = ttk.Style()
    style.theme_use("default")

    
    style.configure(
    "Treeview.Heading",
    background="green",  
    foreground="white",     
    font=("Arial", 12, "bold") 
)

    memberframe = tk.Frame(ViewMembersWindow, bd=4, relief=tk.RIDGE, bg="lightgreen")
    memberframe.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    membertable = ttk.Treeview(memberframe, columns=("ID", "Name", "Email", "Phone", "Date"), show="headings",style="Treeview")
    membertable.pack(fill=tk.BOTH, expand=True)

    for col in ("ID", "Name", "Email", "Phone", "Date"):
        membertable.heading(col, text=col)
        membertable.column(col, width=100, anchor=tk.CENTER)

    cursor.execute("SELECT * FROM Members")
    membertable.delete(*membertable.get_children())  
    for row in cursor.fetchall():
        membertable.insert("", tk.END, values=row)


# insert member into member table  new code 
def insert_member():
    def SaveMember():
        # Validate input fields
        if not all([MemberName.get(), MemberEmail.get(), MemberPhone.get()]):
            messagebox.showerror("Error", "Please fill all member details.")
            return

        if not MemberPhone.get().isdigit() or len(MemberPhone.get()) != 11:
            messagebox.showerror("Error", "Phone Number must be an integer with exactly 11 digits.")
            return

        if "@" not in MemberEmail.get():
            messagebox.showerror("Error", "Email must contain '@'.")
            return
        try:

            cursor.execute(
                "INSERT INTO Members (Name, Email, PhoneNumber, MembershipDate) VALUES (%s, %s, %s, NOW())",
                (MemberName.get(), MemberEmail.get(), MemberPhone.get())
            )
            db.commit()
            messagebox.showinfo("Success", "Member added successfully.")
            InsertMemberWindow.destroy()  
        except Exception as e:
            messagebox.showerror("Error", str(e))


    InsertMemberWindow = tk.Toplevel()
    InsertMemberWindow.title("Insert Member")
    InsertMemberWindow.geometry("600x500")  
    InsertMemberWindow.configure(bg="lightgreen")


    tk.Label(InsertMemberWindow, text="INSERT MEMBER", font=("Arial", 20, "bold"), bg="darkgreen", fg="white", pady=10).pack(fill= tk.X)


    TableFrame = tk.Frame(InsertMemberWindow, bg="lightgreen")
    TableFrame.pack(expand=True, fill= tk.BOTH, padx=20, pady=20)

    # Member ID
   # tk.Label(TableFrame, text="Member ID", font=("Arial", 12), bg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky= tk.W)
   # MemberId = tk.Entry(TableFrame, width=30)
   # MemberId.grid(row=0, column=1, padx=10, pady=10)

    # Name
    tk.Label(TableFrame, text="Name", font=("Arial", 12), bg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky= tk.W)
    MemberName = tk.Entry(TableFrame, width=30)
    MemberName.grid(row=1, column=1, padx=10, pady=10)

    # Email
    tk.Label(TableFrame, text="Email", font=("Arial", 12), bg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    MemberEmail = tk.Entry(TableFrame, width=30)
    MemberEmail.grid(row=2, column=1, padx=10, pady=10)

    # Phone
    tk.Label(TableFrame, text="Phone", font=("Arial", 12), bg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    MemberPhone = tk.Entry(TableFrame, width=30)
    MemberPhone.grid(row=3, column=1, padx=10, pady=10)

    
    InsertButton = tk.Button(TableFrame, text="Add Member", font=("Arial", 14), bg="darkblue", fg="white", command=SaveMember)
    InsertButton.grid(row=4, column=0, columnspan=2, pady=20)  # Place the button below the form fields

    TableFrame.grid_rowconfigure(0, weight=1)
    TableFrame.grid_rowconfigure(1, weight=1)
    TableFrame.grid_rowconfigure(2, weight=1)
    TableFrame.grid_rowconfigure(3, weight=1)
    TableFrame.grid_rowconfigure(4, weight=1)  
    
    TableFrame.grid_columnconfigure(0, weight=1)
    TableFrame.grid_columnconfigure(1, weight=2)

    # Ensure the content is centered in the form frame
    TableFrame.place(relx=0.5, rely=0.5, anchor="center")


# Delete member new code
def delete_member():
    def DeleteMember():
        if not MemberID.get():
            messagebox.showerror("Error", "Please enter Member ID.")
            return
        try:
            cursor.execute("DELETE FROM Members WHERE MemberID = %s", (MemberID.get(),))
            db.commit()
            if cursor.rowcount == 0:  # Check if any rows were affected
                messagebox.showerror("Error", "No member found with this ID.")
            else:
                messagebox.showinfo("Success", "Member deleted successfully.")
                DeleteWindow.destroy()  

        except Exception as e:
            messagebox.showerror("Error", str(e))


    DeleteWindow = tk.Toplevel()
    DeleteWindow.title("Delete Member")
    DeleteWindow.geometry("400x200")
    DeleteWindow.resizable(False, False)
    DeleteWindow.configure(bg="lightyellow")

    # Title label
    tk.Label(DeleteWindow, text="DELETE MEMBER", font=("Arial", 18, "bold"), bg="lightyellow", fg="red").pack(pady=10)

    # Input frame
    InputFrame = tk.Frame(DeleteWindow, bg="lightyellow")
    InputFrame.pack(pady=10)

    tk.Label(InputFrame, text="Member ID:", font=("Arial", 12), bg="lightyellow").grid(row=0, column=0, padx=10, pady=10)
    MemberID = tk.Entry(InputFrame, font=("Arial", 12), width=20)
    MemberID.grid(row=0, column=1, padx=10, pady=10)
    
    # Delete button
    tk.Button(DeleteWindow, text="Delete Member", command=DeleteMember, bg="red", fg="white", font=("Arial", 12), width=15).pack(pady=20)


# Add book into the book table new code
def insert_book():
    def SaveBook():
        # Validate input fields
        if not all([BookTitle.get(), BookAuthor.get(), BookPublisher.get(), BookQuantity.get()]):
            messagebox.showerror("Error", "Please fill all book details.")
            return
        
        
        try:
            # BookIdVal = int(BookID.get())
            BookQuantityVal = int(BookQuantity.get())
        except ValueError:
            messagebox.showerror("Error", "Book ID and Quantity must be integers.")
            return
        
        try:
            cursor.execute(
                "INSERT INTO Books (Title, Author, Publisher, Quantity) VALUES (%s, %s, %s, %s)",
                (BookTitle.get(), BookAuthor.get(), BookPublisher.get(), BookQuantityVal)
            )
            db.commit()
            messagebox.showinfo("Success", "Book added successfully.")
            SaveMemberWindow.destroy() 
        except Exception as e:
            messagebox.showerror("Error", str(e))

    
    SaveMemberWindow = tk.Toplevel()
    SaveMemberWindow.title("Insert Book")
    SaveMemberWindow.geometry("600x500") 
    SaveMemberWindow.configure(bg="lightblue")

    # Title label
    tk.Label(SaveMemberWindow, text="INSERT BOOK", font=("Arial", 20, "bold"), bg="darkblue", fg="white", pady=10).pack(fill=tk.X)


    TableFrame = tk.Frame(SaveMemberWindow, bg="lightblue")
    TableFrame.pack(expand=True, fill= tk.BOTH, padx=20, pady=20)

    # Book ID
    # tk.Label(TableFrame, text="Book ID", font=("Arial", 12), bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    # BookID = tk.Entry(TableFrame, width=30)
    # BookID.grid(row=0, column=1, padx=10, pady=10)

    # Title
    tk.Label(TableFrame, text="Title", font=("Arial", 12), bg="lightblue").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    BookTitle = tk.Entry(TableFrame, width=30)
    BookTitle.grid(row=1, column=1, padx=10, pady=10)

    # Author
    tk.Label(TableFrame, text="Author", font=("Arial", 12), bg="lightblue").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    BookAuthor = tk.Entry(TableFrame, width=30)
    BookAuthor.grid(row=2, column=1, padx=10, pady=10)

    # Publisher
    tk.Label(TableFrame, text="Publisher", font=("Arial", 12), bg="lightblue").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    BookPublisher = tk.Entry(TableFrame, width=30)
    BookPublisher.grid(row=3, column=1, padx=15, pady=10)

    # Quantity
    tk.Label(TableFrame, text="Quantity", font=("Arial", 12), bg="lightblue").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    BookQuantity = tk.Entry(TableFrame, width=30)
    BookQuantity.grid(row=4, column=1, padx=10, pady=10)

    InsertButton = tk.Button(TableFrame, text="Add Book", font=("Arial", 14), bg="darkblue", fg="white", command=SaveBook)
    InsertButton.grid(row=5, column=0, columnspan=2, pady=20)  # Place the button below the form fields
    TableFrame.grid_rowconfigure(0, weight=1)
    TableFrame.grid_rowconfigure(1, weight=1)
    TableFrame.grid_rowconfigure(2, weight=1)
    TableFrame.grid_rowconfigure(3, weight=1)
    TableFrame.grid_rowconfigure(4, weight=1)
    TableFrame.grid_rowconfigure(5, weight=1) 
    
    TableFrame.grid_columnconfigure(0, weight=1)
    TableFrame.grid_columnconfigure(1, weight=2)

    TableFrame.place(relx=0.5, rely=0.5, anchor="center")

# delete book from book table 
def delete_book():
    def DeleteBook():
        book_id = BookID.get()
        if not book_id:
            messagebox.showerror("Error", "Please enter Book ID.")
            return
        if not book_id.isdigit():
            messagebox.showerror("Error", "Book ID must be an integer.")
            return
        try:
            cursor.execute("DELETE FROM Books WHERE BookID = %s", (book_id,))
            db.commit()
            if cursor.rowcount == 0:  # Check if any rows were affected
                messagebox.showerror("Error", "No book found with this ID.")
            else:
                messagebox.showinfo("Success", "Book deleted successfully.")
                DeleteWindow.destroy()  # Close the delete book window
                
        except Exception as e:
            messagebox.showerror("Error", str(e))

    DeleteWindow = tk.Toplevel()
    DeleteWindow.title("Delete Book")
    DeleteWindow.geometry("400x200")
    DeleteWindow.resizable(False, False)
    DeleteWindow.configure(bg="lightyellow")

    # Title label
    tk.Label(DeleteWindow, text="DELETE BOOK", font=("Arial", 18, "bold"), bg="lightyellow", fg="red").pack(pady=10)

    # Input frame
    InputFrame = tk.Frame(DeleteWindow, bg="lightyellow")
    InputFrame.pack(pady=10)

    tk.Label(InputFrame, text="Book ID:", font=("Arial", 12), bg="lightyellow").grid(row=0, column=0, padx=10, pady=10)
    BookID = tk.Entry(InputFrame, font=("Arial", 12), width=20)
    BookID.grid(row=0, column=1, padx=10, pady=10)
    
    # Delete button
    tk.Button(DeleteWindow, text="Delete Book", command=DeleteBook, bg="red", fg="white", font=("Arial", 12), width=15).pack(pady=20)
# check update code

# UPDATE A BOOK
def update_book():
    # Create a new window for updating books
    update_window = tk.Toplevel()
    update_window.title("Update Book")
    update_window.geometry("600x500")  # Adjusted size for better fit
    update_window.configure(bg="lightpink")  # Updated theme

    # Title label
    tk.Label(update_window, text="UPDATE BOOK", font=("Arial", 20, "bold"), bg="purple", fg="white", pady=10).pack(fill=tk.X)

    # Frame for form fields
    TableFrame = tk.Frame(update_window, bg="lightpink")
    TableFrame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Labels and entry fields for book details
    tk.Label(TableFrame, text="Book ID", font=("Arial", 12), bg="lightpink").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    update_book_id = tk.Entry(TableFrame, width=30)
    update_book_id.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Title", font=("Arial", 12), bg="lightpink").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    update_book_title = tk.Entry(TableFrame, width=30)
    update_book_title.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Author", font=("Arial", 12), bg="lightpink").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    update_book_author = tk.Entry(TableFrame, width=30)
    update_book_author.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Publisher", font=("Arial", 12), bg="lightpink").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    update_book_publisher = tk.Entry(TableFrame, width=30)
    update_book_publisher.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Quantity", font=("Arial", 12), bg="lightpink").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    update_book_quantity = tk.Entry(TableFrame, width=30)
    update_book_quantity.grid(row=4, column=1, padx=10, pady=10)

    # Function to perform the update
    def perform_update():
        book_id = update_book_id.get().strip()
        title = update_book_title.get().strip()
        author = update_book_author.get().strip()
        publisher = update_book_publisher.get().strip()
        quantity = update_book_quantity.get().strip()

        if not all([book_id, title, author, publisher, quantity]):
            messagebox.showerror("Error", "Please fill all the fields.")
            return

        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a valid number.")
            return

        try:
            # Check if the book exists
            cursor.execute("SELECT BookID FROM Books WHERE BookID = %s", (book_id,))
            book = cursor.fetchone()

            if not book:
                messagebox.showerror("Error", "Book not found. Please enter a valid Book ID.")
                return

            # Perform the update
            query = """UPDATE Books 
                    SET Title = %s, Author = %s, Publisher = %s, Quantity = %s 
                    WHERE BookID = %s"""
            cursor.execute(query, (title, author, publisher, int(quantity), book_id))
            db.commit()

            messagebox.showinfo("Success", "Book details updated successfully.")
            
            update_window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Update button (Centered and in the next row)
    update_button = tk.Button(TableFrame, text="Update Book", font=("Arial", 14), bg="darkblue", fg="white", command=perform_update)
    update_button.grid(row=5, column=0, columnspan=2, pady=20)

    # Centering the form
    TableFrame.grid_rowconfigure(0, weight=1)
    TableFrame.grid_rowconfigure(1, weight=1)
    TableFrame.grid_rowconfigure(2, weight=1)
    TableFrame.grid_rowconfigure(3, weight=1)
    TableFrame.grid_rowconfigure(4, weight=1)
    TableFrame.grid_rowconfigure(5, weight=1)  # Row for the button

    TableFrame.grid_columnconfigure(0, weight=1)
    TableFrame.grid_columnconfigure(1, weight=2)

    # Ensure the content is centered in the form frame
    TableFrame.place(relx=0.5, rely=0.5, anchor="center")


# borrow book code 
def borrow_book():

    borrow_window = tk.Toplevel()
    borrow_window.title("Borrow Book")
    borrow_window.geometry("600x400")  # Adjusted size for better alignment
    borrow_window.configure(bg="lightpink")  # Updated theme to match sample code

    
    tk.Label(borrow_window, text="BORROW BOOK", font=("Arial", 20, "bold"), bg="purple", fg="white", pady=10).pack(fill=tk.X)

    
    FormFrame = tk.Frame(borrow_window, bg="lightpink")
    FormFrame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    
    tk.Label(FormFrame, text="Book ID", font=("Arial", 12), bg="lightpink").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    book_id_entry = tk.Entry(FormFrame, width=30)
    book_id_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(FormFrame, text="Member ID", font=("Arial", 12), bg="lightpink").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    member_id_entry = tk.Entry(FormFrame, width=30)
    member_id_entry.grid(row=1, column=1, padx=10, pady=10)

    
    def confirm_borrow():
        # Retrieve inputs
        book_id = book_id_entry.get().strip()
        member_id = member_id_entry.get().strip()
        issue_date = datetime.now().date()
        due_date = issue_date + timedelta(days=7)

        # Validation
        if not book_id or not member_id:
            messagebox.showerror("Error", "Please fill all the fields.")
            return

        try:
            
            cursor.execute("SELECT Quantity FROM Books WHERE BookID = %s", (book_id,))
            book = cursor.fetchone()
            if not book:
                messagebox.showerror("Error", "Book ID does not exist.")
                return
            if book[0] <= 0:
                messagebox.showerror("Error", "Book is out of stock.")
                return

            
            query = """
            INSERT INTO Transactions (BookID, MemberID, IssueDate, DueDate, ReturnDate) 
            VALUES (%s, %s, %s, %s, NULL)
            """
            values = (book_id, member_id, issue_date, due_date)
            cursor.execute(query, values)
            print("databse connected here")
            db.commit()

            messagebox.showinfo("Success", "Book borrowed successfully!")
            load_books()
            borrow_window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"An error occurred: {str(err)}")

    
    borrow_button = tk.Button(FormFrame, text="Borrow Book", font=("Arial", 14), bg="darkblue", fg="white", command=confirm_borrow)
    borrow_button.grid(row=2, column=0, columnspan=2, pady=20)

    
    FormFrame.grid_rowconfigure(0, weight=1)
    FormFrame.grid_rowconfigure(1, weight=1)
    FormFrame.grid_rowconfigure(2, weight=1)  

    FormFrame.grid_columnconfigure(0, weight=1)
    FormFrame.grid_columnconfigure(1, weight=2)

    
    FormFrame.place(relx=0.5, rely=0.5, anchor="center")


# return book code
def return_book():
    # Create a new window for returning books
    return_window = tk.Toplevel()
    return_window.title("Return Book")
    return_window.geometry("600x400") 
    return_window.configure(bg="orange") 

    # Title label
    tk.Label(return_window, text="RETURN BOOK", font=("Arial", 20, "bold"), bg="brown", fg="white", pady=10).pack(fill=tk.X)

    # Frame for form fields
    FormFrame = tk.Frame(return_window, bg="orange")
    FormFrame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Labels and entry fields for return details
    tk.Label(FormFrame, text="Transaction ID", font=("Arial", 12), bg="orange").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    transaction_id_entry = tk.Entry(FormFrame, width=30)
    transaction_id_entry.grid(row=0, column=1, padx=10, pady=10)

    # Function to confirm return
    def confirm_return():
        # Retrieve inputs
        transaction_id = transaction_id_entry.get().strip()
        return_date = datetime.now().date()

        if not transaction_id:
            messagebox.showerror("Error", "Please enter Transaction ID.")
            return

        try:
            cursor.execute("SELECT ReturnDate, DueDate, BookID FROM Transactions WHERE TransactionID = %s", (transaction_id,))
            transaction = cursor.fetchone()

            if not transaction:
                messagebox.showerror("Error", "Transaction not found.")
                return

            if transaction[0] is not None:
                messagebox.showinfo("Info", "Book already returned.")
                return

            # Calculate Fine if the return date is after the due date
            fine = 0
            if return_date > transaction[1]:  # Check if the return date is after the due date
                days_overdue = (return_date - transaction[1]).days
                fine = days_overdue * 10  # Assume fine is 10 per day

            # Update the Transactions table
            cursor.execute("""
                UPDATE Transactions 
                SET ReturnDate = %s, Fine = %s
                WHERE TransactionID = %s
                """, (return_date, fine, transaction_id))

            db.commit()

            messagebox.showinfo("Success", "Book returned successfully!")
            load_books()
            return_window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"An error occurred: {str(err)}")

    # Return button (Centered and in the next row)
    return_button = tk.Button(FormFrame, text="Return Book", font=("Arial", 14), bg="darkblue", fg="white", command=confirm_return)
    return_button.grid(row=1, column=0, columnspan=2, pady=20)

    # Centering the form
    FormFrame.grid_rowconfigure(0, weight=1)
    FormFrame.grid_rowconfigure(1, weight=1)  # Row for the button

    FormFrame.grid_columnconfigure(0, weight=1)
    FormFrame.grid_columnconfigure(1, weight=2)

    # Ensure the content is centered in the form frame
    FormFrame.place(relx=0.5, rely=0.5, anchor="center")

def update_member():
    # Create a new window for updating members
    update_window = tk.Toplevel()
    update_window.title("Update Member")
    update_window.geometry("600x500")  # Adjusted size for better fit
    update_window.configure(bg="lightgray")  # Updated theme

    # Title label
    tk.Label(update_window, text="UPDATE MEMBER", font=("Arial", 20, "bold"), bg="black", fg="white", pady=10).pack(fill=tk.X)

    # Frame for form fields
    TableFrame = tk.Frame(update_window, bg="lightgray")
    TableFrame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    # Labels and entry fields for member details
    tk.Label(TableFrame, text="Member ID", font=("Arial", 12), bg="lightgray").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    update_member_id = tk.Entry(TableFrame, width=30)
    update_member_id.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Member Name", font=("Arial", 12), bg="lightgray").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    update_member_name = tk.Entry(TableFrame, width=30)
    update_member_name.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Email ID", font=("Arial", 12), bg="lightgray").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    update_member_email = tk.Entry(TableFrame, width=30)
    update_member_email.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Phone Number", font=("Arial", 12), bg="lightgray").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    update_member_phone = tk.Entry(TableFrame, width=30)
    update_member_phone.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(TableFrame, text="Membership Date", font=("Arial", 12), bg="lightgray").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    update_membership_date = tk.Entry(TableFrame, width=30)
    update_membership_date.grid(row=4, column=1, padx=10, pady=10)

    # Function to perform the update
    def perform_update():
        member_id = update_member_id.get().strip()
        member_name = update_member_name.get().strip()
        member_email = update_member_email.get().strip()
        member_phone = update_member_phone.get().strip()
        membership_date = update_membership_date.get().strip()

        if not all([member_id, member_name, member_email, member_phone, membership_date]):
            messagebox.showerror("Error", "Please fill all the fields.")
            return

        # Validate Phone Number (must be an integer and exactly 11 digits)
        if not update_member_phone.get().isdigit() or len(update_member_phone.get()) != 11:
            messagebox.showerror("Error", "Phone Number must be an integer with exactly 11 digits.")
            return

        # Validate Email (must contain "@")
        if "@" not in update_member_email.get():
            messagebox.showerror("Error", "Email must contain '@'.")
            return

        try:
            # Check if the member exists
            cursor.execute("SELECT MemberID FROM Members WHERE MemberID = %s", (member_id,))
            member = cursor.fetchone()

            if not member:
                messagebox.showerror("Error", "Member not found. Please enter a valid Member ID.")
                return

            # Perform the update
            query = """UPDATE Members 
                    SET Name = %s, Email = %s, PhoneNumber = %s, MembershipDate = %s 
                    WHERE MemberID = %s"""
            cursor.execute(query, (member_name, member_email, member_phone, membership_date, member_id))
            db.commit()

            messagebox.showinfo("Success", "Member details updated successfully.")
            update_window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Update button (Centered and in the next row)
    update_button = tk.Button(TableFrame, text="Update Member", font=("Arial", 14), bg="darkblue", fg="white", command=perform_update)
    update_button.grid(row=5, column=0, columnspan=2, pady=20)

    # Centering the form
    TableFrame.grid_rowconfigure(0, weight=1)
    TableFrame.grid_rowconfigure(1, weight=1)
    TableFrame.grid_rowconfigure(2, weight=1)
    TableFrame.grid_rowconfigure(3, weight=1)
    TableFrame.grid_rowconfigure(4, weight=1)
    TableFrame.grid_rowconfigure(5, weight=1)  # Row for the button

    TableFrame.grid_columnconfigure(0, weight=1)
    TableFrame.grid_columnconfigure(1, weight=2)

    # Ensure the content is centered in the form frame
    TableFrame.place(relx=0.5, rely=0.5, anchor="center")

    update_window.mainloop()


# Search book code 
def search_book():

    def SearchBook():
        SearchField = search_var.get()
        SearchValue = SearchTextbox.get()

        if not SearchValue:
            messagebox.showerror("Error", "Please enter a value to search.")
            return

        try:

            if SearchField == "BookID":
                query = "SELECT * FROM Books WHERE BookID = %s"
                cursor.execute(query,(SearchValue,))
            else:
                # Query to search the database for other fields
                query = f"SELECT * FROM Books WHERE {SearchField} LIKE %s"
                cursor.execute(query, ('%' + SearchValue + '%',))

            # Clear the previous data in the table
            for row in booktable.get_children():
                booktable.delete(row)


            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    booktable.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("No Results", "No books found matching the search criteria.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    SearchWindow = tk.Toplevel()
    SearchWindow.title("Search Book")
    SearchWindow.geometry("900x600")
    SearchWindow.configure(bg="lightgray")

    TitleLabel = tk.Label(
        SearchWindow, text="SEARCH BOOK", font=("Arial", 20, "bold"), bg="darkblue", fg="white", pady=10
    )
    TitleLabel.pack(fill=tk.X)


    InputFrame = tk.Frame(SearchWindow, bg="lightgray")
    InputFrame.pack(pady=20, padx=20, fill=tk.X)

    
    tk.Label(InputFrame, text="Search By:", font=("Arial", 14), bg="lightgray").grid(row=0, column=0, padx=10, pady=5)
    search_var = tk.StringVar()
    options = ["BookID", "Title", "Author", "Publisher"]
    dropdown = ttk.Combobox(InputFrame, textvariable=search_var, values=options, state="readonly")
    dropdown.grid(row=0, column=1, padx=10, pady=5)
    search_var.set("BookID")


    tk.Label(InputFrame, text="Enter Value:", font=("Arial", 14), bg="lightgray").grid(row=0, column=2, padx=10, pady=5)
    SearchTextbox = tk.Entry(InputFrame, font=("Arial", 14))
    SearchTextbox.grid(row=0, column=3, padx=10, pady=5)


    SearchButton = tk.Button(
        InputFrame, text="Search", font=("Arial", 14), bg="darkblue", fg="white", command=SearchBook
    )
    SearchButton.grid(row=0, column=4, padx=10, pady=5)


    TableFrame = tk.Frame(SearchWindow, bg="lightgray")
    TableFrame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)


    style = ttk.Style()
    style.theme_use("default")


    style.configure(
    "Treeview.Heading",
    background="darkblue",  
    foreground="white",     
    font=("Arial", 12, "bold") 
)


    
    booktable = ttk.Treeview(
        TableFrame,
        columns=("BookID", "Title", "Author", "Publisher", "Quantity"),
        show="headings",
        style="Treeview"  
    )
    booktable.pack(fill=tk.BOTH, expand=True)


    for col in ("BookID", "Title", "Author", "Publisher", "Quantity"):
        booktable.heading(col, text=col)
        booktable.column(col, anchor=tk.CENTER, width=150 )


    scrollbar_y = ttk.Scrollbar(TableFrame, orient=tk.VERTICAL, command=booktable.yview)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x = ttk.Scrollbar(TableFrame, orient=tk.HORIZONTAL, command=booktable.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    booktable.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    
def search_member():
    def fetch_data():
        member_id = member_id_entry.get().strip()
        if not member_id:
            messagebox.showwarning("Input Error", "Please enter a Member ID.")
            return
        
        try:

            cursor = db.cursor()

            query = """
                SELECT m.MemberID, m.Name, 
                t.BookID, t.IssueDate, t.DueDate, t.ReturnDate, t.Fine
                FROM Members m
                LEFT JOIN Transactions t ON m.MemberID = t.MemberID
                WHERE m.MemberID = %s
            """
            cursor.execute(query, (member_id,))
            results = cursor.fetchall()

            
            for row in booktable.get_children():
                booktable.delete(row)

            
            if results:
                for row in results:
                    booktable.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("No Results", "No matching records found.")

            
            cursor.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
    
    
    SearchWindow = tk.Toplevel()
    SearchWindow.title("Search Members")
    SearchWindow.geometry("900x600")
    SearchWindow.configure(bg="lightgray")

    
    title_label = tk.Label(SearchWindow, text="Search Member's Transaction Record", font=("Arial", 18, "bold"), bg="darkblue", fg="white")
    title_label.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")

    
    member_id_label = tk.Label(SearchWindow, text="Enter Member ID:", font=("Arial", 14), bg="lightgray")
    member_id_entry = tk.Entry(SearchWindow, font=("Arial", 14))
    search_button = tk.Button(SearchWindow, text="Search", font=("Arial", 14), command=fetch_data , bg="darkblue", fg="white")


    member_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    member_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    search_button.grid(row=1, column=2, padx=10, pady=10)

    
    SearchWindow.grid_columnconfigure(0, weight=1)
    SearchWindow.grid_columnconfigure(1, weight=2)
    SearchWindow.grid_columnconfigure(2, weight=1)

    
    SearchWindow.grid_rowconfigure(0, weight=0)
    SearchWindow.grid_rowconfigure(1, weight=1)


    TableFrame = tk.Frame(SearchWindow, bg="lightgray")
    TableFrame.grid(row=2, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")

    
    style = ttk.Style()
    style.theme_use("default")
    style.configure(
        "Treeview.Heading",
        background="darkblue",
        foreground="white",
        font=("Arial", 12, "bold")
    )
    style.configure("Treeview", font=("Arial", 10))


    booktable = ttk.Treeview(
    TableFrame,
    columns=("MemberID", "Name", "BookID", "IssueDate", "DueDate", "ReturnDate", "Fine"),
    show="headings",
    style="Treeview"
)


    booktable.grid(row=0, column=0, sticky="nsew")


    scrollbar = tk.Scrollbar(TableFrame, orient=tk.VERTICAL, command=booktable.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")


    booktable.configure(yscrollcommand=scrollbar.set)


    TableFrame.grid_rowconfigure(0, weight=1)
    TableFrame.grid_columnconfigure(0, weight=1)
    TableFrame.grid_columnconfigure(1, weight=0)



    for col in ("MemberID", "Name", "BookID", "IssueDate", "DueDate", "ReturnDate", "Fine"):
        booktable.heading(col, text=col)
        booktable.column(col, anchor=tk.CENTER, width=120)


    SearchWindow.grid_rowconfigure(2, weight=1)
    SearchWindow.grid_columnconfigure(0, weight=1)

# function for transaction button 
def view_transactions():

    ViewTransactionsWindow = tk.Toplevel()
    ViewTransactionsWindow.title("Transactions")
    ViewTransactionsWindow.geometry("700x500")  # Adjust the size as needed

    TitleLabel = tk.Label(ViewTransactionsWindow, text="Transactions", font=("Arial", 20, "bold"), bg="lightgreen", fg="black", padx=10, pady=5)
    TitleLabel.pack(fill=tk.X)

    style = ttk.Style()
    style.theme_use("default")

    
    style.configure(
        "Treeview.Heading",
        background="green",  
        foreground="white",   
        font=("Arial", 12, "bold")  
    )

    
    TransactionFrame = tk.Frame(ViewTransactionsWindow, bd=4, relief=tk.RIDGE, bg="lightgreen")
    TransactionFrame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    
    TransactionTable = ttk.Treeview(TransactionFrame, columns=("TransactionID", "BookID", "MemberID", "IssueDate", "ReturnDate", "DueDate", "Fine"), show="headings", style="Treeview")
    TransactionTable.pack(fill=tk.BOTH, expand=True)

    
    for col in ("TransactionID", "BookID", "MemberID", "IssueDate", "ReturnDate", "DueDate", "Fine"):
        TransactionTable.heading(col, text=col)
        TransactionTable.column(col, width=100, anchor=tk.CENTER)

    
    cursor.execute("SELECT * FROM Transactions")
    TransactionTable.delete(*TransactionTable.get_children())  # Clear existing rows
    for row in cursor.fetchall():
        TransactionTable.insert("", tk.END, values=row)

#main
login_window.mainloop()
    
    
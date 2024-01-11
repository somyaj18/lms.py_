import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from tkinter.ttk import Treeview

global e1, e2, e3, e4, frame1, frame2, count
global labelFrame
global frame4
mydb = pymysql.connect(host="localhost", port=3307, user="root", password="", database='ad_db')
print(mydb)
my_cursor = mydb.cursor()
#my_cursor.execute("ALTER TABLE admin_info DROP column STATUS")

'''sql="INSERT INTO admin_info (ADMIN_ID,NAME,PASSWORD,DEPARTMENT_NAME) values (%s,%s,%s,%s)"
data=("111","ram","1234","IT")
my_cursor.execute(sql,data)
mydb.commit()
print(my_cursor.rowcount)'''


# my_cursor.execute('select *from admin_info')
# my_result=my_cursor.fetchall()
# for x in my_result:
#   print(x)


def st_site():
    global fr
    frame1.destroy()
    fr = Frame(win, bg='sky blue', bd=1)
    fr.pack(expand=True, fill='both')
    label1 = Label(fr, text='WELCOME  STUDENT', font=50)
    label1.pack(pady=100)
    b3 = Button(fr, text='Register', font=10, command=student_site)
    b3.place(x=500, y=200)
    b4 = Button(fr, text='Login', font=10, command=student_login)
    b4.place(x=1000, y=200)

def student_site():
    frame1.destroy()
    global entry1, entry2, entry3, entry4, entry6, entry7
    global framest
    framest = Frame(win, bg='#77DD77', bd=2)
    framest.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.5)
    name = Label(framest, text='Name::')
    name.place(relx=0.05, rely=0.05)
    entry1 = Entry(framest)
    entry1.place(relx=0.3, rely=0.05, relwidth=0.62)

    contact_no = Label(framest, text="Contact No::")
    contact_no.place(relx=0.05, rely=0.2)
    entry2 = Entry(framest)
    entry2.place(relx=0.3, rely=0.2, relwidth=0.62)

    email_id = Label(framest, text="Password::")
    email_id.place(relx=0.05, rely=0.35)
    entry3 = Entry(framest, show='*')
    entry3.place(relx=0.3, rely=0.35, relwidth=0.62)

    course = Label(framest, text='Course::')
    course.place(relx=0.05, rely=0.5)
    entry4 = Entry(framest)
    entry4.place(relx=0.3, rely=0.5, relwidth=0.62)

    Enroll_no = Label(framest, text="Enrollment")
    Enroll_no.place(relx=0.05, rely=0.75)
    entry6 = Entry(framest)
    entry6.place(relx=0.3, rely=0.75, relwidth=0.62)
    b = tkinter.Button(framest, text='Submit', command=register)
    b.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    b2 = Button(framest, text='BACK', command=lambda: framest.destroy())
    b2.place(relx=0.50, rely=0.9, relwidth=0.18, relheight=0.08)


def register():
    mydb = pymysql.connect(host="localhost", port=3307, user="root", password="", database="st_db")
    print(mydb)
    name = entry1.get()
    contact = entry2.get()
    password = entry3.get()
    course = entry4.get()
    enroll = entry6.get()
    my_cursor = mydb.cursor()
    insert_query = "INSERT INTO student_info( NAME,CONTACT_NO,PASSWORD, COURSE,	ENROLL_NO ) VALUES (%s, %s,%s,%s,%s)"
    value = (name, contact, password, course, enroll)
    my_cursor.execute(insert_query, value)
    mydb.commit()
    my_cursor.execute("SELECT * FROM student_info")


'''def stu_login():
    reg = Label(win, text='You successfully registered,Please login').place(x=100, y=150)
    back = tkinter.Button(win, text='Back to login page', command=student_login).place(x=150, y=170)'''


def student_login():
    global e1, e4
    global framest2
    framest2 = Frame(win, bg='#D3DB55', bd=2)
    framest2.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.42)
    id = Label(framest2, text='Enrollment No ::')
    id.place(relx=0.05, rely=0.05)
    e1 = Entry(framest2)
    e1.place(relx=0.3, rely=0.05, relwidth=0.62)
    password = Label(framest2, text='Password ::')
    password.place(relx=0.05, rely=0.35)
    e4 = Entry(framest2, show='*')
    e4.place(relx=0.3, rely=0.35, relwidth=0.62)
    log = tkinter.Button(framest2, text='Log in', command=fetch_student_login)
    log.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    '''b = Button(framest2, text='BACK', command=lambda:framest2.destroy())
    b.place(relx=0.50, rely=0.9, relwidth=0.18, relheight=0.08)'''


def fetch_student_login():
    mydb = pymysql.connect(host='localhost', port=3307, user="root", password="", database='st_db')
    print(mydb)
    getno = 0
    getPswd = 0
    enroll = e1.get()
    login_pass = e4.get()
    my_cursor = mydb.cursor()
    print(enroll)
    print(login_pass)
    my_cursor.execute("select ENROLL_NO,PASSWORD from student_info where ENROLL_NO= %s", (enroll,))
    for i in my_cursor:
        getno = i[0]
        getPswd = i[1]
        print(getno)

    if enroll == str(getno) and login_pass == str(getPswd):
        # messagebox.showinfo('Successfully login! BY' + getno + "And" + getPswd)
        print("success")
        entry()
    else:
        print("kuch nhi hua")


def entry():
    global frameentry
    framest2.destroy()
    global search_box
    global stwin
    stwin = Tk()
    stwin.title('Student Site')
    frameentry=Frame(stwin,bg='#C6C650',bd=1)
    frameentry.pack(expand=True,fill='both')
    search_box = Entry(frameentry)
    search_box.place(x=900, y=30)
    b7 = ttk.Button(frameentry, text='Search', command=search_option2)
    b7.place(x=800, y=30)
    b = ttk.Button(frameentry, text='Available books',  command=show_table)
    b.place(relx=0.1,rely=0.15,relwidth=0.16, relheight=0.06)
    b2 = ttk.Button(frameentry, text='Request books', command=student_request_book)
    b2.place(relx=0.4,rely=0.15,relwidth=0.16, relheight=0.06)
    '''
    b4 = ttk.Button(win, text='Issued books')
    b4.place(x=380, y=100)
    b5 = ttk.Button(win, text='Help')
    b5.place(x=540, y=100)
    b6 = ttk.Button(win, text='Review')
    b6.place(x=650, y=100)
    '''


def search_option2():
    box = search_box.get()
    print(box)
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT *from  available_books WHERE BOOK_ID=%s", (box,))
    result = my_cursor.fetchall()
    frame_search2 = Frame(frameentry, bg='#BC2276', bd=1)
    frame_search2.place(relx=0.6, rely=0.44, relwidth=0.3, relheight=0.42)
    b = Button(frame_search2, text='BACK', command=lambda: frame_search2.destroy())
    b.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    l = Label(frame_search2, text=" ")
    l.place(relx=0.08, rely=0.35)
    print(result)
    if result:
        for i in result:
            book_id = i[0]
            title = i[1]
            author= i[2]
            status= i[3]
        l.config(text="")
        l.config(text=f"Book ID : {book_id}\n"
                      f"Title : {title}\n"
                      f"Author : {author}\n"
                      f"Status : {status}")
    else:
        l.config(text="Book not found in available_books.")


def student_request_book():
    global en1
    framest4 = Frame(frameentry, bg='#cc9900', bd=1)
    framest4.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.38)
    lb = Label(framest4, text="BOOK ID : ", bg='#044F67', fg='white')
    lb.place(relx=0.05, rely=0.05)
    en1 = Entry(framest4)
    en1.place(relx=0.3, rely=0.05, relwidth=0.62)
    SubmitBtn = Button(framest4, text="SUBMIT", bg='#264348', fg='white', command=fetch_request_book)
    SubmitBtn.place(relx=0.35, rely=0.6, relwidth=0.18, relheight=0.08)
    b = Button(framest4, text='BACK', bg='#264348', fg='white', command=lambda: framest4.destroy())
    b.place(relx=0.35, rely=0.9, relwidth=0.18, relheight=0.08)

def fetch_request_book():
    id = en1.get()
    my_cursor = mydb.cursor()
    #my_cursor.execute("INSERT INTO request_book (BOOK_ID) values (%s)", (id,))
    #mydb.commit()
    my_cursor.execute("SELECT *from  available_books WHERE BOOK_ID=%s", (id,))
    result = my_cursor.fetchall()

    if result:
        for i in result:
            book_id = i[0]
            print(book_id)
            title = i[1]
            print(title)
            author= i[2]
            print(author)
            status= i[3]
            print(status)
    my_cursor.execute("UPDATE available_books set STATUS='ISSUED' WHERE BOOK_ID=%s", (id,))
    mydb.commit()
    query = "INSERT INTO request_book (BOOK_ID,TITLE,AUTHOR,STATUS) VALUES (%s, %s, %s, %s)"
    value = (book_id,title, author,status)
    my_cursor.execute(query, value)
    mydb.commit()
    my_cursor.execute("SELECT * FROM request_book")

    all_request_books = my_cursor.fetchall()
    for row in all_request_books:
        print(row)



def show_table():
    global framest3
    framest3 = Frame(frameentry, bg='#ff6666', bd=1)
    framest3.pack(expand=True, fill='both')
    table = ttk.Treeview(framest3, column=('BOOK_ID', 'TITLE', 'AUTHOR', 'STATUS'), show='headings')
    table.heading('BOOK_ID', text='BOOK_ID')
    table.heading('TITLE', text='TITLE')
    table.heading('AUTHOR', text='AUTHOR')
    table.column('BOOK_ID', width=50)
    table.column('TITLE', width=150)
    table.column('AUTHOR', width=150)
    table.column('STATUS', width=50)
    my_cursor = mydb.cursor()
    my_cursor.execute("select *from  available_books")
    my_result = my_cursor.fetchall()
    for row in my_result:
        table.insert("", "end", values=row)
    back_button = tkinter.Button(framest3, text="Back", command=go_back)
    back_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    table.pack(expand=True, fill='both')


def go_back():
    framest3.destroy()
    entry()


'''def student_site2():
    student_site2_win = Tk()
    search_box = Entry(student_site2_win).place(x=900, y=30)
    b7 = tkinter.Button(student_site2_win, text='Search').place(x=830, y=30)
    b = tkinter.Button(student_site2_win, text='Available books')
    b.place(x=50, y=100)
    b2 = tkinter.Button(student_site2_win, text='New books')
    b2.place(x=230, y=100)
    b4 = tkinter.Button(student_site2_win, text='Issued books')
    b4.place(x=380, y=100)
    b5 = tkinter.Button(student_site2_win, text='Help')
    b5.place(x=540, y=100)
    b6 = tkinter.Button(student_site2_win, text='Review')
    b6.place(x=650, y=100)
    student_site2_win.mainloop()'''


def admin_site():
    global frame2
    frame1.destroy()
    frame2 = Frame(win, bg='sky blue', bd=1)
    frame2.pack(expand=True, fill='both')
    label1 = Label(frame2, text='WELCOME  ADMIN', font=50)
    label1.pack(pady=100)
    b3 = Button(frame2, text='Register', font=10, command=admin_site2)
    b3.place(x=500, y=200)
    b4 = Button(frame2, text='Login', font=10, command=login)
    b4.place(x=1000, y=200)


# def login_site_admin():


def admin_site2():
    global labelFrame
    global count
    count = 0
    count += 1

    if (count >= 2):
        labelFrame.destroy()

    global en1, en2, en3, en4, en5, en6

    labelFrame = Frame(frame2, bg='#044F67')
    labelFrame.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.42)

    # Employee ID
    lb1 = Label(labelFrame, text="Emp ID : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05, rely=0.05)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3, rely=0.05, relwidth=0.62)

    # Employee Name
    lb2 = Label(labelFrame, text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05, rely=0.2)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Employee Password
    lb3 = Label(labelFrame, text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05, rely=0.35)

    en3 = Entry(labelFrame, show='*')
    en3.place(relx=0.3, rely=0.35, relwidth=0.62)

    # Employee Department
    lb4 = Label(labelFrame, text="Department : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05, rely=0.5)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(labelFrame, text="SUBMIT", bg='#264348', fg='white', command=submit1)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    b = Button(labelFrame, text='BACK', bg='#264348', fg='white', command=lambda: labelFrame.destroy())
    b.place(relx=0.50, rely=0.9, relwidth=0.18, relheight=0.08)


def login():
    global frame4
    global count
    count = 0
    count += 1

    if count >= 2:
        frame4.destroy()

    global e1, e4
    frame4 = Frame(win, bg='pink', bd=1)
    frame4.pack(expand=True, fill='both')
    id = Label(frame4, text='Admin   ID ::')
    id.place(relx=0.05, rely=0.05)
    e1 = Entry(frame4)
    e1.place(relx=0.3, rely=0.05, relwidth=0.62)
    password = Label(frame4, text='Password ::')
    password.place(relx=0.05, rely=0.35)
    e4 = Entry(frame4, show='*')
    e4.place(relx=0.3, rely=0.35, relwidth=0.62)
    log = tkinter.Button(frame4, text='Log in', command=fetch_login_detail)
    log.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    b = Button(frame4, text='BACK', command=lambda: frame4.destroy())
    b.place(relx=0.50, rely=0.9, relwidth=0.18, relheight=0.08)


def fetch_login_detail():
    login_id = e1.get()
    login_pass = e4.get()
    my_cursor = mydb.cursor()
    my_cursor.execute("select ADMIN_ID,PASSWORD from admin_info where ADMIN_ID= " + login_id + "")
    for i in my_cursor:
        getID = i[0]
        getPswd = i[1]

    if (getID == login_id and getPswd == login_pass):
        # messagebox.showinfo('Successfully login! BY'+getID +"And"+ getPswd)
        admin_final_window()


def submit1():
    emp_id = en1.get()
    name = en2.get()
    password = en3.get()
    department_name = en4.get()
    print(emp_id)
    labelFrame.destroy()
    # frame = Frame(win, bg='#672d04', bd=1,fg='white')
    #  frame.pack(relx=0.29,rely=0.85,relwidth=0.58,relheight=0.78)

    my_cursor = mydb.cursor()
    insert_query = "INSERT INTO admin_info (ADMIN_ID, NAME, PASSWORD, DEPARTMENT_NAME) VALUES (%s, %s,%s,%s)"
    value = (emp_id, name, password, department_name)
    my_cursor.execute(insert_query, value)

    mydb.commit()
    my_cursor.execute("SELECT * FROM admin_info")
    # my_result=my_cursor.fetchall()


# for i in my_result:
#     print(i)
def after_submit():
    label2 = Label(win, font=12, text=' You  have  registerd  successfully , Please  Login', command=login)
    label2.place(x=300, y=800)
    '''Back_button =Button(win, text='BACK',font=10)
    Back_button.place(x=150, y=100)'''
def show_user():
    mydb2=pymysql.connect(host="localhost", port=3307, user="root", password="", database='st_db')
    print(mydb2)
    my_cursor=mydb2.cursor()
    my_cursor.execute("select *from student_info")
    my_result=my_cursor.fetchall()
    if my_result:
        for i in my_result:
            name=i[0]
            print(name)
            contact_no=i[1]
            print(contact_no)
            password=i[2]
            print(password)
            course=i[3]
            print(course)
            enroll_no=i[4]
            print(enroll_no)
    my_cursor2=mydb.cursor()
    '''query="INSERT INTO users(NAME,CONTACT_NO,PASSWORD,COURSE,ENROLL_NO)values(%s,%s,%s,%s,%s)"
    value=(name,contact_no,password,course,enroll_no)
    my_cursor2.execute(query,value)'''
    mydb.commit()
    my_cursor2.execute("SELECT * FROM users")
    show=my_cursor2.fetchall()
    for i in show:
        print(i)

    frameuser=Frame(frame6,bg='#5A4641',bd=1)
    frameuser.pack(expand=True,fill='both')
    table = ttk.Treeview(frameuser, column=('NAME','CONTACT_NO', 'PASSWORD', 'COURSE','ENROLL_NO'), show='headings')
    table.heading('NAME', text='NAME')
    table.heading('CONTACT_NO', text='CONTACT_NO')
    table.heading('PASSWORD', text='PASSWORD')
    table.heading('COURSE', text='COURSE')
    table.heading('ENROLL_NO', text='ENROLL_NO')
    table.column('NAME', width=50)
    table.column('CONTACT_NO', width=100)
    table.column('PASSWORD', width=100)
    table.column('COURSE', width=50)
    table.column('ENROLL_NO', width=50)
    for row in show:
        table.insert("", "end", values=row)
    back_button = Button(frameuser, text="Back", command=lambda:frameuser.destroy())
    back_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    table.pack(expand=True, fill='both')
def admin_final_window():
    global admin_win
    admin_win = Tk()
    global frame6
    global search_box
    frame6 = Frame(admin_win, bg='#ff9933', bd=1)
    frame6.pack(expand=True, fill='both')
    search_box = Entry(frame6)
    search_box.place(x=900, y=30)
    b7 = tkinter.Button(frame6, text='Search', command=search_option)
    b7.place(x=830, y=30)
    b = tkinter.Button(frame6, text='Available books', command=admin_available_books)
    b.place(x=50, y=100)
    b2 = tkinter.Button(frame6, text='Add books', command=add_book_form)
    b2.place(x=200, y=100)
    b3 = tkinter.Button(frame6, text='Users',command=show_user)
    b3.place(x=350, y=100)
    b4 = tkinter.Button(frame6, text='Requesting books',command=see_request_book)
    b4.place(x=500, y=100)
    '''b5 = tkinter.Button(win, text='Requesting books')
    b5.place(x=630, y=100)
    b6 = tkinter.Button(win, text='Users')
    b6.place(x=780, y=100)'''
def see_request_book():
    my_cursor=mydb.cursor()
    my_cursor.execute("SELECT *from request_book")
    my_result=my_cursor.fetchall()

    framebook = Frame(frame6, bg='#5A4641', bd=1)
    framebook.pack(expand=True, fill='both')
    table = ttk.Treeview(framebook, column=('BOOK_ID', 'TITLE', 'AUTHOR', 'STATUS'), show='headings')
    table.heading('BOOK_ID', text='BOOK_ID')
    table.heading('TITLE', text='TITLE')
    table.heading('AUTHOR', text='AUTHOR')
    table.heading('STATUS', text='STATUS')
    table.column('BOOK_ID', width=50)
    table.column('TITLE', width=150)
    table.column('AUTHOR', width=150)
    table.column('STATUS', width=50)
    for row in my_result:
        table.insert("", "end", values=row)
    back_button = Button(framebook, text="Back", command=lambda: framebook.destroy())
    back_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    table.pack(expand=True, fill='both')
#def change_status():

def add_book_form():
    global frame7
    global ent1, ent2, ent3
    global ent4
    frame7 = Frame(admin_win, bg='#cc66ff', bd=2)
    frame7.pack(expand=True, fill='both')
    l1 = Label(frame7, text='Book_Id ::')
    l1.place(relx=0.05, rely=0.05)
    ent1 = Entry(frame7)
    ent1.place(relx=0.3, rely=0.05, relwidth=0.62)
    l2 = Label(frame7, text='Book_Name ::')
    l2.place(relx=0.05, rely=0.2)
    ent2 = Entry(frame7)
    ent2.place(relx=0.3, rely=0.2, relwidth=0.62)
    l3 = Label(frame7, text='Author ::')
    l3.place(relx=0.05, rely=0.35)
    ent3 = Entry(frame7)

    ent3.place(relx=0.3, rely=0.35, relwidth=0.62)
    l4 = Label(frame7, text='Status ::')
    l4.place(relx=0.05, rely=0.5)
    ent4 = Entry(frame7)
    ent4.place(relx=0.3, rely=0.5, relwidth=0.62)
    # status_var = tkinter.StringVar()

    '''button3 = Radiobutton(frame7, text='Available', variable=status_var, value='Available')
    button3.place(relx=0.3, rely=0.5)
    button4 = Radiobutton(frame7, text='Issued', variable=status_var, value='Issued')
    button4.place(relx=0.45, rely=0.5)'''

    button = tkinter.Button(frame7, text='ADD', command=connect_newbook)
    button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    button2 = tkinter.Button(frame7, text='BACK', command=go3_back)
    button2.place(relx=0.50, rely=0.9, relwidth=0.18, relheight=0.08)


def connect_newbook():
    # mydb2 = pymysql.connect(host="localhost", port=3307, user="root", password="", database='st_db')
    # mydb = pymysql.connect(host="localhost", port=3307, user="root", password="", database='addbook')
    # print(mydb)
    #  print(mydb2)
    my_cursor = mydb.cursor()
    book_id = ent1.get()
    book_name = ent2.get()
    book_author = ent3.get()
    book_status = ent4.get()
    print(book_id)
    print(book_author)
    print(book_name)
    print(book_status)
    #  my_cursor.execute("ALTER TABLE available_books ADD COLUMN STATUS varchar(50) ")
    query = "INSERT INTO available_books (BOOK_ID, TITLE, AUTHOR,STATUS) values (%s,%s,%s,%s)"
    value = (book_id, book_name, book_author, book_status)
    my_cursor.execute(query, value)
    mydb.commit()
    my_cursor.execute("select *from available_books")
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x)


def search_option():
    box = search_box.get()
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT *from  available_books WHERE BOOK_ID=%s", (box,))
    result = my_cursor.fetchone()
    frame_search = Frame(frame6, bg='#BC2276', bd=1)
    frame_search.place(relx=0.6, rely=0.44, relwidth=0.3, relheight=0.42)
    b = Button(frame_search, text='BACK', command=lambda: frame_search.destroy())
    b.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    l = Label(frame_search, text='')
    l.place(relx=0.08, rely=0.35)
    if result:
        book_id = result[0]
        title = result[1]
        author = result[2]
        status = result[3]
        l.config(text="")
        l.config(text=f"Book ID : {book_id}\n"
                      f"Title : {title}\n"
                      f"Author : {author}\n"
                      f"Status : {status}")
    else:
        l.config(text="Book not found in available_books.")


def go3_back():
    frame7.destroy()


def admin_available_books():
    global frame5
    frame5 = Frame(frame6, bg='#99ff66', bd=2)
    frame5.pack(expand=True, fill='both')
    my_cursor = mydb.cursor()
    my_cursor.execute("select *from  available_books")
    my_result = my_cursor.fetchall()
    table = ttk.Treeview(frame6, column=('BOOK_ID', 'TITLE', 'AUTHOR', 'STATUS'), show='headings')
    table.heading('BOOK_ID', text='BOOK_ID')
    table.heading('TITLE', text='TITLE')
    table.heading('AUTHOR', text='AUTHOR')
    table.heading('STATUS',text='STATUS')
    table.column('BOOK_ID', width=50)
    table.column('TITLE', width=150)
    table.column('AUTHOR', width=150)
    table.column('STATUS', width=50)
    for row in my_result:
        table.insert("", "end", values=row)
    back_button = Button(frame5, text="Back", command=admin_final_window)
    back_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    table.pack(expand=True, fill='both')


def go2_back():
    frame5.destroy()

    admin_final_window()


win = Tk()
win.title('Library  Management')
frame1 = tkinter.Frame(win, bg='#E12458', bd=1)
frame1.pack(expand=True, fill='both')
label1 = Label(frame1, text="WELCOME  TO  SOMYA'S LIBRARY", font=300).place(x=590, y=150)
b1 = tkinter.Button(frame1, text='Admin', font=50, command=admin_site).place(relx=0.4,rely=0.4,relwidth=0.18, relheight=0.08)
b2 = tkinter.Button(frame1, text='Student', font=50, command=st_site).place(relx=0.4,rely=0.55,relwidth=0.18, relheight=0.08)

#canvas = tkinter.Canvas(frame1, bg='sky blue', width=800, height=400)
#canvas.pack()
#img = Image.open(r'C:\Users\Dell\library2.png')
#canvas.update()
#canvas_width = canvas.winfo_width()
#canvas_height = canvas.winfo_height()
#resized_image = img.resize((canvas_width, canvas_height))
#tk_image = ImageTk.PhotoImage(resized_image)
#canvas.create_image(50, 50, anchor='nw', image=tk_image)

win.mainloop()

from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk
from tkinter import messagebox


class Student():
    def __init__(self, root):

        self.root = root
        self.root.title("DBMS_PROJECT")
        self.root.geometry("1305x800+100+10")
        self.root.maxsize(1305, 800)

        self.image=Image.open("wp3194549.jpg")
        self.photo=ImageTk.PhotoImage(self.image)
        lebel=Label(image=self.photo)
        lebel.place(x=0,y=0)


        title = Label(self.root, text="***** Student Management System *****", font=("comic sans", 25, "bold"),
                      bg="grey25",
                      fg="white", bd="6", relief=GROOVE)
        title.pack(side=TOP, fill=X)



        # ===================All variables=====================

        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        # self.address_var = StringVar()
        self.DOB_var = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()
        self.Year_var = StringVar()
        self.Branch_var = StringVar()

        # ================manage_frame=================

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="grey25")
        Manage_Frame.place(x=10, y=60, width=1285, height=260)

        m_title = Label(Manage_Frame, text="* Manage Students Here * ", font=("comic sans", 18, "bold"),
                        bg="aquamarine",
                        fg="grey25")
        m_title.grid(row=0, columnspan=6, pady=10, padx=40)

        lbl_roll = Label(Manage_Frame, text="Roll_No:-", font=("comic sans", 15, "bold"), bg="grey25", fg="white")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Manage_Frame,bg="white", textvariable=self.Roll_No_var, font=("comic sans", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name:-", font=("comic sans", 15, "bold"), bg="grey25", fg="white")
        lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,bg="white", textvariable=self.Name_var, font=("comic sans", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", font=("comic sans", 15, "bold"), bg="grey25", fg="white")
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame,bg="white", textvariable=self.Email_var, font=("comic sans", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender:-", font=("comic sans", 15, "bold"), bg="grey25", fg="white")
        lbl_Gender.grid(row=1, column=2, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("comic sans", 13, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=1, column=3, padx=20, pady=10)

        lbl_year = Label(Manage_Frame, text="Year_of_study:-", font=("comic sans", 15, "bold"), bg="grey25",
                         fg="white")
        lbl_year.grid(row=2, column=2, pady=10, padx=20, sticky="w")

        combo_year = ttk.Combobox(Manage_Frame, textvariable=self.Year_var, font=("comic sans", 13, "bold"),
                                  state='readonly')
        combo_year['values'] = ("1st_Year", "2nd_Year", "3rd_Year", "4th_Year")
        combo_year.grid(row=2, column=3, padx=20, pady=10)

        lbl_branch = Label(Manage_Frame, text="Select_Branch:-", font=("comic sans", 15, "bold"), bg="grey25",
                           fg="white")
        lbl_branch.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        combo_branch = ttk.Combobox(Manage_Frame, textvariable=self.Branch_var, font=("comic sans", 13, "bold"),
                                    state='readonly')
        combo_branch['values'] = ("MECH", "CSE", "CIVIL", "IT", "EXTC")
        combo_branch.grid(row=3, column=3, padx=20, pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact:-", font=("comic sans", 15, "bold"), bg="grey25",
                            fg="white")
        lbl_Contact.grid(row=1, column=4, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame,bg="white", textvariable=self.Contact_var, font=("comic sans", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=1, column=5, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B:-", font=("comic sans", 15, "bold"), bg="grey25", fg="white")
        lbl_DOB.grid(row=2, column=4, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, bg="white",textvariable=self.DOB_var, font=("comic sans", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_DOB.grid(row=2, column=5, pady=10, padx=20, sticky="w")






        lbl_Address = Label(Manage_Frame, text="Address:-", font=("comic sans", 15, "bold"), bg="grey25",
                            fg="white")
        lbl_Address.grid(row=3, column=4, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame,bg="white", width=19, height=3)
        self.txt_Address.grid(row=3, column=5, pady=10, padx=20, sticky="w")

        # ================Button_frame=================

        btn_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="grey25")
        btn_Frame.place(x=10, y=320, width=1285)

        Add_btn = Button(btn_Frame,bg="aquamarine", text="Add", width=18, command=self.add_students).grid(row=0, column=0, padx=32,
                                                                                          pady=10)
        Update_btn = Button(btn_Frame,bg="aquamarine", text="Update", width=18,command=self.update_data).grid(row=0, column=1, padx=32,
                                                                     pady=10)
        Delete_btn = Button(btn_Frame,bg="aquamarine", text="Delete", width=18,command=self.delete_data).grid(row=0, column=2, padx=32,
                                                                     pady=10)
        Clear_btn = Button(btn_Frame, bg="aquamarine",text="Clear", width=18,command=self.clear).grid(row=0, column=3, padx=32,
                                                                   pady=10)
        Search_btn = Button(btn_Frame,bg="aquamarine", text="Search", width=18,command=self.search_data).grid(row=0, column=4, padx=32, pady=10)

        # ==================tableframe================================

        Table_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="grey25")
        Table_Frame.place(x=10, y=400, width=1283, height=400)

        Scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        Scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,
                                          columns=(
                                              "roll", "name", "email", "gender", "contact", "dob", "year", "branch",
                                              "address"),
                                          xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.Student_table.xview)
        Scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll_No")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("year", text="Year")
        self.Student_table.heading("branch", text="Branch")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=150)
        self.Student_table.column("email", width=150)
        self.Student_table.column("gender", width=150)
        self.Student_table.column("contact", width=150)
        self.Student_table.column("dob", width=150)
        self.Student_table.column("year", width=150)
        self.Student_table.column("branch", width=150)
        self.Student_table.column("address", width=250)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()  # when program is run it initially fetches data in tye database and displays in the frame

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.Name_var=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.Year_var.get()=="" or self.Branch_var.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="Satpute@223", database="stm")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                                    self.Name_var.get(),
                                                                                    self.Email_var.get(),
                                                                                    self.Gender_var.get(),
                                                                                    self.Contact_var.get(),
                                                                                    self.DOB_var.get(),
                                                                                    self.Year_var.get(),
                                                                                    self.Branch_var.get(),
                                                                                    self.txt_Address.get('1.0', END)
                                                                                    ))
            con.commit()
            self.fetch_data()  # when entry is added it fetches the data present in the database at that time
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")



    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="Satpute@223", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)

            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.Year_var.set("")
        self.Branch_var.set("")
        self.txt_Address.delete('1.0', END)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.Year_var.set(row[6])
        self.Branch_var.set(row[7])
        self.txt_Address.delete('1.0', END)
        self.txt_Address.insert(END, row[8])

    def update_data(self):
        if self.Roll_No_var.get()=="" or self.Name_var=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.Year_var.get()=="" or self.Branch_var.get()=="":
            messagebox.showerror("Error","All fields are required to update!!!")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="Satpute@223", database="stm")
            cur = con.cursor()
            cur.execute(
                "update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,year=%s,branch=%s,address=%s where roll_no=%s",
                (self.Name_var.get(),
                 self.Email_var.get(),
                 self.Gender_var.get(),
                 self.Contact_var.get(),
                 self.DOB_var.get(),
                 self.Year_var.get(),
                 self.Branch_var.get(),
                 self.txt_Address.get('1.0', END),
                 self.Roll_No_var.get()
                 ))
            con.commit()
            self.fetch_data()  # when entry is added it fetches the data present in the database at that time
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been updated.")



    def delete_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="Satpute@223", database="stm")
        cur = con.cursor()

        cur.execute("DELETE FROM students WHERE Roll_No=" + str(self.Roll_No_var.get()))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Record has been Deleted.")

    def search_data(self):
        # if self.Roll_No_var.get()=="":
        #     messagebox.showerror("Error", "Enter roll_no to search in!!!")
        if self.Name_var.get() == "":
              messagebox.showerror("Error", "Enter Name to search in!!!")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="Satpute@223", database="stm")
            cur = con.cursor()
            cur.execute("select * from students where Roll_No=" + str(self.Roll_No_var.get()))

            # cur.execute("select * from students where name={0}".format(str(self.Name_var.get())))
            row = cur.fetchone()

            self.Roll_No_var.set(row[0])
            self.Name_var.set(row[1])
            self.Email_var.set(row[2])
            self.Gender_var.set(row[3])
            self.Contact_var.set(row[4])
            self.DOB_var.set(row[5])
            self.Year_var.set(row[6])
            self.Branch_var.set(row[7])
            self.txt_Address.delete('1.0', END)
            self.txt_Address.insert(END, row[8])
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Search details has been displayed.")




root = Tk()
ob = Student(root)
root.mainloop()

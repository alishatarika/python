from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import random
import requests
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()
class customerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        self.customername = StringVar()
        self.FatherName = StringVar()
        self.Gender = StringVar()
        self.MobileNumber = StringVar()
        self.Email = StringVar()
        self.PermanentAddress = StringVar()
        self.aadharnumber = StringVar()
        
        self.create_table()  
        
        # top image 
        image_url = "https://content.r9cdn.net/rimg/himg/a7/7e/50/ice-10360-99952962-873912.jpg?width=1200&height=630&crop=true"
        response = requests.get(image_url)
        img0 = Image.open(BytesIO(response.content))
        img0= img0.resize((1550, 140), Image.LANCZOS)
        self.photoimg0 = ImageTk.PhotoImage(img0)
        lbImage= Label(self.root, image=self.photoimg0, bd=4, relief=RIDGE)
        lbImage.place(x=0, y=0, width=1550, height=140)
        
        # Entry frame
        leftframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Data", font=("times new roman", 12, "bold"), bg="white", fg="black")
        leftframe.place(x=5, y=140, width=425, height=660)
        
        
        # Customer details
        customerREF = Label(leftframe, text="Customer Ref", width=15,font=("times new roman", 15, "bold"), padx=4, pady=6)
        customerREF.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=30, font=("arial", 15, "bold"), textvariable=self.var_ref)
        entry_ref.grid(row=0, column=1)
        
        customername = Label(leftframe, text="Customer Name",width=15, font=("times new roman", 15, "bold"), padx=4, pady=6)
        customername.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(leftframe, width=30, textvariable=self.customername, font=("arial", 15, "bold"))
        entry_name.grid(row=1, column=1)
        
        customerfathername = Label(leftframe, text="Father Name",width=15, font=("times new roman", 15, "bold"),padx=4 , pady=6)
        customerfathername.grid(row=2, column=0, sticky=W)
        entry_fathername = ttk.Entry(leftframe, width=30, textvariable=self.FatherName, font=("arial", 15, "bold"))
        entry_fathername.grid(row=2, column=1)
        
        customergender = Label(leftframe, text="Gender", width=15,font=("times new roman", 15, "bold"), padx=4, pady=4)
        customergender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(leftframe, font=("times new roman", 15, "bold"), width=30, textvariable=self.Gender, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.grid(row=3, column=1)
        
        customermobilenumber = Label(leftframe, text="Mobile Number", width=15,font=("times new roman", 15, "bold"), padx=4, pady=6)
        customermobilenumber.grid(row=4, column=0, sticky=W)
        entry_mobile = ttk.Entry(leftframe, width=30, font=("arial", 15, "bold"), textvariable=self.MobileNumber)
        entry_mobile.grid(row=4, column=1)
        
        customeremail = Label(leftframe, text="Email", font=("times new roman", 15, "bold"),width=15 ,padx=4, pady=6)
        customeremail.grid(row=5, column=0, sticky=W)
        entry_email = ttk.Entry(leftframe, width=30, font=("arial", 15, "bold"), textvariable=self.Email)
        entry_email.grid(row=5, column=1)
        
        customeraddress = Label(leftframe, text="Permanent Address", font=("times new roman", 15, "bold"),width=15, padx=4, pady=6)
        customeraddress.grid(row=6, column=0, sticky=W)
        entry_address = ttk.Entry(leftframe, width=30, font=("arial", 15, "bold"), textvariable=self.PermanentAddress)
        entry_address.grid(row=6, column=1)
        
        customerID = Label(leftframe, text="Aadhaar Card", font=("times new roman", 15, "bold"),width=15, padx=4, pady=6)
        customerID.grid(row=7, column=0, sticky=W)
        entry_aadhaar = ttk.Entry(leftframe, width=30, font=("arial", 15, "bold"), textvariable=self.aadharnumber)
        entry_aadhaar.grid(row=7, column=1)
        
        # Buttons frame to add, update, delete, reset
        btn_frame = Frame(leftframe, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=412, height=100)
        
        addbutton = Button(btn_frame, text="ADD", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14, command=self.add_data)
        addbutton.grid(row=0, column=0, padx=1)
        
        updatebutton = Button(btn_frame, text="UPDATE", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14,command=self.update1)
        updatebutton.grid(row=0, column=1, padx=1)
        
        deletebutton = Button(btn_frame, text="DELETE", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14,command=self.delete_data)
        deletebutton.grid(row=1, column=0, padx=1)
        
        close_btn = Button(btn_frame, text="Close", command=root.destroy, font=("times new roman", 18, "bold"), bg="red", fg="white", width=14)
        close_btn.grid(row=1,column=1,padx=1)
        
        
        # Right frame to show customer details
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=430, y=140, width=1200, height=660)
        
        detailframe = Frame(tableframe, bd=2, relief=RIDGE)
        detailframe.place(x=0, y=15, width=1100, height=600)
        
        scrollx = ttk.Scrollbar(detailframe, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(detailframe, orient=VERTICAL)
        
        self.Cust_Details_Table = ttk.Treeview(detailframe, column=("ref", "name", "fathername", "gender", "mobile", "email", "address", "aadhaar"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        scrollx.config(command=self.Cust_Details_Table.xview)
        scrolly.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref", text="Ref No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("fathername", text="Father's Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("address", text="Address")
        self.Cust_Details_Table.heading("aadhaar", text="Aadhaar")
        
        self.Cust_Details_Table["show"] = "headings"
        
        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("fathername", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("address", width=100)
        self.Cust_Details_Table.column("aadhaar", width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()
        
    def create_table(self):
        try:
            conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
            my_cursor = conn.cursor()
            my_cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                ref VARCHAR(10) PRIMARY KEY,
                customername VARCHAR(100),
                fathername VARCHAR(100),
                gender VARCHAR(10),
                mobilenumber VARCHAR(15),
                email VARCHAR(100),
                address VARCHAR(255),
                aadharnumber VARCHAR(20)
            )
            """)
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    
    def add_data(self):
        if self.customername.get() == "" or self.FatherName.get() == "" or self.MobileNumber=="" or self.aadharnumber=="":
            messagebox.showerror("Error", "These fields are required")
        else:
            try:
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_ref.get(),
                    self.customername.get(),
                    self.FatherName.get(),
                    self.Gender.get(),
                    self.MobileNumber.get(),
                    self.Email.get(),
                    self.PermanentAddress.get(),
                    self.aadharnumber.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}")

    def fetch_data(self):
        conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
            conn.close()
    
    def getcursor(self, event):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]
        self.var_ref.set(row[0])
        self.customername.set(row[1])
        self.FatherName.set(row[2])
        self.Gender.set(row[3])
        self.MobileNumber.set(row[4])
        self.Email.set(row[5])
        self.PermanentAddress.set(row[6])
        self.aadharnumber.set(row[7])


    def update1(self):
      if self.customername.get() == "" or self.FatherName.get() == "" or self.MobileNumber.get() == "" or self.aadharnumber.get() == "":
        messagebox.showerror("Error", "All fields are required")
      else:
        try:
            
            conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
            my_cursor = conn.cursor()
            my_cursor.execute("""
                UPDATE customer
                SET customername=%s, fathername=%s, gender=%s, mobilenumber=%s, email=%s, address=%s, aadharnumber=%s
                WHERE ref=%s
            """, (
                self.customername.get(),
                self.FatherName.get(),
                self.Gender.get(),
                self.MobileNumber.get(),
                self.Email.get(),
                self.PermanentAddress.get(),
                self.aadharnumber.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details have been updated", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

                
    
    def delete_data(self):
        deleteCustomer = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if deleteCustomer:
            try:
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute("""DELETE FROM customer WHERE ref = %s""",(self.var_ref.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been deleted", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                 
            
if __name__== "__main__":
    root = Tk()
    obj1 = customerWindow(root)
    root.mainloop()
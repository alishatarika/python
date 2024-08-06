from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import random
import requests
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()

class roomDetail:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        self.contact = StringVar()
        self.checkIn = StringVar()
        self.checkOut = StringVar()
        self.roomType = StringVar()
        self.roomAvailable = StringVar()
        self.meal = StringVar()
        self.noOfDays = StringVar()
        self.paidTax = StringVar()
        self.subTotal = StringVar()
        self.total = StringVar()
        self.create_table()
        
        # top image 
        image_url = "https://content.r9cdn.net/rimg/himg/a7/7e/50/ice-10360-99952962-873912.jpg?width=1200&height=630&crop=true"
        response = requests.get(image_url)
        img0 = Image.open(BytesIO(response.content))
        img0 = img0.resize((1550, 140), Image.LANCZOS)
        self.photoimg0 = ImageTk.PhotoImage(img0)
        lbImage = Label(self.root, image=self.photoimg0, bd=4, relief=RIDGE)
        lbImage.place(x=0, y=0, width=1550, height=140)
        
        
        # Entry frame
        leftframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("times new roman", 18, "bold"), padx=2, pady=2)
        leftframe.place(x=5, y=150, width=425, height=660)

        # Customer details
        customerContact = Label(leftframe, text="Customer Contact", font=("times new roman", 15, "bold"), padx=2, pady=6)
        customerContact.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=20, font=("arial", 15, "bold"), textvariable=self.contact)
        entry_ref.grid(row=0, column=1, sticky=W)

        # Fetch Data button
        fetchdata = Button(leftframe, text="Fetch Data", font=("times new roman", 11, "bold"), bg="black", fg="white", width=10, command=self.fetchRoom)
        fetchdata.place(x=323, y=5)

        checkIn = Label(leftframe, text="Check In", font=("times new roman", 15, "bold"), padx=2, pady=6)
        checkIn.grid(row=1, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=20, font=("arial", 15, "bold"), textvariable=self.checkIn)
        entry_ref.grid(row=1, column=1)

        checkOut = Label(leftframe, text="Check Out", font=("times new roman", 15, "bold"), padx=2, pady=6)
        checkOut.grid(row=2, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=20, font=("arial", 15, "bold"), textvariable=self.checkOut)
        entry_ref.grid(row=2, column=1)

        roomtype = Label(leftframe, text="Room Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        roomtype.grid(row=3, column=0, sticky=W)
        
        conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
        my_cursor = conn.cursor()
        my_cursor.execute("select  RoomType from details")
        row = my_cursor.fetchall()
        
        room = ttk.Combobox(leftframe, font=("times new roman", 15, "bold"), width=20, textvariable=self.roomType, state="readonly")
        room["value"] = row
        room.grid(row=3, column=1)

   
        Availableroom = Label(leftframe, text="Available Room", font=("times new roman", 15, "bold"), padx=2, pady=6)
        Availableroom.grid(row=4, column=0, sticky=W)
        
        conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT  RoomNo FROM details")
        rows = my_cursor.fetchall()
        
        Availroom = ttk.Combobox(leftframe, font=("times new roman", 15, "bold"), width=20, textvariable=self.roomAvailable, state="readonly")
        Availroom["value"] = rows
        Availroom.grid(row=4, column=1)

        
        meal = Label(leftframe, text="Meal", font=("times new roman", 15, "bold"), padx=2, pady=6)
        meal.grid(row=5, column=0, sticky=W)
        meal = ttk.Combobox(leftframe, font=("times new roman", 15, "bold"), width=20, textvariable=self.meal, state="readonly")
        meal["value"] = ("BreakFast", "Lunch","Dinner")
        meal.grid(row=5, column=1)
        
        NoOfDays = Label(leftframe, text="NO Of Days", font=("times new roman", 15, "bold"), padx=2, pady=6)
        NoOfDays.grid(row=6, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=20, font=("arial", 15, "bold"), textvariable=self.noOfDays)
        entry_ref.grid(row=6, column=1)
        
        PaidTax = Label(leftframe, text="Paid tax", font=("times new roman", 15, "bold"), padx=2, pady=6)
        PaidTax.grid(row=7, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=20, font=("arial", 15, "bold"), textvariable=self.paidTax)
        entry_ref.grid(row=7, column=1)
        
        SubTotal = Label(leftframe, text="Sub Total", font=("times new roman", 15, "bold"), padx=2, pady=6)
        SubTotal.grid(row=8, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=20, font=("arial", 15, "bold"), textvariable=self.subTotal)
        entry_ref.grid(row=8, column=1)
        
        total = Label(leftframe, text="Total Cost", font=("times new roman", 15, "bold"), padx=2, pady=6)
        total.grid(row=9, column=0, sticky=W)
        entry_ref = ttk.Entry(leftframe, width=20, font=("arial", 15, "bold"), textvariable=self.total)
        entry_ref.grid(row=9, column=1)
        
        btn_frame = Frame(leftframe, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=155)
        
        bill = Button(btn_frame, text="Bill", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14,command=self.billtotal)
        bill.grid(row=0, column=0, padx=1)
        
        addbutton = Button(btn_frame, text="ADD", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14,command=self.add_room)
        addbutton.grid(row=0, column=1, padx=1)
        
        updatebutton = Button(btn_frame, text="UPDATE", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14,command=self.updateroom)
        updatebutton.grid(row=1, column=0, padx=1)
        
        deletebutton = Button(btn_frame, text="DELETE", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14,command=self.delete_data)
        deletebutton.grid(row=1, column=1, padx=1)
        
        btn_frame2 = Frame(leftframe, bd=2, relief=RIDGE)
        btn_frame2.place(x=70, y=500, width=200, height=50)
        close_btn = Button(btn_frame2, text="Close", command=root.destroy, font=("times new roman", 18 , "bold"), bg="red", fg="white", width=14)
        close_btn.grid(row=0,column=1,padx=1)
        # Right frame to show customer details
        
        image_url = "https://media.istockphoto.com/id/627892060/photo/hotel-room-suite-with-view.jpg?s=612x612&w=0&k=20&c=YBwxnGH3MkOLLpBKCvWAD8F__T-ypznRUJ_N13Zb1cU="
        response = requests.get(image_url)
        img2 = Image.open(BytesIO(response.content))
        img2 = img2.resize((500, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbImage = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbImage.place(x=1050, y=140, width=500, height=200)
    
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room booking Details", font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=430, y=320, width=1200, height=660)
        
        detailframe = Frame(tableframe, bd=2, relief=RIDGE)
        detailframe.place(x=0, y=15, width=1100, height=600)
        
        scrollx = ttk.Scrollbar(detailframe, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(detailframe, orient=VERTICAL)
        
        self.RoomDetail_Table = ttk.Treeview(detailframe, column=("Contact Number", "Check In",
                                                                  "Check out","Room Type", "Room Available", "Meal", "No of days"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        scrollx.config(command=self.RoomDetail_Table.xview)
        scrolly.config(command=self.RoomDetail_Table.yview)
        
        self.RoomDetail_Table.heading("Contact Number", text="Contact Number")
        self.RoomDetail_Table.heading("Check In", text="Check In")
        self.RoomDetail_Table.heading("Check out", text="Check out")
        self.RoomDetail_Table.heading("Room Type", text="Room Type")
        self.RoomDetail_Table.heading("Room Available", text="Room Available")
        self.RoomDetail_Table.heading("Meal", text="Meal")
        self.RoomDetail_Table.heading("No of days", text="No of days")
        
        self.RoomDetail_Table["show"] = "headings"
        
        self.RoomDetail_Table.column("Contact Number", width=100)
        self.RoomDetail_Table.column("Check In", width=100)
        self.RoomDetail_Table.column("Check out", width=100)
        self.RoomDetail_Table.column("Room Type", width=100)
        self.RoomDetail_Table.column("Room Available", width=100)
        self.RoomDetail_Table.column("Meal", width=100)
        self.RoomDetail_Table.column("No of days", width=100)
        self.RoomDetail_Table.pack(fill=BOTH, expand=1)   
        self.RoomDetail_Table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()
        
    def create_table(self):
        try:
            conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
            my_cursor = conn.cursor()
            my_cursor.execute("""
            CREATE TABLE IF NOT EXISTS details (
            contact VARCHAR(255),
            checkIn VARCHAR(255),
            checkOut VARCHAR(255),
            roomType VARCHAR(255),
            roomAvailable VARCHAR(255),
            meal VARCHAR(255),
            noOfDays INT 
            )
            """)
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
       
    def fetchRoom(self):
        if self.contact.get() == "":
            messagebox.showerror("Error", "Please enter contact details", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                query = ("SELECT customername FROM customer WHERE mobilenumber = %s")
                value = (self.contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                
                if row == None:
                    messagebox.showerror("Error", "This number not found", parent=self.root)
                else:
                    conn.commit()
                    conn.close()
                    showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                    showDataframe.place(x=430, y=140, width=300, height=170)
                    
                    lblname = Label(showDataframe, text="Customer Name:", font=("times new roman", 12, "bold"))
                    lblname.place(x=0, y=0)
                    
                    lbl1 = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                    lbl1.place(x=120, y=0)
                    
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="Alisha@1210", database="hotelmanagement")
                    my_cursor = conn.cursor()
                    query = ("SELECT fathername FROM customer WHERE mobilenumber = %s")
                    value = (self.contact.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    
                    lblfather= Label(showDataframe, text="Father Name:", font=("times new roman", 12, "bold"))
                    lblfather.place(x=0, y=30)
                    
                    lbl2= Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                    lbl2.place(x=120, y=30)
                    
                    
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="Alisha@1210", database="hotelmanagement")
                    my_cursor = conn.cursor()
                    query = ("SELECT email FROM customer WHERE mobilenumber = %s")
                    value = (self.contact.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    
                    lblfather= Label(showDataframe, text="Father Name:", font=("times new roman", 12, "bold"))
                    lblfather.place(x=0, y=60)
                    
                    lbl2= Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                    lbl2.place(x=120, y=60)
                    
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="Alisha@1210", database="hotelmanagement")
                    my_cursor = conn.cursor()
                    query = ("SELECT email FROM customer WHERE mobilenumber = %s")
                    value = (self.contact.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    
                    lblfather= Label(showDataframe, text="Email:", font=("times new roman", 12, "bold"))
                    lblfather.place(x=0, y=60)
                    
                    lbl2= Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                    lbl2.place(x=120, y=60)
                    
                    
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="Alisha@1210", database="hotelmanagement")
                    my_cursor = conn.cursor()
                    query = ("SELECT address FROM customer WHERE mobilenumber = %s")
                    value = (self.contact.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    
                    lblfather= Label(showDataframe, text="Address:", font=("times new roman", 12, "bold"))
                    lblfather.place(x=0, y=90)
                    
                    lbl2= Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                    lbl2.place(x=120, y=90)
                    
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="Alisha@1210", database="hotelmanagement")
                    my_cursor = conn.cursor()
                    query = ("SELECT aadharnumber FROM customer WHERE mobilenumber = %s")
                    value = (self.contact.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    
                    lblfather= Label(showDataframe, text="Aadhaar Number:", font=("times new roman", 12, "bold"))
                    lblfather.place(x=0, y=120)
                    
                    lbl2= Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                    lbl2.place(x=120, y=120)
                    
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {str(err)}", parent=self.root)
                

                
    def add_room(self):
        if self.contact.get() == "" or self.checkIn.get() == "":
            messagebox.showerror("Error", "These fields are required")
        else:
            try:   
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                self.contact.get(),
                self.checkIn.get(),
                self.checkOut.get(),
                self.roomType.get(), 
                self.roomAvailable.get(),
                self.meal.get(),
                self.noOfDays.get()    
            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}")
                
                
    def fetch_data(self):
        conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
        my_cursor = conn.cursor()
        my_cursor.execute("select  * FROM room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.RoomDetail_Table.delete(*self.RoomDetail_Table.get_children())
            for i in rows:
                self.RoomDetail_Table.insert("", END, values=i)
            conn.commit()
            conn.close()
            
            
    def getcursor(self, event=""):
        cursor_row = self.RoomDetail_Table.focus()
        content = self.RoomDetail_Table.item(cursor_row)
        row = content["values"]
        self.contact.set(row[0]),
        self.checkIn.set(row[1]),
        self.checkOut.set(row[2]),
        self.roomType.set(row[3]), 
        self.roomAvailable.set(row[4]),
        self.meal.set(row[5]),
        self.noOfDays.set(row[6])   


    def updateroom(self):
        if self.contact.get() == "" or self.checkIn.get() == "":
           messagebox.showerror("Error", "All fields are required")
        else:
            try:
               conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
               my_cursor = conn.cursor()
               my_cursor.execute("""
                UPDATE room
                SET checkIn=%s, checkOut=%s, roomType=%s, roomAvailable=%s, meal=%s, noOfDays=%s
                WHERE contact=%s
                """,
                (
                    self.checkIn.get(),
                    self.checkOut.get(),
                    self.roomType.get(), 
                    self.roomAvailable.get(),
                    self.meal.get(),
                    self.noOfDays.get(),
                    self.contact.get()
                ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Update", "Room details have been updated", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


    
    def delete_data(self):
        deleteCustomer = messagebox.askyesno("Hotel Management System", "Do you want to delete this detail ?", parent=self.root)
        if deleteCustomer:
            try:
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM room WHERE contact = %s",  (self.contact.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data has been deleted", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


    def billtotal(self):
        inDate = self.checkIn.get()
        outDate = self.checkOut.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.noOfDays.set(abs((outDate - inDate).days))

        if self.noOfDays.get() == "":
           messagebox.showerror("Error", "No of days is required")
           return

        days = float(self.noOfDays.get())

        meal_price = {
           "BreakFast": 300,
           "Lunch": 400,
           "Dinner": 500
            }

        room_price = {
           "Single": 500,
           "Double": 600,
            "Luxury": 700
            }
  
        meal = self.meal.get()
        room_type = self.roomType.get()


        q1 = meal_price[meal]
        q2 = room_price[room_type]
        q3 = days
        q4 = (q1 + q2 )* q3

        Tax = "Rs. " + str("%.2f" % (q4 * 0.1))
        ST = "Rs. " + str("%.2f" % (q4))
        TT = "Rs. " + str("%.2f" % (q4 + (q4 * 0.1)))

        self.paidTax.set(Tax)
        self.subTotal.set(ST)
        self.total.set(TT)
                

if __name__ == "__main__":
    root = Tk()
    obj1 = roomDetail(root)
    root.mainloop()

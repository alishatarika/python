from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import requests
from io import BytesIO
import os
from dotenv import load_dotenv


load_dotenv()
class detailOfRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        self.floor = StringVar()
        self.roomNumber = StringVar()
        self.roomType = StringVar()
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
        leftframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("times new roman", 18, "bold"), padx=2, pady=2)
        leftframe.place(x=5, y=150, width=540, height=350)
        
        # floor
        floor = Label(leftframe, text="Floor", font=("times new roman", 15, "bold"), padx=2, pady=6)
        floor.grid(row=0, column=0, sticky=W)
        entry_floor = ttk.Entry(leftframe, width=20, font=("times new roman", 15, "bold"), textvariable=self.floor)
        entry_floor.grid(row=0, column=1, sticky=W)
        
        # room number
        roomNumber = Label(leftframe, text="Room No", font=("times new roman", 15, "bold"), padx=2, pady=6)
        roomNumber.grid(row=1, column=0, sticky=W)
        entry_roomNumber = ttk.Entry(leftframe, width=20, font=("times new roman", 15, "bold"), textvariable=self.roomNumber)
        entry_roomNumber.grid(row=1, column=1, sticky=W)
        
        # room type
        roomType = Label(leftframe, text="Room Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        roomType.grid(row=2, column=0, sticky=W)
        room = ttk.Combobox(leftframe, font=("times new roman", 15, "bold"), width=20, textvariable=self.roomType, state="readonly")
        room["value"] = ("Single", "Double", "Luxury")
        room.grid(row=2, column=1)
        
        # buttons
        btn_frame = Frame(leftframe, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=150, width=420, height=95)
        
        addbutton = Button(btn_frame, text="ADD", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14, command=self.add_room)
        addbutton.grid(row=0, column=0, padx=1)
        
        updatebutton = Button(btn_frame, text="UPDATE", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14, command=self.updateRoom)
        updatebutton.grid(row=0, column=1, padx=1)
        
        deletebutton = Button(btn_frame, text="DELETE", font=("times new roman", 18, "bold"), bg="black", fg="gold", width=14, command=self.deleteData)
        deletebutton.grid(row=1, column=0, padx=1)
        
        close_btn = Button(btn_frame, text="Close", command=root.destroy, font=("times new roman", 18, "bold"), bg="red", fg="white", width=14)
        close_btn.grid(row=1,column=1,padx=1)
        
        # table frame
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("times new roman", 18, "bold"), padx=2)
        tableframe.place(x=600, y=150, width=600, height=350)
        
        scrollx = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(tableframe, orient=VERTICAL)
        
        self.Room_Table = ttk.Treeview(tableframe, column=("Floor", "RoomNo", "RoomType"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        scrollx.config(command=self.Room_Table.xview)
        scrolly.config(command=self.Room_Table.yview)
        
        self.Room_Table.heading("Floor", text="Floor")
        self.Room_Table.heading("RoomNo", text="RoomNo")
        self.Room_Table.heading("RoomType", text="RoomType")
        
        self.Room_Table["show"] = "headings"
        
        self.Room_Table.column("Floor", width=100)
        self.Room_Table.column("RoomNo", width=100)
        self.Room_Table.column("RoomType", width=100)
        self.Room_Table.pack(fill=BOTH, expand=1) 
        self.Room_Table.bind("<ButtonRelease-1>", self.getcursor)
        self.fetch_data()
        
    def create_table(self):
        try:
            conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
            my_cursor = conn.cursor()
            my_cursor.execute("""
               CREATE TABLE IF NOT EXISTS details (
                   Floor VARCHAR(10),
                   RoomNo VARCHAR(10) PRIMARY KEY,
                   RoomType VARCHAR(20)
            )
            """)
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

        
    def add_room(self):
        if self.floor.get() == "" or self.roomNumber.get() == "" or self.roomType.get() == "":
            messagebox.showerror("Error", "These fields are required")
        else:
            try:
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO details VALUES(%s, %s, %s)", (
                    self.floor.get(),
                    self.roomNumber.get(),
                    self.roomType.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}")
    
    def fetch_data(self):
        conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
            conn.close()
            
    def getcursor(self, event=""):
        cursor_row = self.Room_Table.focus()
        content = self.Room_Table.item(cursor_row)
        row = content["values"]
        if row:
            self.floor.set(row[0])
            self.roomNumber.set(row[1])
            self.roomType.set(row[2])

    def updateRoom(self):
        if self.floor.get() == "" or self.roomNumber.get() == "" or self.roomType.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    UPDATE details
                    SET Floor=%s, RoomType=%s
                    WHERE RoomNo=%s
                    """, (
                    self.floor.get(),
                    self.roomType.get(),
                    self.roomNumber.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Room details have been updated", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def deleteData(self):
        deleteCustomer = messagebox.askyesno("Hotel Management System", "Do you want to delete this detail?", parent=self.root)
        if deleteCustomer:
            try:
                conn = mysql.connector.connect( host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM details WHERE RoomNo = %s", (self.roomNumber.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data has been deleted", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                

if __name__ == "__main__":
    root = Tk()
    obj1 = detailOfRoom(root)
    root.mainloop()

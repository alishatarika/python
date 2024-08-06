from tkinter import *
from PIL import Image, ImageTk
from customer import customerWindow
from room import roomDetail
from detail1 import detailOfRoom
from about import AboutUs
import requests
from io import BytesIO

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # background image 
        image_url = "https://images.pexels.com/photos/70441/pexels-photo-70441.jpeg?cs=srgb&dl=pexels-amar-saleem-15661-70441.jpg&fm=jpg"
        response = requests.get(image_url)
        self.bg = Image.open(BytesIO(response.content))
        self.bg= self.bg.resize((1550, 800), Image.LANCZOS)
        self.photoimg0 = ImageTk.PhotoImage(self.bg)
        lbImage2= Label(self.root, image=self.photoimg0, bd=4, relief=RIDGE)
        lbImage2.place(x=0, y=0, width=1550, height=800)
        
        #hotel name frame
        labeltitle = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", bg="black", font=("times new roman", 40, "bold"), fg="gold")
        labeltitle.place(x=0, y=0, width=1550, height=120)
        
        #frame for menu
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=120, width=260, height=220)
        
       
        labelmenu = Label(main_frame, text="MENU", bg="white", font=("times new roman", 20, "bold"), fg="black")
        labelmenu.place(x=0, y=0, width=230,height=50)
        
       #options for user
        buttonframe = Frame(main_frame, bd=4, relief=RIDGE)
        buttonframe.place(x=0, y=50, width=260, height=180)
        
        button4 = Button(buttonframe, text="ABOUT",command=self.HotelInfo,width=22, bg="black", font=("times new roman", 14, "bold"), fg="gold")
        button4.grid(row=0, column=0, pady=1)
    
        button1 = Button(buttonframe, text="CUSTOMER DETAILS",command=self.customerDetails, width=22, bg="black", font=("times new roman", 14, "bold"), fg="gold")
        button1.grid(row=1, column=0, pady=1)
        
        button2 = Button(buttonframe, text="ROOM BOOKING", command=self.roomDetail,width=22, bg="black", font=("times new roman", 14, "bold"), fg="gold")
        button2.grid(row=2, column=0, pady=1)
        
        button3 = Button(buttonframe, text="ROOMS AVAILABLE",command=self.RoomData, width=22, bg="black", font=("times new roman", 14, "bold"), fg="gold")
        button3.grid(row=3, column=0, pady=1)
        

    def customerDetails(self):
       self.new_window=Toplevel(self.root)
       self.app=customerWindow(self.new_window)

    def roomDetail(self):
       self.new_window=Toplevel(self.root)
       self.app=roomDetail(self.new_window)
       
    def RoomData(self):
       self.new_window=Toplevel(self.root)
       self.app=detailOfRoom(self.new_window)
       
    def HotelInfo(self):
       self.new_window=Toplevel(self.root)
       self.app=AboutUs(self.new_window)
        

if __name__ == "__main__":
    root= Tk()
    obj = HotelManagement(root)
    root.mainloop()
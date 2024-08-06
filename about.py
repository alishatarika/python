from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

class AboutUs:
    def __init__(self, root):
        self.root = root
        self.root.title("About Us")
        self.root.geometry("1550x800+0+0")
        
        # Background Image
        image_url = "https://www.pymnts.com/wp-content/uploads/2016/05/Hotel-Room-Secondary-Market.jpg"
        response = requests.get(image_url)
        self.bg = Image.open(BytesIO(response.content))
        self.bg = self.bg.resize((1550, 800), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg)

        self.bg_label = Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # About Us Frame
        about_frame = Frame(self.root, bg="white", bd=5)
        about_frame.place(x=450, y=0, width=750, height=800)

        # Title
        title = Label(about_frame, text="About Hotel Management System", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title.place(x=0, y=0)

        # Description
        desc = Label(about_frame, text=("Welcome to our Hotel Management System!\n"
                                        "This application is designed to streamline hotel operations, manage room bookings,\n"
                                        "and handle guest information efficiently. It offers a user-friendly interface for\n"
                                        "hotel staff to perform their daily tasks.\n\n"
                                        "Developed using Python with Tkinter for the graphical interface and MySQL\n"
                                        "for database management, our system ensures reliability and performance.\n"
                                        "It is suitable for hotels aiming to improve their\n"
                                        "operational efficiency and guest satisfaction.\n\n"
                                        "Our system provides a range of features that cater to the needs of hotel management,\n"
                                        "including room service management, billing, and customer relationship management.\n\n"
                                        "We continuously update our system to incorporate the latest industry trends and\n"
                                        "technologies, ensuring that your hotel stays ahead of the competition. Whether you\n"
                                        "are running a small boutique hotel or a large chain, our Hotel Management System\n"
                                        "can be customized to meet your specific needs."), 
                      font=("times new roman", 16), bg="white", fg="black", justify=LEFT)
        desc.place(x=0, y=60)

        desc1 = Label(about_frame, text="Features: \n"
                                        "<>Individual Customer Report \n"
                                        "<>Room Details \n"
                                        "<>Details Of New Room \n"
                                        "<>Opening a new room \n"
                                        "<>Room Activities Safely \n",
                      font=("times new roman", 16), bg="white", fg="black", justify=LEFT)
        
        desc1.place(x=0, y=550)

        # Close Button
        close_btn = Button(about_frame, text="Close", command=root.destroy, font=("times new roman", 18, "bold"), bg="red", fg="white", width=10)
        close_btn.place(x=0, y=700)

if __name__ == "__main__":
    root = Tk()
    obj1 = AboutUs(root)
    root.mainloop()

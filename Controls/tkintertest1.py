from Tkinter import *
import tkFont
from PIL import ImageTk,Image


class screen:

    def __init__(self, master):
        self.master = master
        self.framei = Frame(master)
        self.framei["bg"] = "black"
        self.framei.pack()
        image2 = Image.open("C:/Users/Harshit Soni/Desktop/python/music/gui/logo.jpg")
        image1 = ImageTk.PhotoImage(image2)
        bg_image =Label(self.framei,image = image1)
        bg_image.place(x=0, y=0, relwidth=1, relheight=1)
        fontx = tkFont.Font(family="Helvetica", size=16, weight="bold")
        fonty = tkFont.Font(family="Times", size=12, weight="normal")
        self.button1 = Button(self.framei, text="Play my own Music", command=self.ownmusic, font=fontx, fg="red", bg="white")
        self.button2 = Button(self.framei, text="Use camera", command=self.camera1, font=fontx, fg="red", bg="white")
        # self.button3 = Button(self.framei, text="Ask me questions", command=self.questions)
        self.text1 = Label(self.framei,text="This is the very first player to play music online and it uses mood based sentiment analysis", font=fontx, fg="red", bg="white")
        self.text2 = Label(self.framei, text="How would you like to listen to music?", font=fonty, fg="red", bg="white")
        self.text3 = Label(self.framei, text="Can we use camera to select best fit music for you?", font=fonty, fg="red", bg="white")
        # self.text4 = Label(self.framei, text = "Not in Mood for a picture? We can ask you questions!")
        self.text5 = Label(self.framei, text="Have your own Music? No worries, we can play it too!", font=fonty, fg="red", bg="white")
        self.text1.grid(row=0, columnspan=4, pady=2)
        self.text2.grid(row=0, columnspan=4, pady=2)
        self.text3.grid(row=0, column=2, columnspan=2, pady=5)
        self.button2.grid(row=4, column=0, columnspan=2)
        # self.text4.grid(row=3, column=2,columnspan=2, pady=5)
        # self.button3.grid(row=4, column=2, columnspan=2)
        self.text5.grid(row=5, column=0, columnspan=4, pady=10)
        self.button1.grid(row=6, column=0, columnspan=4)

    def ownmusic(self):
        self.button1.configure(bg="green")
        pass

    def camera1(self):
        self.button2.configure(bg="green")
        pass

root = Tk()
musicapp = screen(root)
root.title("MUSIC RECOMMENDATION SYSTEM")
root.geometry("720x360")
root.mainloop()

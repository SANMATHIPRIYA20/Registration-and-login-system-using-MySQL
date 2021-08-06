from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql


class welcome:
    def __init__(self, root):

        self.root=root
        self.root.title("WELCOME PAGE")
        self.root.geometry("1350x700+0+0")
        # Background Image
        self.bg = ImageTk.PhotoImage(file="images/w1.jpg")
        bg=Label(self.root, image=self.bg, bg="#001a00").place(x=0,y=0,relwidth=1,relheight=1)
        bg1=Label(self.root, text="We're Glad You're Here!",font=("times new roman", 20, "bold"), bg = "#ffdd99", fg = "#336600").place(x=500,y=400)

        footer_name = Label(root, text="Created & Developed By SANMATHIPRIYA B S\nContact@sanmathipriyabs50@gmail.com", font=("comic sans ms", 23, "bold"), bg="#ffdd99", fg="#000d1a").place(x=620, y=605)

        # Button for closing
        btn_exit = Button(root,text="EXIT",font=("times new roman", 18),bg="#3CBC71", cursor="hand2",command=self.exitpro).place(x=50, y=550)
        btn_back = Button(root,text="Back to Registration Page", font=("times new roman", 18),bg="#3CBC71",cursor="hand2",command=self.register_window).place(x=50,y=630)
    def register_window(self):
        self.root.destroy()
        import register


    def exitpro(self):
        res = messagebox.askquestion('Exit Application', 'Do you really want to exit')
        if res == 'yes':
            root.destroy()
        else:
            messagebox.showinfo('Return', 'Returning back to program')





root=Tk()
obj=welcome(root)
root.mainloop()
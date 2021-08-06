from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
from tkinter import messagebox,ttk


class login_widow():
    def __init__(self, root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        login_frame=Frame(self.root, bg="#87CEEB")
        login_frame.place(x=350,y=100, width=700, height=500)
        title=Label(login_frame,text="    LOGIN HERE    ", font=("times new roman",30, "bold"), bg="#021e2f", fg="#87CEEB").place(x=180,y=40)

        email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 15, "bold"), bg="#87CEEB",fg="#021e2f").place(x=70, y=140)
        self.txt_email = Entry(login_frame,font=("times new roman", 15), bg="white",fg="#021e2f")
        self.txt_email.place(x=70, y=170, width=350,height=35)

        pass_= Label(login_frame, text="PASSWORD", font=("times new roman", 15, "bold"), bg="#87CEEB",fg="#021e2f").place(x=70, y=240)
        self.txt_pass_ = Entry(login_frame,show = '*',font=("times new roman", 15), bg="white", fg="#021e2f")
        self.txt_pass_.place(x=70, y=270, width=350, height=35)

        btn_login = Button(login_frame, text="Login", font=("times new roman", 20, "bold"), bg="#FF8C00",fg="black",cursor="hand2", command = self.login).place(x=70, y=320,width=180,height=40)
        btn_reg=Button(login_frame,text="Don't have an account? Register", font=("times new roman",14), bg="#87CEEB", bd=0,fg="black",cursor="hand2", command=self.register_window).place(x=70,y=390)
        btn_forgot = Button(login_frame, text="Forgot Password?", font=("times new roman", 14), bg="#87CEEB", bd=0,fg="red", cursor="hand2", command=self.forgot_password_window).place(x=350, y=390)



    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)


    def forgot_password(self):
        if self.cmb_quest.get()=="Select"or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email = %s and question = %s and answer=%s", (self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Please select the correct Security Question/Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email = %s",(self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your password has been reset successfully, Please login with your new password",parent = self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)




    def forgot_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email = %s", (self.txt_email.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("350x400+450+150")
                    self.root2.config(bg="#021e2f")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forgot Password?", font=("times new roman", 20, "bold"), bg="#021e2f",fg="#ff0000").place(x=0, y=10, relwidth=1)

                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),bg="#021e2f", fg="#e6f2ff").place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly',justify=CENTER)
                    self.cmb_quest['values'] = ( "Select", "What is Your Favorite Color?", "Which primary school did you attend?","What is your Your Nickname?")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="#021e2f",fg="#e6f2ff").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15))
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),bg="#021e2f", fg="#e6f2ff").place(x=50, y=260)
                    self.txt_new_pass = Entry(self.root2, show ="*",font=("times new roman", 15))
                    self.txt_new_pass.place(x=50, y=290, width=250)

                    bn_change_password = Button(self.root2, text="Reset Password", command=self.forgot_password,bg="green", fg="white", font=("times new roman", 15, "bold")).place(x=50, y=340)


            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror('Error', 'All Required Are Required', parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root",password="",database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email = %s and password=%s", (self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'INVALID EMAIL ID OR PASSWORD', parent=self.root)

                else:
                    messagebox.showinfo('SUCCESS', 'WELCOME!', parent=self.root)
                    self.root.destroy()
                    import test
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root=Tk()
obj=login_widow(root)
root.mainloop()
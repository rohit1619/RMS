from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

class Login:
	def __init__(self, root):
		self.root=root
		self.root.title("RMS Login")
		self.root.geometry("900x550+220+60")
		self.root.config(bg="lightgray")
		#---Title Frame---#
		frame_title=Frame(self.root,bg="lightblue").place(x=0,y=10,width=900,height=50)
		title=Label(frame_title,text="Real Management System",font=("times new roman",25,"bold"),bg="lightblue",fg="blue").place(x=240,y=10)
		#==Login Frame==#
		frame1=Frame(self.root,bg="white")
		frame1.place(x=430,y=60,width=460,height=430)
		frame_Id=Frame(frame1,bg="gray")
		frame_Id.place(x=5,y=70,width=450,height=45)
		frame_pass=Frame(frame1,bg="gray")
		frame_pass.place(x=5,y=125,width=450,height=45)
		frame_sec=Frame(frame1,bg="gray")
		frame_sec.place(x=5,y=180,width=450,height=45)
		frame_btn=Frame(frame1,bg="gray")
		frame_btn.place(x=5,y=235,width=450,height=45)
		frame_fg=Frame(frame1,bg="gray")
		frame_fg.place(x=5,y=290,width=450,height=45)

		#---Text field & label---#
		user_id=Label(frame_Id,text="User Id ",font=("times new roman",18,"bold"),bg="gray",fg="black").place(x=20,y=10)
		self.txt_user_id=Entry(frame_Id,font=("times new roman",15),bg="white")
		self.txt_user_id.place(x=140,y=10,width=260,height=30)
		password=Label(frame_pass,text="Password ",font=("times new roman",18,"bold"),bg="gray",fg="black").place(x=20,y=10)
		self.txt_password=Entry(frame_pass,font=("times new roman",15),bg="white")
		self.txt_password.place(x=140,y=10,width=260,height=30)
		sec=Label(frame_sec,text="Section ",font=("times new roman",18,"bold"),bg="gray",fg="black").place(x=20,y=10)
		self.txt_sec=ttk.Combobox(frame_sec,font=("times new roman",15),state="readonly",justify=CENTER)
		self.txt_sec['values']=(["Select","2k13-16","2k14-17","2k15-18","2k16-19","2k17-20","2k18-21","2k19-22"])
		self.txt_sec.place(x=140,y=10,width=260,height=30)
		self.txt_sec.current(0)

		#----Buttons----#
		btn_login=Button(frame_btn,text="Login",width=20,bg="lightblue",fg="black",font=("times new roman",15),command=self.login_data).place(x=80,y=5)
		btn_register=Button(frame_fg,text="Forget Password ?",width=18,fg="blue",font=("times new roman",15),command=self.register).place(x=240,y=5)

		#---Image----#
		self.bg=ImageTk.PhotoImage(file="rms1.jpg")
		bg=Label(self.root,image=self.bg).place(x=10,y=120,width=400,height=320)


		#---Footer Frame---#
		frame_footer=Frame(self.root,bg="lightblue")
		frame_footer.place(x=0,y=490,width=900,height=50)
		footer=Label(frame_footer,text="Welcome To RMS School Automation System",font=("times new roman",25,"bold"),bg="lightblue",fg="blue").place(x=120,y=10)
		
	def login_data(self):
		if self.txt_user_id.get() == '' or self.txt_password.get() == '':
			messagebox.showerror("Error","All fields are required",parent=self.root)
		else:
			try:
				mydb = mysql.connector.connect(host="localhost",user="root",password="",database="python_project")
				cur=mydb.cursor()
				cur.execute("SELECT * FROM register_data WHERE phone = %s AND password = %s ",(self.txt_user_id.get(),self.txt_password.get()))
				row=cur.fetchone()
				if row == None :messagebox.showerror('Error', "Login failed,Invalid Username or Password.Try again!!!")
				else:
					 messagebox.showinfo("Success","Login Successfully",parent=self.root)
					 self.root.destroy()
					 import home

				mydb.commit()
				mydb.close()
			except Exception as es:
				messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)
	def register(self):
		self.root.destroy()
		import register
root=Tk()
obj=Login(root)
root.mainloop()
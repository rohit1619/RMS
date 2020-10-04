from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

class Register:
	def __init__(self,root):
		self.root=root
		self.root.title("Registration Window")
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")
		#==BG image==#
		self.bg=ImageTk.PhotoImage(file="pic.jpg")
		bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

		#==LEFT image==#
		self.left=ImageTk.PhotoImage(file="pic1.jpg")
		left=Label(self.root,image=self.left).place(x=80,y=100,width=450,height=500)

		#==Registration Frame==#
		frame1=Frame(self.root,bg="white")
		frame1.place(x=480,y=100,width=700,height=500)

		title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

		
		f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=60,y=90)
		self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_fname.place(x=60,y=120,width=250)
		l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=90)
		self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_lname.place(x=350,y=120,width=250)

		con_t=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=60,y=160)
		self.txt_con=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_con.place(x=60,y=190,width=250)
		e_mail=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=160)
		self.txt_em=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_em.place(x=350,y=190,width=250)
		
		question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=60,y=230)
		self.txt_que=ttk.Combobox(frame1,font=("times new roman",12),state="readonly",justify=CENTER)
		self.txt_que['values']=(["Select","Your First Pet","Your Favirate Book","Your High School Name"])
		self.txt_que.place(x=60,y=260,width=250)
		self.txt_que.current(0)
		answer=Label(frame1,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=230)
		self.txt_ans=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_ans.place(x=350,y=260,width=250)
		
		password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=60,y=300)
		self.txt_pas=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_pas.place(x=60,y=330,width=250)
		cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=300)
		self.txt_cpas=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_cpas.place(x=350,y=330,width=250)
		
		self.var_chk=IntVar()
		chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=60,y=380)
		
		btn_register=Button(frame1,text="Register",width=30,bg="blue",fg="white",font=("times new roman",15),command=self.register_data).place(x=180,y=420)
		btn_login=Button(root,text="Log In",width=20,bg="red",fg="yellow",font=("times new roman",15),command=self.login).place(x=150,y=520)

	def register_data(self):
		if self.txt_fname.get() == '' or self.txt_lname.get() == '' or self.txt_con.get() == '' or self.txt_em.get() == '' or self.txt_que.get() =='Select' or self.txt_ans.get() == '' or self.txt_pas.get() == '' or self.txt_cpas.get() == '':
			messagebox.showerror("Error","All fields are required",parent=self.root)
		elif self.txt_pas.get() != self.txt_cpas.get():
			messagebox.showerror("Error","Password does not matched",parent=self.root)
		elif self.var_chk.get() == 0:
			messagebox.showerror("Error","Please Agree our terms & conditions",parent=self.root)
		else:
			try:
				mydb = mysql.connector.connect(host="localhost",user="root",password="",database="python_project")
				cur=mydb.cursor()
				cur.execute("insert into register_data (f_name,l_name,phone,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
					        (self.txt_fname.get(),
					        self.txt_lname.get(),
					        self.txt_con.get(),
					        self.txt_em.get(),
					        self.txt_que.get(),
					        self.txt_ans.get(),
					        self.txt_pas.get()

					        	))
				mydb.commit()
				mydb.close()
				messagebox.showinfo("Info","Register Successfully",parent=self.root)
			except Exception as es:
				messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)
	def login(self):
		self.root.destroy()
		import login
		


root=Tk()
obj=Register(root)
root.mainloop()
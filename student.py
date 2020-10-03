from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql



class Student:
	def __init__(self, root):
		self.root=root
		self.root.title("School Automation System")
		self.root.geometry("1300x680+25+0")
		self.root.config(bg="gray")
		#---Title Frame---#
		frame_title=Frame(self.root,bg="lightblue").place(x=0,y=10,width=1300,height=50)
		title=Label(frame_title,text="Real Management System",font=("times new roman",25,"bold"),bg="lightblue",fg="blue").place(x=440,y=10)
		#==Student Details Frame==#
		frame1=Frame(self.root,bg="brown")
		frame1.place(x=30,y=70,width=460,height=580)
		#==Student Frame==#
		frame2=Frame(self.root,bg="brown")
		frame2.place(x=500,y=70,width=770,height=580)

		#----Text field & Labels---#
		data_title=Label(frame1,text="Manage Students",font=("times new roman",18,"bold"),bg="brown",fg="white").place(x=110,y=20)
		roll=Label(frame1,text="Roll No.",font=("times new roman",15,"bold"),bg="brown",fg="white").place(x=30,y=80)
		self.txt_roll=Entry(frame1,font=("times new roman",14),bg="white")
		self.txt_roll.place(x=130,y=80,width=260,height=30)
		name=Label(frame1,text="Name",font=("times new roman",15,"bold"),bg="brown",fg="white").place(x=30,y=130)
		self.txt_name=Entry(frame1,font=("times new roman",14),bg="white")
		self.txt_name.place(x=130,y=130,width=260,height=30)
		email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="brown",fg="white").place(x=30,y=180)
		self.txt_email=Entry(frame1,font=("times new roman",14),bg="white")
		self.txt_email.place(x=130,y=180,width=260,height=30)
		gender=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="brown",fg="white").place(x=30,y=230)
		self.txt_gender=ttk.Combobox(frame1,font=("times new roman",14),state="readonlt",justify=CENTER)
		self.txt_gender['values']=(["Select","Male","Female","Transgender"])
		self.txt_gender.place(x=130,y=230,width=260,height=30)
		self.txt_gender.current(0)
		contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="brown",fg="white").place(x=30,y=280)
		self.txt_contact=Entry(frame1,font=("times new roman",14),bg="white")
		self.txt_contact.place(x=130,y=280,width=260,height=30)
		dob=Label(frame1,text="D.O.B",font=("times new roman",15,"bold"),bg="brown",fg="white").place(x=30,y=330)
		self.txt_dob=Entry(frame1,font=("times new roman",14),bg="white")
		self.txt_dob.place(x=130,y=330,width=260,height=30)
		address=Label(frame1,text="Address",font=("times new roman",15,"bold"),bg="brown",fg="white").place(x=30,y=380)
		self.txt_address=Entry(frame1,font=("times new roman",14),bg="white")
		self.txt_address.place(x=130,y=380,width=260,height=60)

		#---Button Frame----#
		frame_btn=Frame(frame1,bg="#CBF9EC")
		frame_btn.place(x=10,y=490,width=440,height=40)
		#----Buttons----#
		btn_add=Button(frame_btn,text="Add",bg="#03F7B2",fg="black",font=("times new roman",15),command=self.add_data).place(x=10,y=5,width=100,height=30)
		btn_update=Button(frame_btn,text="Update",bg="#03F7B2",fg="black",font=("times new roman",15),command=self.update_data).place(x=115,y=5,width=100,height=30)
		btn_delete=Button(frame_btn,text="Delete",bg="#03F7B2",fg="black",font=("times new roman",15),command=self.delete_data).place(x=220,y=5,width=100,height=30)
		btn_exit=Button(frame_btn,text="Clear",bg="#03F7B2",fg="black",font=("times new roman",15),command=self.clear).place(x=325,y=5,width=100,height=30)

		#----Search Bar-----#
		search=Label(frame2,text="Search By",font=("times new roman",16,"bold"),bg="brown",fg="white").place(x=10,y=20)
		self.search_by=ttk.Combobox(frame2,font=("times new roman",14),state="readonly",justify=CENTER)
		self.search_by['values']=(["Select","roll","email","name"])
		self.search_by.place(x=120,y=20,width=100)
		self.search_by.current(0)
		self.search_txt=Entry(frame2,font=("times new roman",14),bg="white")
		self.search_txt.place(x=250,y=20,width=160)
		search_btn=Button(frame2,text="Search",bg="lightgray",fg="black",font=("times new roman",14),command=self.search_data).place(x=440,y=20,width=100,height=30)
		all_search_btn=Button(frame2,text="Search All",font=("times new roman",14),command=self.data_table,bg="lightgray",fg="black").place(x=560,y=20,width=120,height=30)



		#------student table----#
		list_frame=Frame(frame2,bd=4,relief=RIDGE,bg="white")
		list_frame.place(x=6,y=80,width=754,height=470)
		scroll_x=Scrollbar(list_frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(list_frame,orient=VERTICAL)
		self.student_table=ttk.Treeview(list_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.student_table.xview)
		scroll_y.config(command=self.student_table.yview)
		self.student_table.heading("roll",text="Roll No.")
		self.student_table.heading("name",text="Name")
		self.student_table.heading("email",text="Email")
		self.student_table.heading("gender",text="Gender")
		self.student_table.heading("contact",text="Contact")
		self.student_table.heading("dob",text="DOB")
		self.student_table.heading("address",text="Address")
		self.student_table['show']='headings'
		self.student_table.column("roll",width=100)
		self.student_table.column("name",width=150)
		self.student_table.column("email",width=150)
		self.student_table.column("gender",width=150)
		self.student_table.column("contact",width=150)
		self.student_table.column("dob",width=150)
		self.student_table.column("address",width=150)
		self.student_table.pack(fill=BOTH,expand=1)
		self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.data_table()

	#---- Add Data Function----#
	def add_data(self):
		if self.txt_roll.get()=="" or self.txt_name.get()=="" or self.txt_gender.get()=="Select" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_address.get()=="" or self.txt_dob.get()=="":
			messagebox.showerror("Error","All field are requried")
		else:
			try:
				con=pymysql.connect(host="localhost",user="root",password="",database="python_project")
				cur=con.cursor()
				cur.execute("insert into student_data (roll,name,email,gender,phone,dob,address) values(%s,%s,%s,%s,%s,%s,%s)",
					        (self.txt_roll.get(),
					        self.txt_name.get(),
					        self.txt_email.get(),
					        self.txt_gender.get(),
					        self.txt_contact.get(),
					        self.txt_dob.get(),
					        self.txt_address.get()

					        	))
				con.commit()
				self.clear()
				self.data_table()
				con.close()
				messagebox.showinfo("Info","Register Successfully",parent=self.root)
			except Exception as es:
				messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

	#----Featch Data For Table---#
	def data_table(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="python_project")
		cur=con.cursor()
		cur.execute("select * from student_data")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END,values=row)
			con.commit()
		con.close()

	#---Clear Function-----#
	def clear(self):
		self.txt_roll.delete(first=0,last=22)
		self.txt_name.delete(first=0,last=22)
		self.txt_email.delete(first=0,last=22)
		self.txt_gender.delete(first=0,last=22)
		self.txt_gender.insert(END,"Select")
		self.txt_contact.delete(first=0,last=22)
		self.txt_dob.delete(first=0,last=22)
		self.txt_address.delete(first=0,last=22)

	#--Cursor Function---#
	def get_cursor(self,ev):
		cursor_row=self.student_table.focus()
		contents=self.student_table.item(cursor_row)
		row=contents['values']
		self.txt_roll.delete(first=0,last=22)
		self.txt_roll.insert(END,row[0])
		self.txt_name.delete(first=0,last=22)
		self.txt_name.insert(END,row[1])
		self.txt_email.delete(first=0,last=22)
		self.txt_email.insert(END,row[2])
		self.txt_gender.delete(first=0,last=22)
		self.txt_gender.insert(END,row[3])
		self.txt_contact.delete(first=0,last=22)
		self.txt_contact.insert(END,row[4])
		self.txt_dob.delete(first=0,last=22)
		self.txt_dob.insert(END,row[5])
		self.txt_address.delete(first=0,last=22)
		self.txt_address.insert(END,row[6])

	#---Update Function---#
	def update_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="python_project")
		cur=con.cursor()
		cur.execute("update student_data set name=%s,email=%s,gender=%s,phone=%s,dob=%s,address=%s where roll=%s",
					        (
					        self.txt_name.get(),
					        self.txt_email.get(),
					        self.txt_gender.get(),
					        self.txt_contact.get(),
					        self.txt_dob.get(),
					        self.txt_address.get(),
					        self.txt_roll.get()

					        	))
		con.commit()
		self.clear()
		self.data_table()
		con.close()

	#---Delete Function----#
	def delete_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="python_project")
		cur=con.cursor()
		cur.execute("delete from student_data where roll=%s",self.txt_roll.get())
		con.commit()
		self.clear()
		self.data_table()
		con.close()

	#----Search Data Function---#
	def search_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="python_project")
		cur=con.cursor()
		cur.execute("select * from student_data where "+str(self.search_by.get())+"=%s",self.search_txt.get())
		rows=cur.fetchall()
		if len(rows)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END,values=row)
			con.commit()
		con.close()
		

root=Tk()
obj=Student(root)
root.mainloop()
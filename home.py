from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

class Home:
	def __init__(self, root):
		self.root=root
		self.root.title("School Automation System")
		self.root.geometry("1300x680+25+0")
		self.root.config(bg="white")
		
		#--Menu Frame---#
		menu_frame=Frame(self.root,bg="#2C4B43")
		menu_frame.place(x=0,y=2,width=1300,height=58)
		menu_frame_sub=Frame(menu_frame,bg="#D4E5E0")
		menu_frame_sub.place(x=0,y=10,width=1300,height=30)

		#---Menu Buttons----#

		btn_sessition=Button(menu_frame_sub,text="Session Details",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=30,y=0)
		btn_student=Button(menu_frame_sub,text="Student",bg="#D4E5E0",fg="black",font=("times new roman",15),command=self.student).place(x=170,y=0)
		btn_fee=Button(menu_frame_sub,text="Fee",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=245,y=0)
		btn_result=Button(menu_frame_sub,text="Result",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=290,y=0)
		btn_transport=Button(menu_frame_sub,text="Transport",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=358,y=0)
		btn_document=Button(menu_frame_sub,text="Document",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=453,y=0)
		btn_setting=Button(menu_frame_sub,text="Settings",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=550,y=0)
		btn_staff=Button(menu_frame_sub,text="Staff Management",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=630,y=0)
		btn_exit=Button(menu_frame_sub,text="Exit",bg="#D4E5E0",fg="black",font=("times new roman",15)).place(x=790,y=0)

		#-----Body Labels----#
		main_label=Label(self.root,text="Main Pannel TO Access all resources of software",font=("times new roman",28,"bold"),bg="white",fg="blue").place(x=20,y=120)
		title_label=Label(self.root,text="School Management Software",font=("times new roman",28,"bold"),bg="white",fg="blue").place(x=320,y=320)
		title_phone=Label(self.root,text="Phone Number : 6207232847",font=("times new roman",18,"bold"),bg="white",fg="deeppink").place(x=900,y=480)
		title_email=Label(self.root,text="Email Id : rk730mishra@gmail.com",font=("times new roman",18,"bold"),bg="white",fg="deeppink").place(x=900,y=520)
		title_site=Label(self.root,text="Website : www.sarscoders.com",font=("times new roman",18,"bold"),bg="white",fg="deeppink").place(x=900,y=560)

		#---Footer Frame---#
		frame_footer=Frame(self.root,bg="#2C4B43")
		frame_footer.place(x=0,y=630,width=1300,height=50)

	def student(self):
		self.root.destroy()
		import student
		

root=Tk()
obj=Home(root)
root.mainloop()
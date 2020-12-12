from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox

#connecting to database axis which has 3 table - admin,student,teacher amd getting a cursor of it

mydb = mysql.connect(host="localhost",user="root",password="",database="axis")
c = mydb.cursor(buffered=True)



#admin function gives admin different options(create account of students and teachers,edit account of students and teachers,delete account of students and teachers,edit his own profile) to take action
def root_1():
  global root1
  root1=Tk()
  root1.title("COLLEGE MANGEMENT SYSTEM")
  root1.geometry('1080x720')
  root1.configure(bg='bisque')


  frame1=LabelFrame(root1,text='ADMIN PAGE',padx=100,pady=100)
  frame1.pack(padx=50,pady=50)

  
  #this button is used to create accounts
  account_button=Button(frame1,text='Create Account',font=('Helvetica',10),padx=10,pady=10,command=create_account)
  account_button.grid(row=0,column=0,padx=10,pady=15)

  global root1_clicked
  root1_clicked=StringVar()
  root1_clicked.set("TEACHER")
  #this optionmenu gives option to create account of student or teacher
  account_option=OptionMenu(frame1,root1_clicked,"STUDENT","TEACHER")
  account_option.grid(row=0,column=1)

  #this button is used to edit accounts
  edit_button=Button(frame1,text='Edit Account',font=('Helvetica',10),padx=10,pady=10,command=edit_account)
  edit_button.grid(row=1,column=0,padx=10,pady=15)

  global root1_clicked1
  root1_clicked1=StringVar()
  root1_clicked1.set("STUDENT")
  #this optionmenu gives option to edit account of student or teacher
  account_option1=OptionMenu(frame1,root1_clicked1,"STUDENT","TEACHER")
  account_option1.grid(row=1,column=1)


  #this button is used to delete accounts
  delete_button=Button(frame1,text='Delete Account',font=('Helvetica',10),padx=10,pady=10,command=delete_account)
  delete_button.grid(row=2,column=0,padx=10,pady=15)

  global root1_clicked2
  root1_clicked2=StringVar()
  root1_clicked2.set("STUDENT")
  #this optionmenu gives option to delete account of student or teacher
  account_option2=OptionMenu(frame1,root1_clicked2,"STUDENT","TEACHER")
  account_option2.grid(row=2,column=1)

  #this button is used to edit his profile
  edit_button1=Button(frame1,text='EDIT YOUR PROFILE',command=edit_admin)
  edit_button1.grid(row=3,column=0,columnspan=2,padx=10,pady=15)  

  #logout_button
  logout_button=Button(frame1,text='Logout',bg='RED',command=back_to_root)
  logout_button.grid(row=4,column=0,columnspan=2,padx=10,pady=15)


  root1.mainloop()





  #teacher function is used to take actions like add attendance,add mark,edit profile and logout
def root_2():
  global root2 
  root2=Tk()
  root2.title("COLLEGE MANGEMENT SYSTEM")
  root2.geometry('1080x720')
  root2.configure(bg='bisque')
  frame1=LabelFrame(root2,text='TEACHER PAGE',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
  
  #this button is used to add attendance
  add_attendance_button=Button(frame1,text='Add Attendance',font=('Helvetica',10),padx=10,pady=10,command=add_attendance)
  add_attendance_button.grid(row=0,column=0,padx=10,pady=15)

  #this button is used to add mark
  add_mark_button=Button(frame1,text='Add Mark',font=('Helvetica',10),padx=10,pady=10,command=add_mark)
  add_mark_button.grid(row=1,column=0,padx=10,pady=15)

  #this button is used to edit his profile
  edit_profile_button=Button(frame1,text='Edit Your Profile',font=('Helvetica',10),padx=10,pady=10,command=edit_teacher_profile)
  edit_profile_button.grid(row=2,column=0,padx=10,pady=15)

  #this button is used to logout
  logout_button=Button(frame1,text='Logout',font=('Helvetica',10),bg='RED',padx=10,pady=10,command=back_to_root)
  logout_button.grid(row=3,column=0,columnspan=2,pady=15)  
  root2.mainloop()


  #this is student function,this functions gives students to view their attendance,mark,and edit their profiln#this is student function,this functions gives students to view their attendance,mark,and edit their profile 
def root_3(): 
  global root3 
  root3=Tk() 
  root3.title("COLLEGE MANGEMENT SYSTEM") 
  root3.geometry('1080x720')
  root3.configure(bg='bisque')
  frame1=LabelFrame(root3,text='STUDENT PAGE',padx=100,pady=100,bg='gold2') 
  frame1.pack(padx=50,pady=50) 

  #this button does work of view_attedance function 
  view_attendance_button=Button(frame1,text='View Attendance',font=('Helvetica',10),padx=10,pady=10,command=view_attendance) 
  view_attendance_button.grid(row=0,column=0,padx=10,pady=15) 

  #this button does work of view_mark function 
  view_mark_button=Button(frame1,text='View Mark',font=('Helvetica',10),padx=10,pady=10,command=view_mark) 
  view_mark_button.grid(row=1,column=0,padx=10,pady=15) 

  #this button does work of edit_student_profile function 
  edit_profile_button=Button(frame1,text='Edit Your Profile',font=('Helvetica',10),padx=10,pady=10,comman=edit_student_profile) 
  edit_profile_button.grid(row=2,column=0,padx=10,pady=15) 

  #using this button,student can logout 
  logout_button=Button(frame1,text='Logout',font=('Helvetica',10),bg='RED',padx=10,pady=10,comman=back_to_root) 
  logout_button.grid(row=3,column=0,columnspan=2,pady=15) 
  root3.mainloop()

#create_teacher_account function is used to create student account
def create_student_account():
  branch1=str(branch.get())
  year1=int(year.get())
  rollno=str(create_student_rollno_entry.get())
  query="SELECT * FROM student WHERE ROLL_NO like '"+rollno+"' AND BRANCH = '"+branch1+"' AND YEAR ='"+str(year1)+"'"
  c.execute(query)
  result=c.fetchone()
  if str(type(result)) == "<class 'NoneType'>":
    passwd=str(create_student_passwd_entry.get())
    firstname=str(create_student_f_name_entry.get())
    lastname=str(create_student_l_name_entry.get())
    t=(branch1,year1,rollno,passwd,firstname,lastname)
    query="INSERT INTO student (BRANCH,YEAR,ROLL_NO,PASSWORD,F_NAME,L_NAME) VALUES(%s,%s,%s,%s,%s,%s)"
    c.execute(query,t)
    mydb.commit()
    response=created_popup()
    if response=='ok':
      root1_3.destroy()
      root_1()
  else:
    response=creation_error_popup()
    if response=='ok':
      root1_3.destroy()
      root_1()

#cancel_student_account is used to cancel creation of student account
def cancel_student_account():
  root1_3.destroy()
  root_1()








#create_teacher_account function is used to create teacher account
def create_teacher_account():
  username=str(create_teacher_username_entry.get())
  query="SELECT * FROM teacher WHERE USERNAME like '"+username+"'"
  c.execute(query)
  result=c.fetchone()
  if str(type(result)) == "<class 'NoneType'>":
    firstname=str(create_teacher_f_name_entry.get())
    lastname=str(create_teacher_l_name_entry.get())
    password=str(create_teacher_passwd_entry.get())
    t=(username,firstname,lastname,password)
    query="INSERT INTO TEACHER (USERNAME,F_NAME,L_NAME,PASSWORD) VALUES(%s,%s,%s,%s)"
    c.execute(query,t)
    mydb.commit()
    response=created_popup()
    if response=='ok':
      root1_2.destroy()
      root_1()
  else:
    response=creation_error_popup()
    if response=='ok':
      root1_2.destroy()
      root_1()

#cancel_teacher_account is used to cancel creation of teacher account
def cancel_teacher_account():
  root1_2.destroy()
  root_1()

    
    


#create_account function takes input from admin
def create_account():
  root1.destroy()
  if root1_clicked.get()=='TEACHER':
    global root1_2
    root1_2=Tk()
    root1_2.title("COLLEGE MANGEMENT SYSTEM")
    root1_2.geometry('1080x720')
    root1_2.configure(bg='bisque')
    frame1=LabelFrame(root1_2,text='CREATE TEACHER ACCOUNT',padx=100,pady=100,bg='gold2')
    frame1.pack(padx=50,pady=50)
    username_label=Label(frame1,text='Username/Email :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    password_label=Label(frame1,text='Password :',padx=10,pady=10)
    password_label.grid(row=1,column=0)
    f_name=Label(frame1,text='First Name :',padx=10,pady=10)
    f_name.grid(row=2,column=0)
    l_name=Label(frame1,text='Last Name :',padx=10,pady=10)
    l_name.grid(row=3,column=0)
    global create_teacher_username_entry
    create_teacher_username_entry=Entry(frame1,width=30,bd=2)
    create_teacher_username_entry.grid(row=0,column=1)
    global create_teacher_passwd_entry
    create_teacher_passwd_entry=Entry(frame1,width=30,bd=2)
    create_teacher_passwd_entry.grid(row=1,column=1)
    global create_teacher_f_name_entry
    create_teacher_f_name_entry=Entry(frame1,width=30,bd=2)
    create_teacher_f_name_entry.grid(row=2,column=1)
    global create_teacher_l_name_entry
    create_teacher_l_name_entry=Entry(frame1,width=30,bd=2)
    create_teacher_l_name_entry.grid(row=3,column=1)
    create_teacher_button=Button(frame1,text='Create',width=10,command=create_teacher_account)
    create_teacher_button.grid(row=4,column=0,pady=10)
    cancel_button=Button(frame1,text='Cancel',width=10,command=cancel_teacher_account)
    cancel_button.grid(row=4,column=1,pady=10)
    root1_2.mainloop()
  
  else:
    global root1_3
    root1_3=Tk()
    root1_3.title("COLLEGE MANGEMENT SYSTEM")
    root1_3.geometry('1080x720')
    root1_3.configure(bg='bisque')
    frame1=LabelFrame(root1_3,text='CREATE STUDENT ACCOUNT',padx=100,pady=100,bg='gold2')
    frame1.pack(padx=50,pady=50)
    branch_label=Label(frame1,text='Branch :',padx=10,pady=10)
    branch_label.grid(row=0,column=0)
    year_label=Label(frame1,text='Year :',padx=10,pady=10)
    year_label.grid(row=1,column=0)
    rollno_label=Label(frame1,text='Roll No :',padx=10,pady=10)
    rollno_label.grid(row=2,column=0)
    password_label=Label(frame1,text='Password :',padx=10,pady=10)
    password_label.grid(row=3,column=0)
    f_name=Label(frame1,text='First Name :',padx=10,pady=10)
    f_name.grid(row=4,column=0)
    l_name=Label(frame1,text='Last Name :',padx=10,pady=10)
    l_name.grid(row=5,column=0)
    global branch
    branch=StringVar()
    branch.set("C.S.E.")
    branch_option=OptionMenu(frame1,branch,"C.S.E.","I.T.","Civil","M.E.","Electrical","Electronics")
    branch_option.grid(row=0,column=1)
    global year
    year=StringVar()
    year.set("2")
    year_option=OptionMenu(frame1,year,"1","2","3","4")
    year_option.grid(row=1,column=1)
    global create_student_rollno_entry
    create_student_rollno_entry=Entry(frame1,width=30,bd=2)
    create_student_rollno_entry.grid(row=2,column=1)
    global create_student_passwd_entry
    create_student_passwd_entry=Entry(frame1,width=30,bd=2)
    create_student_passwd_entry.grid(row=3,column=1)
    global create_student_f_name_entry
    create_student_f_name_entry=Entry(frame1,width=30,bd=2)
    create_student_f_name_entry.grid(row=4,column=1)
    global create_student_l_name_entry
    create_student_l_name_entry=Entry(frame1,width=30,bd=2)
    create_student_l_name_entry.grid(row=5,column=1)
    create_student_button=Button(frame1,text='Create',width=10,command=create_student_account)
    create_student_button.grid(row=6,column=0,pady=10)
    cancel_button=Button(frame1,text='Cancel',width=10,command=cancel_student_account)
    cancel_button.grid(row=6,column=1,pady=10)
    root1_3.mainloop()
 





















#cancel_delete_student_account function is used to cancel deletion of student account
def cancel_delete_student_account():
  root1_7.destroy()
  root_1()

#delete_student_account1 function is used to delete account from database
def delete_student_account1():
  query="DELETE from student WHERE ROLL_NO like '"+delete_student_username+"'"
  c.execute(query)
  mydb.commit()
  response=deleted_popup()
  if response=='ok':
    root1_7.destroy()
    root_1()


#delete_student_account function is used to show of selected student's information and gives option to delete
def delete_student_account():
  global delete_student_username
  delete_student_username=str(delete_student_rollno_entry.get())
  #search query
  query="SELECT * FROM student WHERE ROLL_NO like '"+delete_student_username+"'"
  c.execute(query)
  result=c.fetchone()
  if str(type(result)) == "<class 'NoneType'>":
    not_found_popup()
  else:
    global root1_7
    root1_7.destroy()
    root1_7=Tk()
    root1_7.title("COLLEGE MANGEMENT SYSTEM")
    root1_7.geometry('1080x720')
    root1_7.configure(bg='bisque')
    global frame15
    frame15=LabelFrame(root1_7,text='DELETE STUDENT ACCOUNT',padx=100,pady=100,bg='gold2')
    frame15.pack(padx=50,pady=50)
    username_label=Label(frame15,text='Roll No :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    branch_label=Label(frame15,text='Branch :',padx=10,pady=10)
    branch_label.grid(row=1,column=0)
    year_label=Label(frame15,text='Year :',padx=10,pady=10)
    year_label.grid(row=2,column=0)  
    password_label=Label(frame15,text='Password :',padx=10,pady=10)
    password_label.grid(row=3,column=0)
    f_name=Label(frame15,text='First Name :',padx=10,pady=10)
    f_name.grid(row=4,column=0)
    l_name=Label(frame15,text='Last Name :',padx=10,pady=10)
    l_name.grid(row=5,column=0)
  
    username_label1=Label(frame15,text=delete_student_username,padx=10,pady=10)
    username_label1.grid(row=0,column=1)
    branch_label1=Label(frame15,text=result[0],padx=10,pady=10)
    branch_label1.grid(row=1,column=1)
    year_label1=Label(frame15,text=result[1],padx=10,pady=10)
    year_label1.grid(row=2,column=1)
    password_label1=Label(frame15,text=result[3],padx=10,pady=10)
    password_label1.grid(row=3,column=1)
    f_name1=Label(frame15,text=result[4],padx=10,pady=10)
    f_name1.grid(row=4,column=1)
    l_name1=Label(frame15,text=result[5],padx=10,pady=10)
    l_name1.grid(row=5,column=1)
    delete_teacher_button=Button(frame15,text='Delete',width=10,command=delete_student_account1)
    delete_teacher_button.grid(row=6,column=0,pady=10)
    cancel_button=Button(frame15,text='Cancel',width=10,command=cancel_delete_student_account)
    cancel_button.grid(row=6,column=1,pady=10)









#cancel_delete_teacher_account is used to cancel deletion of teacher account
def cancel_delete_teacher_account():
  root1_6.destroy()
  root_1()


#delete_teacher_account1 function is used to delete teacher account from database
def delete_teacher_account1():
  query="DELETE from teacher WHERE USERNAME like '"+delete_teacher_username+"'"
  c.execute(query)
  mydb.commit()
  response=deleted_popup()
  if response=='ok':
    root1_6.destroy()
    root_1()


#delete_teacher_Account function is used to show informations of selected teacher and it gives option to delete
def delete_teacher_account():
  global delete_teacher_username
  delete_teacher_username=str(delete_teacher_username_entry.get())  
  #search query
  query="SELECT F_NAME,L_NAME,PASSWORD FROM teacher WHERE USERNAME like '"+delete_teacher_username+"'"
  c.execute(query)
  result=c.fetchone()
  if str(type(result)) == "<class 'NoneType'>":
    not_found_popup()
  else:
    global root1_6
    root1_6.destroy()
    root1_6=Tk()
    root1_6.title("COLLEGE MANGEMENT SYSTEM")
    root1_6.geometry('1080x720')
    root1_6.configure(bg='bisque')
    global frame14
    frame14=LabelFrame(root1_6,text='DELETE TEACHER ACCOUNT',padx=100,pady=100,bg='gold2')
    frame14.pack(padx=50,pady=50)
    username_label=Label(frame14,text='Username/Email :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    username_label1=Label(frame14,text=delete_teacher_username,padx=10,pady=10)
    username_label1.grid(row=0,column=1)
    delete_teacher_passwd_label1=Label(frame14,text='Password :',bd=2)
    delete_teacher_passwd_label1.grid(row=1,column=0)
    delete_teacher_f_name_label1=Label(frame14,text='First Name :',bd=2)
    delete_teacher_f_name_label1.grid(row=2,column=0)
    delete_teacher_l_name_label1=Label(frame14,text='Last Name :',bd=2)
    delete_teacher_l_name_label1.grid(row=3,column=0)
    delete_teacher_passwd_label=Label(frame14,text=result[2],width=30,bd=2)
    delete_teacher_passwd_label.grid(row=1,column=1)
    delete_teacher_f_name_label=Label(frame14,text=result[0],width=30,bd=2)
    delete_teacher_f_name_label.grid(row=2,column=1)
    delete_teacher_l_name_label=Label(frame14,text=result[1],width=30,bd=2)
    delete_teacher_l_name_label.grid(row=3,column=1)
    delete_teacher_button=Button(frame14,text='Delete',width=10,command=delete_teacher_account1)
    delete_teacher_button.grid(row=4,column=0,pady=10)
    cancel_button=Button(frame14,text='Cancel',width=10,command=cancel_delete_teacher_account)
    cancel_button.grid(row=4,column=1,pady=10)








#delete_account function is used to take input teacher's username or student's rollno from admin to delete
def delete_account():
  root1.destroy()
  if root1_clicked2.get()=='TEACHER':
    global root1_6
    root1_6=Tk()
    root1_6.title("COLLEGE MANGEMENT SYSTEM")
    root1_6.geometry('1080x720')
    root1_6.configure(bg='bisque')
    global frame14
    frame14=LabelFrame(root1_6,text='DELETE TEACHER ACCOUNT',padx=100,pady=100,bg='gold2')
    frame14.pack(padx=50,pady=50)
    username_label=Label(frame14,text='Username/Email :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    global delete_teacher_username_entry
    delete_teacher_username_entry=Entry(frame14,width=30,bd=2)
    delete_teacher_username_entry.grid(row=0,column=1)
    search_button=Button(frame14,text='Search',command=delete_teacher_account)
    search_button.grid(row=1,column=0,pady=5)
    back_button=Button(frame14,text='Back',command=cancel_delete_teacher_account)
    back_button.grid(row=1,column=1,pady=5)
    delete_teacher_username=str(delete_teacher_username_entry.get())
    root1_6.mainloop()
  else:
    global root1_7
    root1_7=Tk()
    root1_7.title("COLLEGE MANGEMENT SYSTEM")
    root1_7.geometry('1080x720')
    root1_7.configure(bg='bisque')
    global frame15
    frame15=LabelFrame(root1_7,text='DELETE STUDENT ACCOUNT',padx=100,pady=100,bg='gold2')
    frame15.pack(padx=50,pady=50)
    username_label=Label(frame15,text='Roll No :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    global delete_student_rollno_entry
    delete_student_rollno_entry=Entry(frame15,width=30,bd=2)
    delete_student_rollno_entry.grid(row=0,column=1)
    search_button=Button(frame15,text='Search',pady=5,command=delete_student_account)
    search_button.grid(row=1,column=0,pady=5)
    back_button=Button(frame15,text='Back',command=cancel_delete_student_account)
    back_button.grid(row=1,column=1,pady=5)

    root1_7.mainloop()






#edit_student_account1 function is used to edit student's informations into database
def edit_student_account1():
  query="UPDATE student SET BRANCH='"+str(branch1.get())+"',YEAR='"+str(year1.get())+"',F_NAME='"+str(edit_student_f_name_entry.get())+"',L_NAME='"+str(edit_student_l_name_entry.get())+"',PASSWORD='"+str(edit_student_passwd_entry.get())+"' WHERE ROLL_NO = '"+student_username+"'"
  c.execute(query)
  mydb.commit()
  response=edited_popup()
  if response=='ok':
    root1_5.destroy()
    root_1()

    
#cancel_edit_student_account is used to cancel editing of student account
def cancel_edit_student_account():
  root1_5.destroy()
  root_1()


#edit_student_account function is used to take information which admin wants to edit
def edit_student_account():
  global student_username
  student_username=str(edit_student_rollno_entry.get())
  #search query
  query="SELECT * FROM student WHERE ROLL_NO like '"+student_username+"'"
  c.execute(query)
  result=c.fetchone()
  if str(type(result)) == "<class 'NoneType'>":
    not_found_popup()
  else:
    global root1_5
    root1_5.destroy()
    root1_5=Tk()
    root1_5.title("COLLEGE MANGEMENT SYSTEM")
    root1_5.geometry('1080x720')
    root1_5.configure(bg='bisque')
    global frame13
    frame13=LabelFrame(root1_5,text='EDIT STUDENT ACCOUNT',padx=100,pady=100,bg='gold2')
    frame13.pack(padx=50,pady=50)
    username_label=Label(frame13,text='Roll No :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    username_label1=Label(frame13,text=student_username,padx=10,pady=10)
    username_label1.grid(row=0,column=1)

    branch_label=Label(frame13,text='Branch :',padx=10,pady=10)
    branch_label.grid(row=1,column=0)
    year_label=Label(frame13,text='Year :',padx=10,pady=10)
    year_label.grid(row=2,column=0)  
    password_label=Label(frame13,text='Password :',padx=10,pady=10)
    password_label.grid(row=3,column=0)
    f_name=Label(frame13,text='First Name :',padx=10,pady=10)
    f_name.grid(row=4,column=0)
    l_name=Label(frame13,text='Last Name :',padx=10,pady=10)
    l_name.grid(row=5,column=0)
    global branch1
    branch1=StringVar()
    branch1.set(result[0])
    branch_option=OptionMenu(frame13,branch1,"C.S.E.","I.T.","Civil","M.E.","Electrical","Electronics")
    branch_option.grid(row=1,column=1)
    global year1
    year1=StringVar()
    year1.set(result[1])
    year_option=OptionMenu(frame13,year1,"1","2","3","4")
    year_option.grid(row=2,column=1)
    global edit_student_passwd_entry
    edit_student_passwd_entry=Entry(frame13,width=30,bd=2)
    edit_student_passwd_entry.grid(row=3,column=1)
    edit_student_passwd_entry.insert(0,result[3])
    global edit_student_f_name_entry
    edit_student_f_name_entry=Entry(frame13,width=30,bd=2)
    edit_student_f_name_entry.grid(row=4,column=1)
    edit_student_f_name_entry.insert(0,result[4])
    global edit_student_l_name_entry
    edit_student_l_name_entry=Entry(frame13,width=30,bd=2)
    edit_student_l_name_entry.grid(row=5,column=1)
    edit_student_l_name_entry.insert(0,result[5])
    edit_student_button=Button(frame13,text='Edit',width=10,command=edit_student_account1)
    edit_student_button.grid(row=6,column=0,pady=10)
    cancel_button=Button(frame13,text='Cancel',width=10,command=cancel_edit_student_account)
    cancel_button.grid(row=6,column=1,pady=10)













#cancel_edit_teacher_account is used to cancel editing of teacher account
def cancel_edit_teacher_account():
  root1_4.destroy()
  root_1()


#edit_teacher_account1 function is used to edit teacher's informations into database
def edit_teacher_account1():
  global teacher_username
  query="UPDATE teacher SET F_NAME='"+str(edit_teacher_f_name_entry.get())+"',L_NAME='"+str(edit_teacher_l_name_entry.get())+"',PASSWORD='"+str(edit_teacher_passwd_entry.get())+"' WHERE USERNAME = '"+teacher_username+"'"
  c.execute(query)
  mydb.commit()
  response=edited_popup()
  if response=='ok':
    root1_4.destroy()
    root_1()


#edit_teacher_account function is used to take input informations which admin wants to edit
def edit_teacher_account():
  global root1_4
  global teacher_username
  teacher_username=str(edit_teacher_username_entry.get())
  #search query
  query="SELECT F_NAME,L_NAME,PASSWORD FROM teacher WHERE USERNAME like '"+teacher_username+"'"
  c.execute(query)
  result=c.fetchone()
  if str(type(result)) == "<class 'NoneType'>":
    not_found_popup()
  else:
    root1_4.destroy()
    root1_4=Tk()
    root1_4.title("COLLEGE MANGEMENT SYSTEM")
    root1_4.geometry('1080x720')
    root1_4.configure(bg='bisque')
    global frame12
    frame12=LabelFrame(root1_4,text='EDIT TEACHER ACCOUNT',padx=100,pady=100,bg='gold2')
    frame12.pack(padx=50,pady=50)
    username_label=Label(frame12,text='Username/Email :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    username_label1=Label(frame12,text=teacher_username,padx=10,pady=10)
    username_label1.grid(row=0,column=1)
    password_label=Label(frame12,text='Password :',padx=10,pady=10)
    password_label.grid(row=1,column=0)
    f_name=Label(frame12,text='First Name :',padx=10,pady=10)
    f_name.grid(row=2,column=0)
    l_name=Label(frame12,text='Last Name :',padx=10,pady=10)
    l_name.grid(row=3,column=0)
    global edit_teacher_passwd_entry
    edit_teacher_passwd_entry=Entry(frame12,width=30,bd=2)
    edit_teacher_passwd_entry.grid(row=1,column=1)
    edit_teacher_passwd_entry.insert(0,result[2])
    global edit_teacher_f_name_entry
    edit_teacher_f_name_entry=Entry(frame12,width=30,bd=2)
    edit_teacher_f_name_entry.grid(row=2,column=1)
    edit_teacher_f_name_entry.insert(0,result[0])
    global edit_teacher_l_name_entry
    edit_teacher_l_name_entry=Entry(frame12,width=30,bd=2)
    edit_teacher_l_name_entry.grid(row=3,column=1)
    edit_teacher_l_name_entry.insert(0,result[1])
    edit_teacher_button=Button(frame12,text='Edit',width=10,command=edit_teacher_account1)
    edit_teacher_button.grid(row=4,column=0,pady=10)
    cancel_button=Button(frame12,text='Cancel',width=10,command=cancel_edit_teacher_account)
    cancel_button.grid(row=4,column=1,pady=10)









#edit_account function is used to take input student's roll no or teacher's username from admin to edit
def edit_account():
  root1.destroy()
  if root1_clicked1.get()=='TEACHER':
    global root1_4
    root1_4=Tk()
    root1_4.title("COLLEGE MANGEMENT SYSTEM")
    root1_4.geometry('1080x720')
    root1_4.configure(bg='bisque')
    global frame12
    frame12=LabelFrame(root1_4,text='EDIT TEACHER ACCOUNT',padx=100,pady=100,bg='gold2')
    frame12.pack(padx=50,pady=50)
    username_label=Label(frame12,text='Username/Email :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    global edit_teacher_username_entry
    edit_teacher_username_entry=Entry(frame12,width=30,bd=2)
    edit_teacher_username_entry.grid(row=0,column=1)
    search_button=Button(frame12,text='Search',command=edit_teacher_account)
    search_button.grid(row=1,column=0,pady=5)
    back_button=Button(frame12,text='Back',command=cancel_edit_teacher_account)
    back_button.grid(row=1,column=1,pady=5)
    root1_4.mainloop()
  else:
    global root1_5
    root1_5=Tk()
    root1_5.title("COLLEGE MANGEMENT SYSTEM")
    root1_5.geometry('1080x720')
    root1_5.configure(bg='bisque')
    global frame13
    frame13=LabelFrame(root1_5,text='EDIT STUDENT ACCOUNT',padx=100,pady=100,bg='gold2')
    frame13.pack(padx=50,pady=50)
    username_label=Label(frame13,text='Roll No :',padx=10,pady=10)
    username_label.grid(row=0,column=0)
    global edit_student_rollno_entry
    edit_student_rollno_entry=Entry(frame13,width=30,bd=2)
    edit_student_rollno_entry.grid(row=0,column=1)
    search_button=Button(frame13,text='Search',command=edit_student_account)
    search_button.grid(row=1,column=0)
    back_button=Button(frame13,text='Back',command=cancel_edit_student_account)
    back_button.grid(row=1,column=1)
    root1_5.mainloop()








    #back_to_root function is used to logout 
def back_to_root():
  root1.destroy()
  root_()





#cancel_admin function is used to cancel editing of admin's information
def cancel_admin():
  root1_1.destroy()
  root_1()


#edit1_admin function is used to edit admin's informations into database
def edit1_admin():
  user_name=str(username_entry.get())
  pass_word=str(passwd_entry.get())
  t=(user_name,pass_word)
  query='DELETE FROM ADMIN'
  c.execute(query)
  query="INSERT INTO ADMIN(USER,PASSWORD) VALUES (%s,%s)"
  c.execute(query,t)
  mydb.commit()
  response=edited_popup()
  if response=='ok':
    root1_1.destroy()
    root_1()



#edit_admin function is used to take input informations
def edit_admin():
  root1.destroy()
  global root1_1
  root1_1=Tk()
  root1_1.title("COLLEGE MANGEMENT SYSTEM")
  root1_1.geometry('1080x720')
  root1_1.configure(bg='bisque') 
  query='SELECT * FROM ADMIN '
  c.execute(query)
  result=c.fetchall()
  frame1=LabelFrame(root1_1,text='EDIT YOUR PROFILE',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
  username_label=Label(frame1,text='Username :',padx=10,pady=10)
  username_label.grid(row=0,column=0)
  password_label=Label(frame1,text='Password :',padx=10,pady=10)
  password_label.grid(row=1,column=0)
  global username_entry
  username_entry=Entry(frame1,width=30,bd=2)
  username_entry.grid(row=0,column=1)
  username_entry.insert(0,result[0][0])
  global passwd_entry
  passwd_entry=Entry(frame1,width=30,bd=2)
  passwd_entry.grid(row=1,column=1)
  passwd_entry.insert(0,result[0][1])
  edit_admin_button=Button(frame1,text='Edit',width=10,command=edit1_admin)
  edit_admin_button.grid(row=2,column=0,pady=10)
  cancel_button=Button(frame1,text='Cancel',width=10,command=cancel_admin)
  cancel_button.grid(row=2,column=1,pady=10)
  root1_1.mainloop()








#edit_student_profile_account1 function is used to edit the data in database
def edit_student_profile_account1():
  global student_passwd
  student_passwd= str(edit_student_profile_passwd_entry.get())
  query="UPDATE student SET BRANCH='"+str(edit_branch.get())+"',YEAR='"+str(edit_year.get())+"',F_NAME='"+str(edit_student_profile_f_name_entry.get())+"',L_NAME='"+str(edit_student_profile_l_name_entry.get())+"',PASSWORD='"+str(edit_student_profile_passwd_entry.get())+"' WHERE ROLL_NO='"+student_user+"'"
  c.execute(query)
  mydb.commit()
  response=edited_popup()
  if response=='ok':
    root3_1.destroy()
    root_3()


#edit_student_profile function takes edited data from student to edit his profile
def edit_student_profile():
  root3.destroy()
  global student_passwd
  global root3_1
  root3_1=Tk()
  root3_1.title("COLLEGE MANGEMENT SYSTEM")
  root3_1.geometry('1080x720')
  root3_1.configure(bg='bisque') 
  frame1=LabelFrame(root3_1,text='EDIT YOUR PROFILE',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
  
  username_label=Label(frame1,text='Username/Roll No :',padx=10,pady=10)
  username_label.grid(row=0,column=0)
  username_label1=Label(frame1,text=student_user,padx=10,pady=10)
  username_label1.grid(row=0,column=1)
  branch_label=Label(frame1,text='Branch :',padx=10,pady=10)
  branch_label.grid(row=1,column=0)
  year_label=Label(frame1,text='Year :',padx=10,pady=10)
  year_label.grid(row=2,column=0)  
  password_label=Label(frame1,text='Password :',padx=10,pady=10)
  password_label.grid(row=3,column=0)
  f_name=Label(frame1,text='First Name :',padx=10,pady=10)
  f_name.grid(row=4,column=0)
  l_name=Label(frame1,text='Last Name :',padx=10,pady=10)
  l_name.grid(row=5,column=0)
  #search query
  query="SELECT * FROM student WHERE ROLL_NO like '"+student_user+"' AND PASSWORD ='"+student_passwd+"'"
  c.execute(query)
  result=c.fetchone()
  global edit_branch
  edit_branch=StringVar()
  edit_branch.set(result[0])
  branch_option=OptionMenu(frame1,edit_branch,"C.S.E.","I.T.","Civil","M.E.","Electrical","Electronics")
  branch_option.grid(row=1,column=1)
  global edit_year
  edit_year=StringVar()
  edit_year.set(result[1])
  year_option=OptionMenu(frame1,edit_year,"1","2","3","4")
  year_option.grid(row=2,column=1)
  global edit_student_profile_passwd_entry
  edit_student_profile_passwd_entry=Entry(frame1,width=30,bd=2)
  edit_student_profile_passwd_entry.grid(row=3,column=1)
  edit_student_profile_passwd_entry.insert(0,result[3])
  global edit_student_profile_f_name_entry
  edit_student_profile_f_name_entry=Entry(frame1,width=30,bd=2)
  edit_student_profile_f_name_entry.grid(row=4,column=1)
  edit_student_profile_f_name_entry.insert(0,result[4])
  global edit_student_profile_l_name_entry
  edit_student_profile_l_name_entry=Entry(frame1,width=30,bd=2)
  edit_student_profile_l_name_entry.grid(row=5,column=1)
  edit_student_profile_l_name_entry.insert(0,result[5])
  edit_student_button=Button(frame1,text='Edit',width=10,command=edit_student_profile_account1)
  edit_student_button.grid(row=6,column=0,pady=10)
  cancel_button=Button(frame1,text='Cancel',width=10,command=back_to_root3)
  cancel_button.grid(row=6,column=1,pady=10)

  root3_1.mainloop()










#back_to_root2 function is used to got out from view_attendance page
def back_to_root3():
  root3_1.destroy()
  root_3()



#view_attendance function is used to view attendance of student who is login 
def view_attendance():
  root3.destroy()
  global root3_1
  root3_1=Tk()
  root3_1.title("COLLEGE MANGEMENT SYSTEM")
  root3_1.geometry('1080x720')
  root3_1.configure(bg='bisque')
  frame1=LabelFrame(root3_1,text='VIEW ATTENDANCE',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
  
  #search_query
  query="SELECT ATTENDANCE,TOTAL_ATTENDANCE,ATTENDANCE_PERCENTAGE FROM student WHERE ROLL_NO like '"+student_user+"' AND PASSWORD ='"+student_passwd+"'"
  c.execute(query)
  result=c.fetchone()

  attendance_label=Label(frame1,text='Attendance :',padx=10,pady=10)
  attendance_label.grid(row=0,column=0)
  total_attendance_label=Label(frame1,text='Total Attendance :',padx=10,pady=10)
  total_attendance_label.grid(row=1,column=0)
  attendance_percentage_label=Label(frame1,text='Attendance Percentage :',padx=10,pady=10)
  attendance_percentage_label.grid(row=2,column=0)
  
  attendance_label1=Label(frame1,text=result[0],padx=10,pady=10)
  attendance_label1.grid(row=0,column=1)
  total_attendance_label1=Label(frame1,text=result[1],padx=10,pady=10)
  total_attendance_label1.grid(row=1,column=1)
  attendance_percentage_label1=Label(frame1,text=result[2],padx=10,pady=10)
  attendance_percentage_label1.grid(row=2,column=1)

  back_button=Button(frame1,text='Back',width=10,command=back_to_root3)
  back_button.grid(row=3,column=0,pady=10,columnspan=2)
  
  root3_1.mainloop()









#view_mark1 function selects data from database and puts the data on screen 
def view_mark1():
  query="SELECT "+str(view_mark_exam.get())+" from student WHERE ROLL_NO like '"+student_user+"' AND PASSWORD ='"+student_passwd+"'"
  c.execute(query)
  result=c.fetchone()

  global root3_1
  root3_1.destroy()
  root3_1=Tk()
  root3_1.title("COLLEGE MANGEMENT SYSTEM")
  root3_1.geometry('1080x720')
  root3_1.configure(bg='bisque')  
  frame1=LabelFrame(root3_1,text='VIEW MARK',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
   
  exam_label=Label(frame1,text='Exam :',padx=10,pady=10)
  exam_label.grid(row=0,column=0)

  exam_label1=Label(frame1,text=view_mark_exam.get(),padx=10,pady=10)
  exam_label1.grid(row=0,column=1)
   

  mark_label=Label(frame1,text='Mark :',padx=10,pady=10)
  mark_label.grid(row=1,column=0)

  mark_label1=Label(frame1,text=result[0],padx=10,pady=10)
  mark_label1.grid(row=1,column=1)

  back_button=Button(frame1,text='Back',width=10,command=back_to_root3)
  back_button.grid(row=2,column=0,pady=10,columnspan=2)

  root3_1.mainloop()



#view_mark function is used to select the exam from ("SGPA(Sem-1)","SGPA(Sem-2)","CertificationNo.","FINAL_INTERNAL") 
def view_mark():
  root3.destroy()
  global root3_1
  root3_1=Tk()
  root3_1.title("COLLEGE MANGEMENT SYSTEM")
  root3_1.geometry('1080x720')
  root3_1.configure(bg='bisque') 
  frame1=LabelFrame(root3_1,text='VIEW MARK',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
   
  exam_label=Label(frame1,text='Exam :',padx=10,pady=10)
  exam_label.grid(row=0,column=0)

  global view_mark_exam
  view_mark_exam=StringVar()
  view_mark_exam.set('SELECT EXAM')
  exam_option=OptionMenu(frame1,view_mark_exam,"SGPA(Sem-1)","SGPA(Sem-2)","CertificationNo.","FINAL_INTERNAL")
  exam_option.grid(row=0,column=1)
  

  search_button=Button(frame1,text='Search',command=view_mark1)
  search_button.grid(row=1,column=0,columnspan=2)

  
  root3_1.mainloop()









#back_to_root2 function is used to back on teacher page
def back_to_root2():
  root2_1.destroy()
  root_2()



#add_student_attendance function is used to add attendance in databases
def add_student_attendance():
  query="SELECT ROLL_NO,F_NAME,L_NAME FROM student WHERE BRANCH like '"+str(attendance_branch.get())+"' AND YEAR ='"+str(attendance_year.get())+"'"
  c.execute(query)
  result=c.fetchall()
  result=list(result)
  result.sort(key = lambda x: x[0])

  for x in range(len(attendance_list)):
    query="SELECT ATTENDANCE,TOTAL_ATTENDANCE FROM student WHERE ROLL_NO like '"+result[x][0]+"'"
    c.execute(query)
    result1=c.fetchone()
    if str(type(result1[0]))=="<class 'NoneType'>":
      a=0
    else:
      a=result1[0]
    if str(type(result1[1]))=="<class 'NoneType'>":
      t=0  
    else:
      t=result1[1]
    query="UPDATE student SET ATTENDANCE='"+str(int(attendance_list[x].get())+a)+"',TOTAL_ATTENDANCE='"+str(t+1)+"',ATTENDANCE_PERCENTAGE='"+str(((int(attendance_list[x].get())+a)/(t+1))*100)+"' WHERE ROLL_NO like '"+result[x][0]+"'"
    c.execute(query)
    mydb.commit()
  response=added_popup()
  if response=='ok':
    back_to_root2()



#add_attendance1 function is used to take attendance of students of selected branch and year
def add_attendance1():
  query="SELECT ROLL_NO,F_NAME,L_NAME FROM student WHERE BRANCH like '"+str(attendance_branch.get())+"' AND YEAR ='"+str(attendance_year.get())+"'"
  c.execute(query)
  result=c.fetchall()
  result=list(result)
  result.sort(key = lambda x: x[0])
  global attendance_list
  attendance_list=[]
  for x in range(0,len(result)):
    attendance_list.append(str('var'+str(x)))
  global root2_1
  root2_1.destroy()
  root2_1=Tk()
  root2_1.title("COLLEGE MANGEMENT SYSTEM")
  root2_1.geometry('1080x720')
  root2_1.configure(bg='bisque')  
  frame1=LabelFrame(root2_1,text='ADD ATTENDANCE',padx=100,pady=100)
  frame1.pack(padx=50,pady=50)
  branch_label=Label(frame1,text='Branch :',padx=10,pady=10)
  branch_label.grid(row=0,column=0,columnspan=2)
  year_label=Label(frame1,text='Year :',padx=10,pady=10)
  year_label.grid(row=1,column=0,columnspan=2)
  branch_label1=Label(frame1,text=str(attendance_branch.get()),padx=5,pady=5)
  branch_label1.grid(row=0,column=2)
  year_label1=Label(frame1,text=str(attendance_year.get()),padx=5,pady=5)
  year_label1.grid(row=1,column=2)
  rollno_label=Label(frame1,text='Roll No',padx=10,pady=10)
  rollno_label.grid(row=2,column=0)
  name_label=Label(frame1,text='Name',padx=10,pady=10)
  name_label.grid(row=2,column=1)
  attendance_label=Label(frame1,text='Attendance',padx=10,pady=10)
  attendance_label.grid(row=2,column=2,columnspan=3)
  count1=0
  count=3
  for item in result:
    temp_rollno_label=Label(frame1,text=item[0],padx=10,pady=10)
    temp_rollno_label.grid(row=count,column=0)
    temp_name_label=Label(frame1,text=str(item[1]+' '+item[2]),padx=10,pady=10)
    temp_name_label.grid(row=count,column=1)
    attendance_list[count1]=IntVar()
    attendance_list[count1].set('1')
    Radiobutton(frame1,text='Present',variable=attendance_list[count1],value=1).grid(row=count,column=2)
    Radiobutton(frame1,text='Absent',variable=attendance_list[count1],value=0).grid(row=count,column=3)
    count+=1
    count1+=1


  add_student_attendance_button=Button(frame1,text='Add',width=10,command=add_student_attendance)
  add_student_attendance_button.grid(row=count,column=0,pady=10,columnspan=2)
  cancel_button=Button(frame1,text='Cancel',width=10,command=back_to_root2)
  cancel_button.grid(row=count,column=2,columnspan=3,pady=10)





#add_attendance function is used to search student names of selected branch and year
def add_attendance():
  root2.destroy()
  global root2_1
  root2_1=Tk()
  root2_1.title("COLLEGE MANGEMENT SYSTEM")
  root2_1.geometry('1080x720')
  root2_1.configure(bg='bisque')  
  frame1=LabelFrame(root2_1,text='ADD ATTENDANCE',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
  branch_label=Label(frame1,text='Branch :',padx=10,pady=10)
  branch_label.grid(row=0,column=0)
  year_label=Label(frame1,text='Year :',padx=10,pady=10)
  year_label.grid(row=1,column=0)
  global attendance_branch
  attendance_branch=StringVar()
  attendance_branch.set('SELECT BRANCH')
  branch_option=OptionMenu(frame1,attendance_branch,"C.S.E.","I.T.","Civil","M.E.","Electrical","Electronics")
  branch_option.grid(row=0,column=1)
  global attendance_year
  attendance_year=StringVar()
  attendance_year.set('SELECT YEAR')
  attendance_option=OptionMenu(frame1,attendance_year,"1","2","3","4")
  attendance_option.grid(row=1,column=1)

  search_button=Button(frame1,text='Search',command=add_attendance1)
  search_button.grid(row=2,column=0,columnspan=2)

  root2_1.mainloop()








 

#add_student_mark function is used to add mark in databases
def add_student_mark():
  query="SELECT ROLL_NO,F_NAME,L_NAME FROM student WHERE BRANCH like '"+str(mark_branch.get())+"' AND YEAR ='"+str(mark_year.get())+"'"
  c.execute(query)
  result=c.fetchall()
  result=list(result)
  result.sort(key = lambda x: x[0])
  
  for x in range(len(mark_list)):
    query="UPDATE student SET "+str(mark_exam.get())+"='"+str(mark_list[x].get())+"' WHERE ROLL_NO like '"+result[x][0]+"'"
    c.execute(query)
    mydb.commit()
  response=added_popup()
  if response=='ok':  
    back_to_root2()


#add_mark1 function is used to take input mark of students of selected branch and year
def add_mark1():
  query="SELECT ROLL_NO,F_NAME,L_NAME FROM student WHERE BRANCH like '"+str(mark_branch.get())+"' AND YEAR ='"+str(mark_year.get())+"'"
  c.execute(query)
  result=c.fetchall()
  result=list(result)
  result.sort(key = lambda x: x[0])
  global mark_list
  mark_list=[]
  for x in range(0,len(result)):
    mark_list.append(str('var'+str(x)))
  global root2_1
  root2_1.destroy()
  root2_1=Tk()
  root2_1.title("COLLEGE MANGEMENT SYSTEM")
  root2_1.geometry('1080x720')
  root2_1.configure(bg='bisque') 
  frame1=LabelFrame(root2_1,text='ADD MARK',padx=100,pady=100)
  frame1.pack(padx=50,pady=50)
  branch_label=Label(frame1,text='Branch :',padx=20,pady=20)
  branch_label.grid(row=0,column=0,columnspan=2)
  year_label=Label(frame1,text='Year :',padx=20,pady=20)
  year_label.grid(row=1,column=0,columnspan=2)
  exam_label=Label(frame1,text='Exam :',padx=10,pady=10)
  exam_label.grid(row=2,column=0,columnspan=2)
  branch_label1=Label(frame1,text=str(mark_branch.get()),padx=10,pady=10)
  branch_label1.grid(row=0,column=2)
  year_label1=Label(frame1,text=str(mark_year.get()),padx=10,pady=10)
  year_label1.grid(row=1,column=2)
  exam_label1=Label(frame1,text=str(mark_exam.get()),padx=10,pady=10)
  exam_label1.grid(row=2,column=2)
  rollno_label=Label(frame1,text='Roll No',padx=10,pady=10)
  rollno_label.grid(row=3,column=0)
  name_label=Label(frame1,text='Name',padx=10,pady=10)
  name_label.grid(row=3,column=1)
  attendance_label=Label(frame1,text='Mark',padx=10,pady=10)
  attendance_label.grid(row=3,column=2,columnspan=3)
  count1=0
  count=4
  for item in result:
    temp_rollno_label=Label(frame1,text=item[0],padx=10,pady=10)
    temp_rollno_label.grid(row=count,column=0)
    temp_name_label=Label(frame1,text=str(item[1]+' '+item[2]),padx=10,pady=10)
    temp_name_label.grid(row=count,column=1)
    mark_list[count1]=Entry(frame1,width=10)
    mark_list[count1].grid(row=count,column=2)
    count+=1
    count1+=1


  add_student_mark_button=Button(frame1,text='Add',width=10,command=add_student_mark)
  add_student_mark_button.grid(row=count,column=0,pady=10,columnspan=2)
  cancel_button=Button(frame1,text='Cancel',width=10,command=back_to_root2)
  cancel_button.grid(row=count,column=2,columnspan=3,pady=10)
  

  root2_1.mainloop()





#add_mark function is used to search student names of selected branch , year and exam
def add_mark():
  root2.destroy()
  global root2_1
  root2_1=Tk()
  root2_1.title("COLLEGE MANGEMENT SYSTEM")
  root2_1.geometry('1080x720')
  root2_1.configure(bg='bisque') 
  frame1=LabelFrame(root2_1,text='ADD MARK',padx=100,pady=100)
  frame1.pack(padx=50,pady=50)
  branch_label=Label(frame1,text='Branch :',padx=10,pady=10)
  branch_label.grid(row=0,column=0)
  year_label=Label(frame1,text='Year :',padx=10,pady=10)
  year_label.grid(row=1,column=0)
  exam_label=Label(frame1,text='Exam :',padx=10,pady=10)
  exam_label.grid(row=2,column=0)
  global mark_branch
  mark_branch=StringVar()
  mark_branch.set('SELECT BRANCH')
  branch_option=OptionMenu(frame1,mark_branch,"C.S.E.","I.T.","Civil","M.E.","Electrical","Electronics")
  branch_option.grid(row=0,column=1)
  
  global mark_year
  mark_year=StringVar()
  mark_year.set('SELECT YEAR')
  year_option=OptionMenu(frame1,mark_year,"1","2","3","4")
  year_option.grid(row=1,column=1)

  global mark_exam
  mark_exam=StringVar()
  mark_exam.set('SELECT EXAM')
  exam_option=OptionMenu(frame1,mark_exam,"SGPA(Sem-1)","SGPA(Sem-2)","CertificationNo.","FINAL_INTERNAL")
  exam_option.grid(row=2,column=1)

  search_button=Button(frame1,text='Search',command=add_mark1)
  search_button.grid(row=3,column=0,columnspan=2)

  root2_1.mainloop()








  #edit_teacher_profile1 function is used to save edited data into database
def edit_teacher_profile_account1():
  global passwd
  passwd=str(edit_teacher_profile_passwd_entry.get())
  query="UPDATE teacher SET F_NAME='"+str(edit_teacher_profile_f_name_entry.get())+"',L_NAME='"+str(edit_teacher_profile_l_name_entry.get())+"',PASSWORD='"+str(edit_teacher_profile_passwd_entry.get())+"' WHERE USERNAME = '"+user+"'"
  c.execute(query)
  mydb.commit()
  response=edited_popup()
  if response=='ok':
    root2_1.destroy()
    root_2()


#edit_teacher_profile function is used to take input edited data
def edit_teacher_profile():
  root2.destroy()
  global root2_1
  root2_1=Tk()
  root2_1.title("COLLEGE MANGEMENT SYSTEM")
  root2_1.geometry('1080x720')
  root2_1.configure(bg='bisque')  
  frame1=LabelFrame(root2_1,text='EDIT YOUR PROFILE',padx=100,pady=100,bg='gold2')
  frame1.pack(padx=50,pady=50)
  #search query
  query="SELECT * FROM teacher WHERE USERNAME like '"+user+"' AND PASSWORD ='"+passwd+"'"
  c.execute(query)
  result=c.fetchone()

  username_label=Label(frame1,text='Username/Email :',padx=10,pady=10)
  username_label.grid(row=0,column=0)
  username_label1=Label(frame1,text=result[0],padx=10,pady=10)
  username_label1.grid(row=0,column=1)

  password_label=Label(frame1,text='Password :',padx=10,pady=10)
  password_label.grid(row=1,column=0)
  f_name=Label(frame1,text='First Name :',padx=10,pady=10)
  f_name.grid(row=2,column=0)
  l_name=Label(frame1,text='Last Name :',padx=10,pady=10)
  l_name.grid(row=3,column=0)

  global edit_teacher_profile_passwd_entry
  edit_teacher_profile_passwd_entry=Entry(frame1,width=30,bd=2)
  edit_teacher_profile_passwd_entry.grid(row=1,column=1)
  edit_teacher_profile_passwd_entry.insert(0,result[3])
  global edit_teacher_profile_f_name_entry
  edit_teacher_profile_f_name_entry=Entry(frame1,width=30,bd=2)
  edit_teacher_profile_f_name_entry.grid(row=2,column=1)
  edit_teacher_profile_f_name_entry.insert(0,result[1])
  global edit_teacher_profile_l_name_entry
  edit_teacher_profile_l_name_entry=Entry(frame1,width=30,bd=2)
  edit_teacher_profile_l_name_entry.grid(row=3,column=1)
  edit_teacher_profile_l_name_entry.insert(0,result[2])
  edit_teacher_button=Button(frame1,text='Edit',width=10,command=edit_teacher_profile_account1)
  edit_teacher_button.grid(row=4,column=0,pady=10)
  cancel_button=Button(frame1,text='Cancel',width=10,command=back_to_root2)
  cancel_button.grid(row=4,column=1,pady=10)






#added_popup function gives message to user that given information is added to databases
def added_popup():
  response=messagebox.showinfo("MESSAGE","Added")
  return response

#deleted_popup function gives message to user that given information is deleted from databases
def deleted_popup():
  response=messagebox.showwarning("WARNING","Deleted")
  return response

#created_popup function gives message to user that account is created and related given information is added to databases
def created_popup():
  response=messagebox.showinfo("MESSAGE","Created")
  return response

#edited_popup function gives message to user that given information is edited to related account to databases
def edited_popup():
  response=messagebox.showinfo("MESSAGE","Edited")
  return response

#creation_error_popup function gives message to user that given information has been already added to databases
def creation_error_popup():
  response=messagebox.showwarning("WARNING","THIS USERNAME ALREADY HAS BEEN ADDED")
  return response

#not_found_popup function gives message to user that given information is found in databases
def not_found_popup():
  response=messagebox.showwarning("WARNING","THIS ACCOUNT IS NOT FOUND")
  return response

#login_popup function gives message to user that given login information is not correct according to databases
def login_popup():
  messagebox.showwarning("WARNING","Either Username or Password is wrong")





















#login_function used to login as admin,teacher,student.It collects the login information and match with database and if it is right then it allow to login 
def login():
    if root_clicked.get()=='ADMIN':
        query='SELECT * FROM ADMIN '
        c.execute(query)
        result=c.fetchall()
        mark=1
        for x in result:
             if x[0]==str(user_entry.get()) and x[1]==str(password_entry.get()):
                 mark=1
             else:
                mark=0
        if mark==1:
           root.destroy()
           root_1()
        else:
          login_popup()
    elif root_clicked.get()=='TEACHER':
        query="SELECT * FROM teacher WHERE USERNAME like '"+str(user_entry.get())+"' AND PASSWORD ='"+str(password_entry.get())+"'"
        c.execute(query)
        result=c.fetchone()
        if str(type(result))== "<class 'NoneType'>":
          login_popup()
        else:
          global user
          global passwd
          user=str(user_entry.get())
          passwd=str(password_entry.get())
          root.destroy()
          root_2()
    else:
        query="SELECT * FROM student WHERE ROLL_NO like '"+str(user_entry.get())+"' AND PASSWORD ='"+str(password_entry.get())+"'"
        c.execute(query)
        result=c.fetchone()
        if str(type(result))== "<class 'NoneType'>":
          login_popup()
        else:
          global student_user
          global student_passwd
          student_user=str(user_entry.get())
          student_passwd=str(password_entry.get())
          root.destroy()
          root_3()


def delete():
    myentry.delete(1)
            
            
#show function is used to show or hide password from other user
def show():
  global string
  global password_entry
  global show_method
  string=str(password_entry.get())
  password_entry.delete(0,END)
  if show_method=='*':
    password_entry=Entry(frame,width=30,bd=2)
    password_entry.grid(row=2,column=1)
    password_entry.insert(0,string)
    show_method=''
  else:
    password_entry=Entry(frame,width=30,bd=2,show='*')
    password_entry.grid(row=2,column=1)
    password_entry.insert(0,string)
    show_method='*'

#main root function
def root_():
  global root
  root=Tk()
  root.title("COLLEGE MANGEMENT SYSTEM")
  root.geometry('1080x720')
  root.configure(bg='bisque')
  global frame
  #login form
  frame=LabelFrame(root,text='LOGIN FORM',padx=100,pady=100,bg='gold2')
  frame.pack(padx=50,pady=50)
  #login_label
  login_label=Label(frame,text="LOGIN AS",width=10,padx=20,pady=10,height=1,bd=5,bg='RED',font='Verdana 10 bold')
  login_label.grid(row=0,column=0)
  #login_dropdown
  global root_clicked
  root_clicked=StringVar()
  root_clicked.set("ADMIN")
  login_option=OptionMenu(frame,root_clicked,"ADMIN","STUDENT","TEACHER")
  login_option.grid(row=0,column=1)
  #username label
  user_label=Label(frame,text="Username :",width=10,padx=20,pady=20,height=1,bd=5,font='Verdana 10 bold')
  user_label.grid(row=1,column=0)
  #username_entry
  global user_entry
  user_entry=Entry(frame,width=30,bd=2)
  user_entry.grid(row=1,column=1)
  #username label
  password_label=Label(frame,text="Password :",width=10,padx=20,pady=20,height=1,bd=5,font='Verdana 10 bold')
  password_label.grid(row=2,column=0)

  show_hide_button=Button(frame,text='SHOW/HIDE',command=show)
  show_hide_button.grid(row=3,column=1,padx=20,pady=20)

  global show_method
  show_method='*'

  #username_entry
  global password_entry
  password_entry=Entry(frame,width=30,bd=2,show='*')
  password_entry.grid(row=2,column=1)
  #login_button
  login_button=Button(frame,text='Login',bd=5,font='Verdana 10 bold',command=login)
  login_button.grid(row=4,column=0,ipadx=30)
  #All Clear_button
  clear_button=Button(frame,text='Clear',bd=5,font='Verdana 10 bold',command=delete)
  clear_button.grid(row=4,column=1,ipadx=30)
  root.mainloop()

#first main function called here
root_()





















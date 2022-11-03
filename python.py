print("Content-Type:text/html")
print()
import cgi

form=cgi.FieldStorage()

id=form.getvalue("id")
Name=form.getvalue("Name")
Address=form.getvalue("Address")
Gender=form.getvalue("Gender")
Hobbies=form.getvalue("Hobbies")
Password=form.getvalue("Password")
Phonenumber=form.getvalue("Phonenumber")

import mysql.connector

con=mysql.connector.connect(user='root',id='',Gender='',Password='', Hobbies='',Name='',Address='',host='localhost',database='table')
cur=con.cursor()

cur.excute("insert intp employee values(%s, %s, %s, %s, %s)",(id,Name,Gender,Hobbies,Password))
con.commit()

con.close()
cur.close()
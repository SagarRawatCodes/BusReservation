
from django.shortcuts import render
import mysql.connector as sql

em =''
pwd =''
def loginaction(request):
    global em,pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Sagar4285", database='user')
        cursor = m.cursor()  # Move this line here

        d = request.POST
        for key,value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "Select * from userDetails where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"home.html")

    return render(request, 'login_page.html')

from django.shortcuts import render
import mysql.connector as sql


fn = ''
ln = ''
s = ''
em = ''
pwd = ''
def signaction(request):
    global fn,ln,s,em,pwd

    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Sagar4285", database='user')
        cursor = m.cursor()  # Move this line here

        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "insert into userDetails Values('{}','{}','{}','{}','{}')".format(fn, ln, s, em, pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')

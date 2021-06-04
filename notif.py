from smtplib import *
from datetime import *
def sender():
    obj=SMTP('smtp.gmail.com',587)
    obj.ehlo()
    obj.starttls()
    email='ratnadeepyeleswarapu@gmail.com'
    passcode='spmndslfqfvnqvsy'#must be your app passcode not your gmail passcode 
    obj.login(email,passcode)
    toadd='ratnadeepyeleswarapu@gmail.com'
    subject='CLASS HAS STARTED'
    mess='MR.RATNADEEP YSVS YOUR CLASS AT {:02d}:{:02d} HAS STARTED PLEASE LISTEN TO THE CLASS'.format(datetime.now().hour,datetime.now().minute)
    msg=f'Subject: {subject}\n\n{mess}'
    obj.sendmail(email,toadd,msg)
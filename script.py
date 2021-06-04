"""
KEY NOTE :-
    AS MOST OF THE ZOOM MEETS WHICH ARE BEING USED ARE TRIAL VERSIONS DUE TO THAT U HAVE TO REJOIN@40 MINS SO I'VE DIRECTLY CODED THAT HERE.
"""
from os import *
from datetime import *
import time,webbrowser
z=[str(i) for i in input('Please Paste Your Class Links Here-> ').split()]#Please Enter Your Class Links Here.
k=[]
for i in range(len(z)):
    s,e=input('Please Enter The Start Time And End Time->').split()#A Quick Note """Please Specify Time In 24 Hour Format""" 
    k=k+[[s,e]]
lis=list(zip(k,z))
lis.sort()
rejoined=False
started=False
def start(t):
    while t:
        time.sleep(1)
        t-=1
    return True
print("CLASSES ARE NOT YET STARTED YOU WILL RECIEVE AN EMAIL WHEN THE CLASS STARTS")
for i in lis:
    sh,sm=i[0][0].split(':')
    eh,em=i[0][1].split(':')
    while True:
        if not started:
            #To Start The Meet
            if datetime.now().hour==int(sh) and datetime.now().minute==int(sm):
                webbrowser.open(i[1])
                started=True
        elif started:
            if not rejoined and start(2400):#Checks For 40 Mins Completion And Rejoins The Meet If Completed
                rejoined=True
                system("wmic process where name='zoom.exe' delete")
                time.sleep(1)
                print('40 MINS OF THE CLASS HAS COMPLETED.\nREJOINING THE MEET AGAIN.')
                webbrowser.open(i[1])
            if datetime.now().hour==int(eh) and datetime.now().minute==int(em):
                system("wmic process where name='zoom.exe' delete")
                print('MEET HAS COMPLETED.')
                rejoined=False
                started=False
                break
print('YOU HAVE COMPLETED ALL YOUR CLASSES TODAY.')
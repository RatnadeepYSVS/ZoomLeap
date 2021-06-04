"""
KEY NOTE :-
    AS MOST OF THE ZOOM MEETS WHICH ARE BEING USED ARE TRIAL VERSIONS DUE TO THAT U HAVE TO REJOIN@40 MINS SO I'VE DIRECTLY CODED THAT HERE.
"""
from os import *
from datetime import *
import time,webbrowser
z=[str(i) for i in input('Please Paste Your Class Links Here-> ').split()]#Please Enter Your Class Links Here.
k=[]#This List Stores Class Timings 
for i in range(len(z)):
    s,e=input('Please Enter The Start Time And End Time->').split()#A Quick Note """Please Specify Time In 24 Hour Format""" 
    k=k+[[s,e]]#Adds Timings For Perspective classes
lis=list(zip(k,z))#Mapping class Links and  Their Timings
lis.sort()#Sorting Based On Least Time
rejoined=False#Flag Variable 1
started=False#Flag Variable 2
def start(t):
    #This Function Returns After 40 mins Time is Completed
    while t:
        time.sleep(1)
        t-=1
    return True
for i in lis:#Looping Through Out The Class Links
    sh,sm=i[0][0].split(':')#Getting The Start Hour And Start Minute of Class Time
    eh,em=i[0][1].split(':')#Getting The End Hour And End Minute of Class Time
    while True:
        if not started:#Checking If The Class is Started Or Not
            #To Start The Meet
            if datetime.now().hour==int(sh) and datetime.now().minute==int(sm):#Checking The Start Time OF THe Class
                webbrowser.open(i[1])#Opens The Class Link If above Condition Is True
                started=True#Setting The Flag Variable 1 to True
        elif started:
            if not rejoined and start(2400):#Checks For 40 Mins Completion And Rejoins The Meet If Completed
                rejoined=True#Setting The Flag Variable 2 to True
                system("wmic process where name='zoom.exe' delete")#CLoses Zoom 
                time.sleep(1)
                print('40 MINS OF THE CLASS HAS COMPLETED.\nREJOINING THE MEET AGAIN.')
                webbrowser.open(i[1])#Opening The Class Link AS we Are Rejoining
            if datetime.now().hour==int(eh) and datetime.now().minute==int(em):#Checking The End Time OF The Class
                system("wmic process where name='zoom.exe' delete")#Ending The CLass
                print('MEET HAS COMPLETED.')
                rejoined=False#Setting Flag to False
                started=False#Setting Flag to False
                break
print('YOU HAVE COMPLETED ALL YOUR CLASSES TODAY.')
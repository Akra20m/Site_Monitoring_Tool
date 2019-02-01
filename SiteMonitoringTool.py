import imgkit
import time
import numpy as np
import cv2
import smtplib
from tkinter import *


window = Tk()
window.title("Site Monitoring Tool")



def watch(im_g1pre):
    config = imgkit.config(wkhtmltoimage=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe')
    options = {

        'javascript-delay': '200',
        #'crop-h': '500',
        #'crop-w': '200',
        #'crop-x': '50',
        #'crop-y': '50',
        #'quality':'100'
        #'no-stop-slow-scripts':''
    }

    try:
        imgkit.from_url(b1_value.get(), "image.jpg", config=config, options=options)
        im_g1=cv2.imread('image.jpg',0)
        im_g1=im_g1.tolist()


        if im_g1pre==[]:
            im_g1pre = im_g1

        if im_g1 != im_g1pre:
            c1.delete("1.0",END)
            c1.insert(END,"send message")
            print("send message")

            # #Using Twilio
            # from twilio.rest import Client
            #
            # # Your Account SID from twilio.com/console
            # account_sid = "#"
            # # Your Auth Token from twilio.com/console
            # auth_token  = "#"
            #
            # client = Client(account_sid, auth_token)
            #
            # message = client.messages.create(
            #     to="#",
            #     from_="#",
            #     body="Your message here")
            #
            # print(message.sid)
            #
            if h1_value.get() == 1:
                print("It is working")
                # send send_to_email
                email = k1_value.get()
                password = m1_value.get()
                send_to_email = o1_value.get()
                message = q1_value.get()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email , message)
                server.quit()

        else:
            c1.delete("1.0",END)
            c1.insert(END,"No Change")
            print("No change !")


        im_g1pre = im_g1
        print(time.ctime())
        #time.sleep(15) # time is in seconds
        window.after((int(g1_value.get())*1000), lambda: watch(im_g1pre))

    except Exception as e:
        print(e)
        c1.delete("1.0",END)
        c1.insert(END,"There is problem with the server")
        print("There is problem with the server")
        print(time.ctime())
        #time.sleep(15)
        window.after((int(g1_value.get())*1000), lambda: watch(im_g1pre))

def function1():
    global stateCheck
    if h1_value.get()==0:
        k1.config(state="disabled")
        m1.config(state="disabled")
        o1.config(state="disabled")
        q1.config(state="disabled")
        print("OFF")

    else:
        k1.config(state="normal")
        m1.config(state="normal")
        o1.config(state="normal")
        q1.config(state="normal")
        print("ON")



title=Label(window,text="Site Monitoring Tool",width="30",bg="blue")
title.grid(row=0,column=0)

a1=Button(window,text="Execute",command=lambda: watch(im_g1pre=[]))
a1.grid(row=9,column=0)

b1_value=StringVar()
b1=Entry(window,textvariable=b1_value,state="normal",width="40")
b1.grid(row=1,column=1)

c1=Text(window,height=1,width="30")
c1.grid(row=3,column=1)

d1=Label(window,text="Website Link",width="30")
d1.grid(row=1,column=0)

e1=Label(window,text="Status",width="30")
e1.grid(row=3,column=0)

f1=Label(window,text="Scan Time(s)",width="30")
f1.grid(row=2,column=0)

g1_value=StringVar()
g1=Entry(window,textvariable=g1_value,width="40")
g1.grid(row=2,column=1)

h1_value=IntVar(value=1)
h1=Checkbutton(window,state=NORMAL,variable=h1_value,command=function1)
h1.grid(row=4,column=1)

i1=Label(window,text="Email Notifications")
i1.grid(row=4,column=0)

j1=Label(window,text="Sender-Email")
j1.grid(row=5,column=0)

k1_value=StringVar()
k1=Entry(window,textvariable=k1_value,width="40")
k1.grid(row=5,column=1)

l1=Label(window,text="Sender-Password")
l1.grid(row=6,column=0)

m1_value=StringVar()
m1=Entry(window,textvariable=m1_value,show="*",width="40")
m1.grid(row=6,column=1)

n1=Label(window,text="Receiver-Email")
n1.grid(row=7,column=0)

o1_value=StringVar()
o1=Entry(window,textvariable=o1_value,width="40")
o1.grid(row=7,column=1)

p1=Label(window,text="Message")
p1.grid(row=8,column=0)

q1_value=StringVar()
q1=Entry(window,textvariable=q1_value,width="40")
q1.grid(row=8,column=1)

window.mainloop()

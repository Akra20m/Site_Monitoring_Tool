import imgkit
import time
import numpy as np
import cv2
import smtplib
from tkinter import *


window = Tk()



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
    #im_g1pre=[]

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
            # # send send_to_email
            # email = '#'
            # password = '#'
            # send_to_email = '#'
            # message = '#
            #
            # server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.starttls()
            # server.login(email, password)
            # server.sendmail(email, send_to_email , message)
            # server.quit()

        else:
            c1.delete("1.0",END)
            c1.insert(END,"No Change")
            print("No change !")


        im_g1pre = im_g1
        print(time.ctime())
        #time.sleep(15) # time is in seconds
        window.after(10000, lambda: watch(im_g1pre))

    except Exception as e:
        print(e)
        c1.delete("1.0",END)
        c1.insert(END,"There is problem with the server")
        print("There is problem with the server")
        print(time.ctime())
        #time.sleep(15)
        window.after(10000, lambda: watch(im_g1pre))



a1=Button(window,text="Execute",command=lambda: watch(im_g1pre=[]))
a1.grid(row=2,column=0)

b1_value=StringVar()
b1=Entry(window,textvariable=b1_value)
b1.grid(row=0,column=1)

c1=Text(window,height=1)
c1.grid(row=1,column=1)

d1=Label(window,text="Website Link",width=30)
d1.grid(row=0,column=0)

e1=Label(window,text="Status",width=30)
e1.grid(row=1,column=0)

window.mainloop()

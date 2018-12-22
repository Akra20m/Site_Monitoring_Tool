import imgkit
import time
import numpy as np
import cv2
import smtplib

config = imgkit.config(wkhtmltoimage=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe')
im_g1pre=[]
while True:
    try:
        imgkit.from_url('put_url_here', "image.jpg", config=config)
        im_g1=cv2.imread('image.jpg',0)
        im_g1=im_g1.tolist()


        if im_g1pre==[]:
            im_g1pre = im_g1

        if im_g1 != im_g1pre:
            print(" send message")
            Using Twilio
            from twilio.rest import Client

            # Your Account SID from twilio.com/console
            account_sid = "#"
            # Your Auth Token from twilio.com/console
            auth_token  = "#"

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to="#",
                from_="#",
                body="Your message here")

            print(message.sid)

            # send send_to_email
            email = '#'
            password = '#'
            send_to_email = '#'
            message = '#

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, send_to_email , message)
            server.quit()

        else:
            print("No change !")


        im_g1pre = im_g1
        print(time.ctime())
        time.sleep(5*60) # time is in seconds

    except:
        print("There is problem with the server")
        print(time.ctime())
        time.sleep(5*60)

import os
import smtplib
import imghdr
from email.message import EmailMessage

Email_Adress="XXX@gmail.com"
Email_Password="xxxxxxxxx"
msg = EmailMessage()
msg['Subject'] = 'here your certificate'
msg['From'] = Email_Adress
msg['To'] = 'YYY@gamil.com'
msg.set_content('Ahem codashmi certificate')
with open("O.png",'rb') as  f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    file_name=f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Adress, Email_Password)
    smtp.send_message(msg)

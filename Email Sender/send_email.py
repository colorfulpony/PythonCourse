from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'flexywall@gmail.com'
email_password = 'mkrmbrzxacamywig'
email_receiver = '4oper321@gmail.com'

subject = 'Percentage below -0.10%'
body = """\
Subject: Hi there
The percentage is under -10%"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

def send_notification():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
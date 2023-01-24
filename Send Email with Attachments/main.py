import yagmail
import os


email_password = 'mkrmbrzxacamywig'
sender = "flexywall@gmail.com"
receiver = "qarowole@lyft.live"

subject = "This is the subject"
content = ["""
Here is the content of the email
""", 'text.txt']

yag = yagmail.SMTP(user=sender, password=email_password)
yag.send(to=receiver, subject=subject, contents=content)
print("Done")



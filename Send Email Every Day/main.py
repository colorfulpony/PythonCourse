import yagmail
import os


email_password = 'mkrmbrzxacamywig'
sender = "flexywall@gmail.com"
receiver = "4oper321@gmail.com"

subject = "This is the subject"
content = """
Here is the content of the email
"""

yag = yagmail.SMTP(user=sender, password=email_password)
yag.send(to=receiver, subject=subject, contents=content)
print("Done")



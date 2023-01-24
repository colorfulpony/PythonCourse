import yagmail
import os
import pandas


email_password = 'mkrmbrzxacamywig'
sender = "flexywall@gmail.com"

subject = "This is the subject"

yag = yagmail.SMTP(user=sender, password=email_password)

df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
    content = f"""
    Hi {row['name']}. Here is the content of the email
    """
    yag.send(to=row['email'], subject=subject, contents=content)
    print("Done")



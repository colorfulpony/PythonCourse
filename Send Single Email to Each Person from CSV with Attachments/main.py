import yagmail
import os
import pandas


email_password = 'mkrmbrzxacamywig'
sender = "flexywall@gmail.com"

subject = "This is the subject"

yag = yagmail.SMTP(user=sender, password=email_password)

df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
    content = [f"""
    Hi {row['name']}. You have to pay {row['amount']}. Bill in the attachments
    """, row['filepath']]
    yag.send(to=row['email'], subject=subject, contents=content)
    print("Done")



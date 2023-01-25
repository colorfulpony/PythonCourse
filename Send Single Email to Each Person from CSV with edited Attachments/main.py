import yagmail
import os
import pandas

email_password = 'mkrmbrzxacamywig'
sender = "flexywall@gmail.com"
subject = "This is the subject"
yag = yagmail.SMTP(user=sender, password=email_password)

df = pandas.read_csv('contacts.csv')

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))

for index, row in df.iterrows():
    name = row['name']
    filename = name + ".txt"
    amount = row['amount']
    receive_email = row['email']

    generate_file(filename, amount)

    content = [f"""
    Hi {name}. You have to pay {amount}. Bill in the attachments
    """,
    filename,
    ]
    yag.send(to=receive_email, subject=subject, contents=content)
    print("Done")



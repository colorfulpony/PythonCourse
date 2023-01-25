import smtplib

#Here should be info of outlook or hotmail accounts
sender = "flexywall@gmail.com"
receiver = "4oper321@gmail.com"
password = "3631508535sashke"

message = """\
Subject: Hello World

This is Ardit:
Some Text
"""

server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Here should be info of outlook or hotmail accounts
sender = "flexywall@gmail.com"
receiver = "4oper321@gmail.com"
password = "3631508535sashke"

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Hello"

body = """
<h1>Hi there</h1>
<p>Some paragraph text</p>
"""

mimetext = MIMEText(body, "html")

message.attach(mimetext)
message_text = message.as_string()

server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message_text)
print(message_text)
server.quit()
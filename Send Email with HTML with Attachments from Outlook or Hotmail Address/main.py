import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


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

attachments_path = "text.txt"
attachments_file = open(attachments_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachments_file.read())
encoders.encode_base64(payload)
payload.add_header("Content-Disposition", "attachment", filename=attachments_path)
message.attach(payload)

server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message_text)
print(message_text)
server.quit()
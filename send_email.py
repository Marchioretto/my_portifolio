import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "dev.marchioretto@gmail.com"
password = 'sxcrekjncdnbzuov'

receiver = "dev.marchioretto@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

import smtplib, ssl

HOST = "smtp.gmail.com"
PORT = "465"


def send_email(email_address,message):

	
	username = "duck0249@gmail.com"
	password = "bunwplqqhnfliigk"

	receiver = "duck0249@gmail.com"

	context = ssl.create_default_context()

	message = f"""\
Subject: New email from {email_address}

From : {email_address} 
{message}
"""

	with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)

if __name__ == "__main__":
	sending_email("duck0249@naver.com", "Hello, it is the test.")

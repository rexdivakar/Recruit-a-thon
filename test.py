import smtplib, ssl
from extra import get_password
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "testrecruitathon@gmail.com"
password = get_password()


# Create a secure SSL context
context = ssl.create_default_context()

def mail():
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        message='hi'
        server.sendmail(sender_email, 'rexdivakar@hotmail.com', message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 
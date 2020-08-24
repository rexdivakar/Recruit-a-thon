from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

#Loading the password
with open('pas.1','r') as f:
    password=f.read()
    
sender_email = "rexdivakar@gmail.com"


def email_content(ip,mail):
    # Preview resumes by HR
    
    receiver_email = mail

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    if ip==1:
        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?"""
        html = """\
        <html>
        <body>
            <p>Hi,<br>
            How are you?<br>
            </p>
        </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)
        
    #Mailing template to call for interview
    elif ip==2:   
        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?"""
        html = """\
        <html>
        <body>
            <p>Hi,<br>
            How are you?<br>
            </p>
        </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    return ('Mail Sent')


# email_content(2,'rexdivakar@hotmail.com')
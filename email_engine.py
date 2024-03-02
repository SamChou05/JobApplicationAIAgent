import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from llama_index.core.tools import FunctionTool
import os

def send_email(recipient_email=None, email_body='', resume_path=''):
    secret_key = os.getenv('EMAIL_PW')
    # Email account credentials
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587  # Use 465 for SSL
    email_address = 'sam@thechous.com'
    password = secret_key

    # Email recipient and subject (MUST BE CUSTOMIZABLE)
    recipient_email = recipient_email
    subject = 'Job Inquiry'

    # Email body (MUST BE CUSTOMIZABLE, get based on CV and job description)
    body = email_body

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = recipient_email
    message['Subject'] = "Job Inquiry"

    # Attach the email body to the message
    message.attach(MIMEText(body, 'plain'))

    # Specify the filename of the attachment (path if not in the same directory)
    # filename = resume_path
    filename = resume_path

    # Open the file to attach
    # with open(filename, 'rb') as attachment:
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload(attachment.read())

    # # Encode the file in ASCII characters to send by email
    # encoders.encode_base64(part)

    # # Add header to the attachment
    # part.add_header(
    #     'Content-Disposition',
    #     f'attachment; filename= {filename}',
    # )

    # # Attach the part (the attachment) to the message
    # message.attach(part)

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Encrypts the connection
            server.login(email_address, password)
            server.send_message(message)
            print("Email sent successfully!")
            return "Email sent successfully!"
    except Exception as e:
        print(f"Error sending email: {e}")

email_engine = FunctionTool.from_defaults(
    fn=send_email,
    name="email_sender",
    description="this tool can send emails to a given email recipient with an email body and path to a resume as an attachment",
)
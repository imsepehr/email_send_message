from email.message import EmailMessage
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(em_send = 'sepehr1657ebadi@gmail.com',em_pass = 'pass',em_rec = 'alirewzaebi@gmail.com',em_text = 'this email was send with python.'):
    subject = 'check out new email'

    #em = EmailMessage()
    em = MIMEMultipart()
    em['From'] = em_send
    em['To'] = em_rec
    em['Subject'] = subject
    #em.set_content(em_text)
    em.attach(MIMEText(em_text))
    context = ssl.create_default_context()

    #creat attachment
    file_path = r"E:\\"
    file_name = "git-cheat-sheet-education.pdf"
    file = open(file_path+file_name,"rb")

    payload = MIMEBase('application','octet-stream')
    payload.set_payload(file.read())
    file.close()

    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=file_name)
    em.attach(payload)

    #send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(em_send,em_pass)
        smtp.sendmail(em_send,em_rec,em.as_string())


def main():
    send_email()

if __name__ == '__main__':
    main()

from email.message import EmailMessage
import ssl
import smtplib

email_sender = "sakalaka094@gmail.com"
email_password = "Sakalaka34@"
email_receiver = "asmahin8@gmail.com"
em = EmailMessage()
em['FROM'] = email_sender
em['To'] = email_receiver
#em['subject'] = subject
#em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

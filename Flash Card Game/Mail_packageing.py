import smtplib
my_email = 'confessionpust46@gmail.com'
password = 'Confession21@'
with smtplib.SMTP('smtp.gmail.com') as connection :
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='asmahin8@gmail.com',
        msg="Subject:Hello\n\n This is body of email"
    )
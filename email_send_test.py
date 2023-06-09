from email.message import EmailMessage
import ssl
import smtplib


def send_otp(reciver,otp):
    otp=str(otp)
    email_sender="pavanparashuramdevang2@gmail.com"
    email_password='bahuyeaifeslmwyz'
    email_receiver=reciver

    subject="OTP for student login GECM"

    body=f"Your otp for student login is : {otp}"

    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())


if __name__=="__main__":
    send_otp('pavanparashuramdevang@gmail.com','123412')

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_to_list = ['xxx@xx.com']
mail_host = "smtp.163.com"
mail_user = "xxx@163.com"
mail_pass = "xxx"


def send_mail(subject, content):
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = subject
    msg['From'] = mail_user
    msg['To'] = ";".join(mail_to_list)

    if login_and_send_mail(msg):
        return True


def send_mail_with_attachment(subject, content):
    msg_root = MIMEMultipart(content, 'related')
    msg_root['Subject'] = subject
    msg_root['From'] = mail_user
    msg_root['To'] = ";".join(mail_to_list)

    msg = MIMEText(open('D:\\image.jpg', 'rb').read(), 'base64', 'utf-8')
    msg['Content-type'] = 'application/octet-stream'
    msg['Content-Disposition'] = 'attachment; filename = "image.jpg" '
    msg_root.attach(msg)

    if login_and_send_mail(msg_root):
        return True


def login_and_send_mail(msg):
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(mail_user, mail_to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == '__main__':

    # send a simple mail
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sub = "hello"
    ctx = "this is a mail test!" + " time is: " + now
    if send_mail(sub, ctx):
        print("done!")
    else:
        print("failed!")

    # send a mail with attachment
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sub = "test mail with attachment"
    ctx = "here is the image.jpg" + " time is " + now
    if send_mail_with_attachment(sub, ctx):
        print("done!")
    else:
        print("failed!")

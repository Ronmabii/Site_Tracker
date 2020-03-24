import smtplib
import os


def send_email(subject,body):

    # Environment Variables (Online/Offline)
    my_email = os.environ.get('CRUD_EMAIL')
    password = os.environ.get('CRUD_PASS')

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(my_email, password)
        message = 'SUBJECT: {}\n{}'.format(subject,body)
        server.sendmail(my_email, my_email, message) #(From, To, Message)
        server.quit()
        print('SUCCESS')
    except:
        print('FAIL')

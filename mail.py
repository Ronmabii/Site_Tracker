import smtplib
import credentials as cred

my_email = cred.EMAIL_ADDRESS
password = cred.PASSWORD

def send_email(subject,body):
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

subject = 'First Test'
body = 'Hope it works'

send_email(subject,body)

# typos strike again(ADRESS)
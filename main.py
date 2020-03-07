import smtplib
import credentials as cred

def send_email(subject,body):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(cred.EMAIL_ADDRESS, cred.PASSWORD)
        message = 'SUBJECT: {}\n{}'.format(subject,body)
        server.sendmail(cred.EMAIL_ADDRESS, cred.EMAIL_ADDRESS, message) #(From, To, Message)
        server.quit()
        print('SUCCESS')
    except:
        print('FAIL')

subject = 'First Test'
body = 'Hope it works'

send_email(subject,body)

# typos strike again(ADRESS)
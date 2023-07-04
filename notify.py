import argparse

def send_email(message, subject = 'JOB STATUS UPDATE'):
    import smtplib
    gmail_user = 'jobstatusou@gmail.com'
    gmail_password = 'uoscidoasrnpmmqb'

    sent_from = gmail_user
    to = ['huongpham1603@gmail.com']
    
    header  = 'From: %s\n' % sent_from
    header += 'To: %s\n' % ','.join(to)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send email with message and subject')
    parser.add_argument('-m','--message', type=str, help='the email message')
    parser.add_argument('-s','--subject', type=str, default='JOB STATUS UPDATE', help='the email subject')
    args = parser.parse_args()

    send_email(args.message, args.subject)
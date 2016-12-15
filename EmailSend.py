#!/usr/bin/env python3

import smtplib


class Send_Mail:

    def __init__(self, user, passwd, recipient, subject, body):
        self.user = user
        self.passwd = passwd
        self.recipient = recipient
        self.subject = subject
        self.body = body


    def send_mail(self):
        gmail_user = self.user
        gmail_passwd = self.passwd
        FROM = self.user
        TO = self.recipient
        SUBJECT = self.subject
        TEXT = self.body

        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    print(message)
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_passwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("successfully send mail")
    except:
        print("failed to send mail")


mail = Send_Mail("jeanmarc.wagner86@gmail.com", "Tunnel2345", "jeanmarc.wagner@gmx.de", "Test Betreff", "Test Nachricht")
mail.send_mail()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import smtplib

class MailScreen(Screen):

    user = ObjectProperty()
    passwd = ObjectProperty()
    recipient = ObjectProperty()
    betreff = ObjectProperty()
    nachricht = ObjectProperty()

    def sendmail(self):
        try:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(self.user.text, self.password.text)
            server.sendmail(self.user.text, self.recipient, self.betreff.text, self.nachricht.text )
            server.close()
            print("successfully send mail")
        except:
            print("failed to send mail")


class MainScreen(Screen):
    pass

class Manager(ScreenManager):
    mail_screen = ObjectProperty()
    main_screen = ObjectProperty()


class MailApp(App):

    def build(self):
        return Manager()




if __name__ == "__main__":
        MailApp().run()

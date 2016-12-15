from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class MailScreen(Screen):

    user = ObjectProperty()
    passwd = ObjectProperty()
    recipient = ObjectProperty()
    



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

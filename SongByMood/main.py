from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from datetime import datetime
import random

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        self.manager.transition.direction = 'left'

    def success(self,uname,pword):
        with open('accounts.json','r') as file:
            accounts = json.load(file)
            if uname in accounts and accounts[uname]['password'] == pword:
                if uname != "" and pword != "":
                    self.manager.current = "success"
                    self.manager.transition.direction = 'left'
            else:
                self.ids.login_failed.text = "I'm sorry, you are not in the terminator's family yet.."



class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open('accounts.json') as file:
            accounts = json.load(file)
        accounts[uname] = {'username': uname, 'password': pword,
                           'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        if uname != "" and pword != "":
            with open('accounts.json','w') as file:
                json.dump(accounts,file)
                self.manager.current = "signedup"

    def login_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class SignedUp(Screen):
    def mainmenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class SuccessScreen(Screen):
    def mainmenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def emotion(self):
        emotionlist = ["sad", "happy", "nostalgic"]
        if self.ids.userfeeling.text not in emotionlist:
            self.ids.advice.text = "Try some other emotions"
        else:
            if self.ids.userfeeling.text == "sad":
                f1 = open('sad.txt', 'r', encoding="utf8")
                lines1 = f1.readlines()
                self.ids.advice.text = random.choice(lines1)
            if self.ids.userfeeling.text == "happy":
                f2 = open('happy.txt', 'r', encoding="utf8")
                lines2 = f2.readlines()
                self.ids.advice.text = random.choice(lines2)

            if self.ids.userfeeling.text == "nostalgic":
                f3 = open('nostalgic.txt', 'r', encoding="utf8")
                lines3 = f3.readlines()
                self.ids.advice.text = random.choice(lines3)



class ImageButton(ButtonBehavior,HoverBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
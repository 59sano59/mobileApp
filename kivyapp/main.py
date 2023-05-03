from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivyapp.database import DataBase as db

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.addUser(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"

            else:
                invalidForm()

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current= 'login'

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginButton(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = 'main'
        else:
            invalidLogin()

    def createButton(self):
        self.reset()
        sm.current = 'create'

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self):
        password, name, created = db.getUser(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file(".vscode/myapp.kv")
sm  =WindowManager()
db = db("users.txt")

screens = [LoginWindow(name='login'), CreateAccountWindow(name='create'), MainWindow(name='main')]
for screen in screens:
    sm.add_widget(screen)

sm.current= 'login'

class MyApp(App):
    def build(self):
        return sm
    
if __name__ == '__main__':
    MyApp().run()
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from tkinter import dialog
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from database import Datab


account_kv = Builder.load_file('account.kv')

class RegisterAccountScreen(Screen):
    dialog = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.conn  = Datab()
    
    def select(self):
        print(self.ids.user.text)
    
    def register_btn_click(self):
        fullname = self.ids.fullname.text
        username = self.ids.username.text
        email = self.ids.email.text
        phone = self.ids.phone.text
        address = self.ids.address.text
        password = self.ids.password.text
        role = self.ids.role.text
        create_user = self.conn.create_user(fullname, username, email, phone, address, password, role)
        if create_user:
            self.reset()
            toast('user account created successfully')
        if not create_user:
            toast('account not created')
            
    def reset(self):
        self.ids.fullname.text = ""
        self.ids.username.text = ""
        self.ids.email.text = ""
        self.ids.phone.text = ""
        self.ids.address.text = ""
        self.ids.password.text = ""
        

class LoginScreen(Screen):
    dialog = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.db  = Datab()

    def user_login(self):
        username = self.ids.login_username.text
        password = self.ids.login_password.text
        login = self.db.login(username, password)
        # self.sm = WindowManager()
        if login:
            self.reset()
            self.manager.current = 'UserButtons'
        if not login:
            toast('You have entered wrong user credentials')

    def reset(self):
        self.ids.login_username.text = ""
        self.ids.login_password.text = ""

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="User has logged in"
            )
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()
        
class UserButtons(Screen):
    Builder.load_file("UserButtons.kv")
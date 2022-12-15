from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivymd.icon_definitions import md_icons
from kivymd.uix.button.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
#from database import SellerDB
from account import LoginScreen

Window.size = (300, 500)
Window.clearcolor = (1, 1, 1, 1)

kv = Builder.load_file('Customer.kv')

class CustomerHomepage(Screen):
    pass

class ProfileCard (MDFloatLayout):
    pass

class CustomerPage(MDApp):
    
    dialog = None
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CustomerHomepage(name= 'CustomerHomepage'))
        sm.add_widget(ProfilePage_Customer(name= 'ProfilePage_Customer'))
        sm.add_widget(ContentAdd(name= 'ContentAdd'))
        sm.add_widget(Notification_Customer(name= 'Notification_Customer'))
        sm.add_widget(Message_Customer(name= 'Message_Customer'))
        sm.add_widget(LoginScreen(name= 'LoginScreen'))
        sm.add_widget(Tracking_Info(name= 'Tracking_Info'))
        
        return sm
    
    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Tracking No.",
                type="custom",
                size_hint= [0.8, 0.8],
                content_cls= ContentAdd())
            self.dialog.open()

class ContentAdd(Screen):
    pass

class Tracking_Info(Screen):
    pass
    
    '''def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.conn  = SellerDB()    
    
    def track_btn(self):
        tracking_id = self.ids.track_trackindID
        track = self.conn.track(tracking_id)
        if track:
            self.reset()
            self.manager.current = 'CustomerHomepage'
        if not track:
            toast('You have entered wrong user credentials')'''

class Notification_Customer(Screen):
    pass

class Message_Customer(Screen):
    pass
    
class ProfilePage_Customer(Screen):
    pass

if __name__ == "__main__":
    CustomerPage().run()
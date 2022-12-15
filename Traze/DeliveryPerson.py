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
from map_ACO_Abeto import CefBrowser1
from map_djikstra_Abeto import CefBrowser2
from map_ACO_Bakhaw import CefBrowser3
from map_djikstra_Bakhaw import CefBrowser4
from map_ACO_Mohon import CefBrowser5
from map_djikstra_Mohon import CefBrowser6

Window.size = (300, 500)
Window.clearcolor = (1, 1, 1, 1)
#kv = Builder.load_file('Profile.kv')
kv = Builder.load_file('DeliveryPerson.kv')

class DeliveryPersonHomepage(Screen):
    pass

class ProfileCard (MDFloatLayout):
    pass

class DeliveryPersonPage(MDApp):
    
    dialog = None
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DeliveryPersonHomepage(name= 'DeliveryPersonHomepage'))
        sm.add_widget(ProfilePage_DeliveryPerson(name= 'ProfilePage_DeliveryPerson'))
        sm.add_widget(DeliveryInfo1(name= 'DeliveryInfo1'))
        sm.add_widget(DeliveryInfo2(name= 'DeliveryInfo2'))
        sm.add_widget(DeliveryInfo3(name= 'DeliveryInfo3'))
        sm.add_widget(CefBrowser1(name= 'map_ACO_Abeto'))
        sm.add_widget(CefBrowser2(name= 'map_djikstra_Abeto'))
        sm.add_widget(CefBrowser3(name='map_ACO_Bakhaw'))
        sm.add_widget(CefBrowser4(name= 'map_djikstra_Bakhaw'))
        sm.add_widget(CefBrowser5(name= 'map_ACO_Mohon'))
        sm.add_widget(CefBrowser6(name= 'map_djikstra_Mohon'))
        sm.add_widget(Notification_DPerson(name = 'Notification_DPerson'))
        sm.add_widget(Message_DPerson(name = 'Message_DPerson'))
        return sm
    
    
class ProfilePage_DeliveryPerson(Screen):
    pass

class DeliveryInfo1(Screen):
    pass

class DeliveryInfo2(Screen):
    pass

class DeliveryInfo3(Screen):
    pass

class Notification_DPerson(Screen):
    pass

class Message_DPerson(Screen):
    pass

if __name__ == "__main__":
    DeliveryPersonPage().run()
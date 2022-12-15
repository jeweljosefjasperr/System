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
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from database import SellerDB, get_data
from account import LoginScreen
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
import kivy.utils
import sqlite3
from kivy.properties import StringProperty, ListProperty, BooleanProperty, ObjectProperty


Builder.load_file('Seller.kv')


class SellerHomepage(Screen):
    pass
        
class CustomerList(OneLineIconListItem):
    
    def get_custname(self):
        cust = self.text
        print(cust)
        
        
        
        
class Customer_Page(Screen):
    pass
    

class ProfileCard (MDFloatLayout):
    pass

class SellerPage(MDApp):
    
    dialog = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SellerHomepage(name= 'SellerHomepage'))
        sm.add_widget(Customer_Info(name= 'Customer_Info'))
        sm.add_widget(ProfilePage_Seller(name= 'ProfilePage_Seller'))
        sm.add_widget(Notification_Seller(name= 'Notification_Seller'))
        sm.add_widget(Message_Seller(name= 'Message_Seller'))
        sm.add_widget(Add_Customer(name= 'Add_Customer'))
        sm.add_widget(LoginScreen(name= 'LoginScreen'))
        return sm
    
    
        
'''    def on_start(self):
        conn = sqlite3.connect(database = "test.db")
        cursor = conn.cursor()
        cust_names = cursor.execute("SELECT cust_name FROM seller ORDER BY tracking_id ASC").fetchall()
        for name in cust_names:
            cust1 = (name[0])
            print(cust1)
        
        for name in cust_names:
            item = OneLineIconListItem(text = self.name, on_release=lambda x, value_for_pass=name: self.passValue(value_for_pass))
            self.ids.container.add_widget(item)'''
            #self.root.ids.container.add_widget(OneLineIconListItem(text=f"Single-line item {name}"))
'''items = OneLineIconListItem(text=str(self.name),on_release=self.show_data)
            
            item = OneLineIconListItem(
            text = self.name
            on_release=lambda x, value_for_pass=name: self.passValue(value_for_pass)
            )
                
            self.ids.container.add_widget(item)
            
            icon = IconLeftWidget(icon = 'menu')
            items.add_widget(image)
            self.root.ids.container.add_widget(item)
'''
class Customer_Info(Screen):
    pass

class Add_Customer(Screen):
    dialog = None
    obj = ObjectProperty(None)
    obj_text = StringProperty("")
        
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.conn  = SellerDB()

    def select(self):
        print(self.ids.category.text)
        
    def AddCustomer_btn(self):
        #tracking_id = self.conn.tracking_id
        cust_name = self.ids.cust_name.text
        cust_phone = self.ids.cust_phone.text
        item_name = self.ids.item_name.text
        cust_addr = self.ids.cust_addr.text
        pu_addr = self.ids.pu_addr.text
        date_order = self.ids.date_order.text
        category = self.ids.category.text
        add_customer = self.conn.add_customer(cust_name, cust_phone, item_name, cust_addr, pu_addr, date_order, category)
        if add_customer:
            self.reset()
            toast('Customer Added Successfully')
        if not add_customer:
            toast('Adding Customer Failed. Try Again')

    def reset(self):
        self.ids.cust_name.text = ""
        self.ids.cust_phone.text = ""
        self.ids.item_name.text = ""
        self.ids.cust_addr.text = ""
        self.ids.pu_addr.text = ""
        self.ids.date_order.text = ""
        self.ids.category.text = ""
    
    
class Notification_Seller(Screen):
    pass

class Message_Seller(Screen):
    pass
    
class ProfilePage_Seller(Screen):
    pass
    

if __name__ == "__main__":
    SellerPage().run()
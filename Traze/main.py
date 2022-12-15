from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from account import LoginScreen, RegisterAccountScreen, UserButtons
from first import fScreen
from Customer import CustomerHomepage, ProfilePage_Customer, Notification_Customer, Message_Customer, ContentAdd
from Seller import SellerHomepage, ProfilePage_Seller, Customer_Info, Notification_Seller, Message_Seller, Add_Customer
from DeliveryPerson import DeliveryPersonHomepage, ProfilePage_DeliveryPerson



Window.size = (300, 500)

class MainApp(MDApp):

    dialog = None
    
    def build(self):
        self.theme_cls.theme_style="Light"
        sm = ScreenManager()
        sm.add_widget(fScreen(name='fscreen'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterAccountScreen(name= 'register'))
        sm.add_widget(UserButtons(name= 'UserButtons'))
        sm.add_widget(CustomerHomepage(name= 'CustomerHomepage'))
        sm.add_widget(ProfilePage_Customer(name= 'ProfilePage_Customer'))
        sm.add_widget(ContentAdd(name= 'ContentAdd'))
        sm.add_widget(Notification_Customer(name= 'Notification_Customer'))
        sm.add_widget(Message_Customer(name = 'Message_Customer'))
        sm.add_widget(SellerHomepage(name= 'SellerHomepage'))
        sm.add_widget(Add_Customer(name= 'Add_Customer'))
        sm.add_widget(Customer_Info(name= 'Customer_Info'))
        sm.add_widget(ProfilePage_Seller(name= 'ProfilePage_Seller'))
        sm.add_widget(Notification_Seller(name= 'Notification_Seller'))
        sm.add_widget(Message_Seller(name= 'Message_Seller'))
        sm.add_widget(DeliveryPersonHomepage(name= 'DeliveryPersonHomepage'))
        sm.add_widget(ProfilePage_DeliveryPerson(name= 'ProfilePage_DeliveryPerson'))
        
        #show_map = CefBrowser()

        return sm
    
    '''def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Customer Details:",
                type="custom",
                size_hint= [0.8, 0.8],
                content_cls= ContentAdd_Seller())
            self.dialog.open()'''

if __name__ == '__main__':
    MainApp().run()
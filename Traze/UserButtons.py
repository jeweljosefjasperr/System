from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


Window.size = (300, 500)
kv = Builder.load_file('UserButtons.kv')

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        sm = ScreenManager()
        sm.add_widget(UserButtons(name= 'UserButtons'))
        
        return sm
    
class UserButtons(Screen):
    pass

if __name__ == '__main__':
    MyApp().run()
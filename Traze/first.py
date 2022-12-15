from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image


kv = Builder.load_file('fScreen.kv')

class fScreen(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def image(self):
        self.ids.img.source = 'Logo.png'
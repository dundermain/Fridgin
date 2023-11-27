import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('1.9.0')


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def gen_random_number(self):
        self.random_label.text = str(random.randint(0, 100))


class Fridgin(App):

    def build(self):   #function to return UI
        #return Label(text = "Fridgin!") #This will be showed on UI
        return MyRoot()
    

fridgin = Fridgin()
fridgin.run()
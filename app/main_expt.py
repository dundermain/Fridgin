import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

import random

kivy.require('1.9.0')


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def gen_random_number(self):
        self.random_number.text = str(random.randint(0, 100))


class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text = "Name:"))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)



class Fridgin(App):

    def build(self):   #function to return UI
        #return Label(text = "Fridgin!") #This will be showed on UI
        #return MyRoot()
        return MyGrid()
    

fridgin = Fridgin()
fridgin.run()
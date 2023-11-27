#In this code we designed an app without design file (.kv) file


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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

        self.cols = 1                                   #number of columns in main layout
        self.inside = GridLayout()                      #grid layout inside the main layout
        self.inside.cols = 2                            #number of columns in the inner grid layout

        self.inside.add_widget(Label(text = "Name:"))   #add the first widget to innergrid layout
        self.name = TextInput(multiline = False)        #add the functions of second widget
        self.inside.add_widget(self.name)               #add the second widget to inner grid layout

        self.add_widget(self.inside)                    #add the inner grid layout to main layout

        self.submit = Button(text = 'Submit', font_size = 40) #add the UI for third widget
        self.submit.bind(on_press = self.pressed)             #add the functions of third widget
        self.add_widget(self.submit)                          #add the third widget to main layout

    def pressed(self, instance):

        name = self.name.text
        print("Name: ", name)
        self.name.text = ""



class Fridgin(App):

    def build(self):   #function to return UI
        #return Label(text = "Fridgin!") #This will be showed on UI
        #return MyRoot()
        return MyGrid()
    

fridgin = Fridgin()
fridgin.run()
#In this code we designed an app with design file (.kv) file


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


kivy.require('1.9.0')


class MyGrid(Widget):
    pass




class MyApp(App):

    def build(self):   #function to return UI
        #return Label(text = "Fridgin!") #This will be showed on UI
        #return MyRoot()
        return MyGrid()
    

MyApp().run()
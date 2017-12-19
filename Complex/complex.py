from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.lang import Builder

class One(FloatLayout):
    pass

class Two(GridLayout):
    pass
class Three(StackLayout):
    pass

class Main(GridLayout):
    pass

Builder.load_file("main.kv")

class Complex(App):


    def build(self):
        return Main()


if __name__ == "__main__":
    Complex().run()


from kivy.app  import  App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyFloat(FloatLayout):
    def foo(self):
        pass
    def myfunction(self,btn):
        if isinstance(btn,Button):
            print("On release from", btn.text)

class MyButton(Button):
    def downloadPicture(self):
        print("Downloading")
    def on_press(self):
        self.downloadPicture()
    def on_release(self):
        print("print finishing")

class SimpleInterface(App):
    def build(self):
        return MyFloat()

if __name__=="__main__":
    SimpleInterface().run()
from kivy.app import App
from kivy.uix.label import Label


def click_text(event):
    print(event)


class MyApp(App):
    def build(self):
        txt = Label(text='text')
        txt.on_touch_up = click_text
        return txt


app = MyApp()
app.run()
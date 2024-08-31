from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        btn = Button(text='press')
        txt = Label(text='text')
        text2 = Label(text='text2')
        btn.add_widget(Button(text='2'))
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        layout.add_widget(text2)
        return layout

MyApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        btn = Button(text='click to next page')
        self.add_widget(btn)

    def next_page(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
        
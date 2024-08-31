from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        btn = Button(text='click to next page')
        btn.on_press = self.next_page
        self.add_widget(btn)

    def next_page(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text='return page')
        btn.on_press = self.next_page
        self.add_widget(btn)

    def next_page(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.current='first'
        return sm


MyApp().run()
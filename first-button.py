from kivy.app import App
from kivy.uix.button import Button


def click_btn():
    print('click')


class MyApp(App):
    def build(self):
        self.title = 'My app'
        btn = Button(text='Press')
        btn.on_press = click_btn
        return btn


MyApp().run()

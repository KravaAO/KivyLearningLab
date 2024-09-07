from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button



class InstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst = Label(text='instruction coming soon')
        lbl_name = Label(text='type your name')
        self.name_input = TextInput(multiline=False)

        # додати вік                                         ДЗ!!!

        line1 = BoxLayout()
        line2 = BoxLayout(orientation='vertical')
        line1.add_widget(inst)
        line2.add_widget(lbl_name)
        line2.add_widget(self.name_input)
        btn = Button(text='start')
        btn.on_press = self.next_page
        line2.add_widget(btn)

        outer = BoxLayout(orientation='vertical')
        outer.add_widget(line1)
        outer.add_widget(line2)
        self.add_widget(outer)

    def next_page(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pulse1'

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst = Label(text='instruction coming soon for pg2')
        lbl_name = Label(text='type pulse')
        self.name_input = TextInput(multiline=False)

        # додати перевірку на число                                       ДЗ!!!

        line1 = BoxLayout()
        line2 = BoxLayout(orientation='vertical')
        line1.add_widget(inst)
        line2.add_widget(lbl_name)
        line2.add_widget(self.name_input)
        btn = Button(text='start')
        line2.add_widget(btn)

        outer = BoxLayout(orientation='vertical')
        outer.add_widget(line1)
        outer.add_widget(line2)
        self.add_widget(outer)


class Ruffier(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        return sm


app = Ruffier()
app.run()
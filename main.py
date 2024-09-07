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
        lbl_name = Label(text="Введіть ім'я")
        self.name_input = TextInput(multiline=False)
        lbl_age = Label(text="Введіть вік")
        self.age_input=TextInput(multiline=False)

        line1 = BoxLayout()
        line2 = BoxLayout()
        line3=BoxLayout()
        line1.add_widget(inst)
        line2.add_widget(lbl_name)
        line2.add_widget(self.name_input)
        line3.add_widget(lbl_age)
        line3.add_widget(self.age_input)

        btn = Button(text='start')
        btn.on_press = self.next_page

        outer = BoxLayout(orientation='vertical')
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(line3)
        outer.add_widget(btn)
        self.add_widget(outer)

    def next_page(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pulse1'

class PulseScr1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst = Label(text='instruction coming soon for pg2')
        lbl_name = Label(text='type pulse')
        self.name_input = TextInput(multiline=False)


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
    def next_page(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pulse2'

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst = Label(text='instruction coming soon for pg2')
        lbl_name = Label(text='type pulse')
        self.name_input = TextInput(multiline=False)


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
    def next_page(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Result'

class ResScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lbl_res1 = Label(text='self.name_input')
        lbl_res2 = Label(text="Ваш індекс Руф'є:")
        lbl_res3 = Label(text="Працездатність серця")


        line1 = BoxLayout()
        line1 = BoxLayout(orientation='vertical')
        line1.add_widget(lbl_res1)

        outer = BoxLayout(orientation='vertical')
        outer.add_widget(line1)
        self.add_widget(outer)

class Ruffier(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstScr(name='instr'))
        sm.add_widget(PulseScr1(name='pulse1'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(ResScr(name='Result'))
        return sm



app = Ruffier()
app.run()
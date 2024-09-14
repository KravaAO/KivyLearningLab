from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import instructions
from instructions import *


name=""
age=0
p1=0
p2=0
p3=0



class InstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst = Label(text=instructions.txt_instruction)
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

        btn = Button(text='Почати')
        btn.on_press = self.next_page

        outer = BoxLayout(orientation='vertical')
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(line3)
        outer.add_widget(btn)
        self.add_widget(outer)

    def next_page(self):
        global name , age
        name=self.name_input.text
        try:
            age=int(self.age_input.text)
            self.manager.transition.direction = 'left'
            self.manager.current = 'pulse1'
        except:
            error=Popup(title='Помилка', content=Label(text='Перевірте правильність вводу'), auto_dismiss=True, size_hint=(None,None), size=(300,300))
            error.open()

class PulseScr1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst = Label(text=instructions.txt_test1)
        lbl_p1 = Label(text='Введіть пульс')
        self.pulse_input = TextInput(multiline=False)


        line1 = BoxLayout()
        line2 = BoxLayout(orientation='vertical')
        line1.add_widget(inst)
        line2.add_widget(lbl_p1)
        line2.add_widget(self.pulse_input)
        btn = Button(text='Почати')
        line2.add_widget(btn)

        outer = BoxLayout(orientation='vertical')
        outer.add_widget(line1)
        outer.add_widget(line2)
        self.add_widget(outer)

        btn.on_press=self.next_page
    def next_page(self):
        global p1
        try:
            p1=int(self.pulse_input.text)
            self.manager.transition.direction = 'left'
            self.manager.current = 'squats'
        except:
            error=Popup(title='Помилка', content=Label(text='Перевірте правильність вводу'), auto_dismiss=True, size_hint=(None,None), size=(300,300))
            error.open()

class Squats(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = instructions.txt_test2)
        self.btn = Button(text = 'Наступна')
        line = BoxLayout(orientation='vertical')
        line.add_widget(instr)
        line.add_widget(self.btn)

        self.add_widget(line)
        self.btn.on_press = self.next_page

    def next_page(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst = Label(text=instructions.txt_test3)
        lbl_before = Label(text='Пульс до відпочинку:')
        lbl_after = Label(text='Пульс після відпочинку:')
        self.input_before = TextInput(multiline=False)
        self.input_after = TextInput(multiline=False)

        line1 = BoxLayout()
        line2 = BoxLayout()

        line1.add_widget(lbl_before)


        line1.add_widget(self.input_before)

        line2.add_widget(lbl_after)
        line2.add_widget(self.input_after)
        btn = Button(text='Результати')
        btn.on_press = self.next_page

        outer = BoxLayout(orientation='vertical')
        outer.add_widget(inst)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(btn)

        self.add_widget(outer)
    def next_page(self):
        global p2,p3
        try:
            p2=int(self.input_before.text)
            p3 = int(self.input_after.text)
            self.manager.transition.direction = 'left'
            self.manager.current = 'result'
        except:
            error=Popup(title='Помилка', content=Label(text='Перевірте правильність вводу'), auto_dismiss=True, size_hint=(None,None), size=(300,300))
            error.open()


class ResScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl_res1 = Label(text=name)
        lbl_res2 = Label(text="Ваш індекс Руф'є:")
        lbl_res3 = Label(text="Працездатність серця:")


        line1 = BoxLayout()
        line1 = BoxLayout(orientation='vertical')
        line1.add_widget(self.lbl_res1)
        line1.add_widget(lbl_res2)
        line1.add_widget(lbl_res3)
        self.on_enter=self.results
        self.add_widget(line1)
    def results(self):
        self.lbl_res1.text=name

class Ruffier(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstScr(name='instr'))
        sm.add_widget(PulseScr1(name='pulse1'))
        sm.add_widget(Squats(name='squats'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(ResScr(name='result'))
        return sm



app = Ruffier()
app.run()
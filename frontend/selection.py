from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout



class BoxLayoutEx(Screen):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = 'vertical'
    #     b1 = Button(text='A')
    #     b2 = Button(text='B')
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    def on_click(self):
        self.manager.current = 'selection'


class SelectionScreen(Screen):
    pass


class Selection(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BoxLayoutEx(name='example'))
        sm.add_widget(SelectionScreen(name='selection'))
        # select = SelectionScreen()
        return sm


if __name__ == '__main__':
    Selection().run()
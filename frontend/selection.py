from kivy.app import App
from kivy.uix.widget import Widget


class SelectionScreen(Widget):
    pass


class Selection(App):
    def build(self):
        select = SelectionScreen()
        return select

Selection().run()
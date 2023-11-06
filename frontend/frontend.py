from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from selection import SelectionScreen
Builder.load_file('./kvFiles/selection.kv')

from mainMenu import MainMenu
Builder.load_file('./kvFiles/mainMenu.kv')

from locationScreen import LocationScreen
Builder.load_file('./kvFiles/location.kv')


class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='Menu'))
        sm.add_widget(SelectionScreen(name='SelectScreen'))
        sm.add_widget(LocationScreen(name='LocationScreen'))

        return sm


if __name__ == '__main__':
    Main().run()
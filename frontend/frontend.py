from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from frontend.selection import SelectionScreen
Builder.load_file('frontend/kvFiles/selection.kv') # testing if this disappears

from frontend.mainMenu import MainMenu
Builder.load_file('frontend/kvFiles/mainMenu.kv')

from frontend.locationScreen import LocationScreen
Builder.load_file('frontend/kvFiles/location.kv')


class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='Menu'))
        sm.add_widget(SelectionScreen(name='SelectScreen'))
        sm.add_widget(LocationScreen(name='LocationScreen'))

        return sm


if __name__ == '__main__':
    Main().run()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from frontend.mainMenu import MainMenu
Builder.load_file('frontend/kvFiles/mainMenu.kv')

from frontend.locationScreen import LocationScreen, View, Add
Builder.load_file('frontend/kvFiles/location.kv')
Builder.load_file('frontend/kvFiles/viewLocs.kv')
Builder.load_file('frontend/kvFiles/add_locs.kv')

from frontend.soloView import Solo
Builder.load_file('frontend/kvFiles/solo.kv')


class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='Menu'))
        sm.add_widget(LocationScreen(name='LocationScreen'))
        sm.add_widget(View(name='viewLocs'))
        sm.add_widget(Add(name='add_locs'))
        sm.add_widget(Solo(name='solo'))

        return sm


if __name__ == '__main__':
    Main().run()
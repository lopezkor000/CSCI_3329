from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from backend.solo import Solo as soloPicker

class Solo(Screen):
    chooser = soloPicker()
    pick = ObjectProperty()
    def pickLocation(self):
        choice = self.chooser.totalRandom()[0]
        self.pick.text = choice
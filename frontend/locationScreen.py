from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import math

from backend.locations import Locations


class LocationScreen(Screen):
	pass

class View(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# self.locsList = TestLocations().someList
		self.add_widget(ViewLayout())
	
	def viewLocs(self):
		pass

class ViewLayout(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.items = 10
		self.cols = round(math.sqrt(self.items))

	def test(self):
		for i in range(self.items):
			self.add_widget(Label(text=str(i)))

class Add(Screen):
	locs = Locations()
	remove = ObjectProperty()
	add = ObjectProperty()
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import math

from backend.locations import Locations


class LocationScreen(Screen):
	pass


class ViewLayout(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.locs = Locations()
		self.items = len(self.locs.listedLocs())
		self.cols = round(math.sqrt(self.items))

	def update(self):
		self.clear_widgets()
		self.items = len(self.locs.listedLocs())
		self.cols = round(math.sqrt(self.items))
		for i in self.locs.listedLocs():
			self.add_widget(Label(text=i[0],
						 		  font_size=int((self.height + self.width)*0.02),))


class View(Screen):
	viewLayout = ViewLayout()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# self.add_widget(self.viewLayout)


class Add(Screen):
	locs = Locations()
	remove = ObjectProperty()
	add = ObjectProperty()
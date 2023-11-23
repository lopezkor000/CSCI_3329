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
		self.view = ViewLayout()
		self.add_widget(self.view)
	
	def refresh(self):
		self.view.update()

class ViewLayout(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.locs = Locations()
		self.items = len(self.locs.listedLocs())
		self.cols = round(math.sqrt(self.items))

	def update(self):
		self.clear_widgets()
		for i in self.locs.listedLocs():
			self.add_widget(Label(text=i[0],
						 		  font_size=int((self.height + self.width)*0.2),))

class Add(Screen):
	locs = Locations()
	remove = ObjectProperty()
	add = ObjectProperty()
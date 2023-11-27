from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MultiLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = 'horizontal'
		self.numUsers = TextInput(multiline=False,
								  font_size=int((self.height + self.width)*0.2),
								  hint_text='enter location',
								  halign='center',
								  padding_y=[self.height // 2, 0])
	
	def add(self):
		self.add_widget(Label(text=f'test {len(self.children)}'))

	def remove(self):
		if len(self.children) > 0:
			self.remove_widget(self.children[0])
	
	def countUsers(self):
		self.clear_widgets()
		self.add_widget(self.numUsers)
		self.add_widget(SubmitButton())


class SubmitButton(Button):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.text = 'Submit'
	
	def on_press(self, value):
		print(value)


class MultiSelect(Screen):
	multi = MultiLayout()
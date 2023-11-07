from kivy.uix.screenmanager import Screen

class MainMenu(Screen):
    def on_click(self):
        self.manager.current = 'SelectScreen'
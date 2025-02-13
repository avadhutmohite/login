from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size= (310, 580)
class main(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager
main().run()

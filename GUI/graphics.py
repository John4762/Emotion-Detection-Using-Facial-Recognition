import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import os

Builder.load_file('graphics.kv')

class ScreenOne(Screen):

	def callback(self):
		os.system('python C:/Users/hp/OneDrive/Desktop\MiniProject/Emotion-Detection-Using-Facial-Recognition/src/recognition.py')
	pass

class ScreenTwo(Screen):
	def callback(self):
		os.system('python C:/Users/hp/OneDrive/Desktop\MiniProject/Emotion-Detection-Using-Facial-Recognition/src/recognition.py')

	def showemotion(self):
		os.system('python C:/Users/hp/OneDrive/Desktop\MiniProject/Emotion-Detection-Using-Facial-Recognition/src/display.py')	
	pass

class ScreenThree(Screen):
	def musicplayer(self):
		os.system('python C:/Users/hp/OneDrive/Desktop\MiniProject/Emotion-Detection-Using-Facial-Recognition/music_app/main.py')		
	pass

class ScreenFour(Screen):
	pass

class ScreenFive(Screen):
	pass

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenOne(name ="screen_one")) 
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))
screen_manager.add_widget(ScreenFive(name ="screen_five"))

class ScreenApp(App):
	def build(self):
		return screen_manager

if __name__ == "__main__":
	sample_app = ScreenApp()
	sample_app.run()

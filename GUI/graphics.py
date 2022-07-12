import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os

Builder.load_file('graphics.kv')

class ScreenOne(Screen):
	def callback(self,instance):
		os.system('python E:/BTech/S6/MP/Music_Recomendation_System/Emotion-Detection-Using-Facial-Recognition/src/recognition.py')
	
	def __init__(self,**kwargs):
		super(ScreenOne, self).__init__(**kwargs)
		mybutton = Button(text = "Submit")
		mybutton.bind(on_release = self.callback) 
		self.add_widget(mybutton)

	pass

class ScreenTwo(Screen):
	pass

class ScreenThree(Screen):
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

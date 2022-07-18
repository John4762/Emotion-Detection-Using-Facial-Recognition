from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os

Builder.load_file('graphics.kv')

class ScreenOne(Screen):

	def callback(self):
		os.system('python src/recognition.py')
	def switch_screen(self):
		screen_manager.switch_to(ScreenTwo(name ="screen_two"))

class ScreenTwo(Screen):
	global screen_manager
	def switch_screen(self):
		screen_manager.switch_to(ScreenThree(name ="screen_three"))
	def on_pre_enter(self, *args):
		lab=self.ids["img_label"]
		lab.source='src/plainpic.jpg'

class ScreenThree(Screen):
	def musicplayer(self):
		os.system('python music_app/main.py')		
	def callemotion(self):
		f = open("result.txt", "r")
		emotion_result=f.read()
		f.close()

		lab=self.ids["emotion_label"]
		lab.text=emotion_result

	def on_enter(self, *args):
		self.callemotion()
		
class ScreenFive(Screen):
	def switch_screen(self):
		screen_manager.switch_to(ScreenOne(name ="screen_one"))
	pass

screen_manager = ScreenManager()
screen_manager.add_widget(ScreenOne(name ="screen_one")) 
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFive(name ="screen_five"))

class ScreenApp(App):
	def build(self):
		return screen_manager

if __name__ == "__main__":
	sample_app = ScreenApp()
	sample_app.run()

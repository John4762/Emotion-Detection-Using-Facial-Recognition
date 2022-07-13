import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
import os

Builder.load_file('emotion.kv')

class Button_Widget(Widget):

	def __init__(self, **kwargs):

		super(Button_Widget, self).__init__(**kwargs)

		btn1 = Button(text ='Submit', font_size ="15sp",
				background_color =(1, 1, 1, 1),
				color =(1, 1, 1, 1),
				# size =(32, 32),
				# size_hint =(.2, .2),
				pos =(300, 250))

		btn1.bind(on_release =self.callback )
		self.add_widget(btn1)

	def callback(self, instance):
		os.system('python C:/Users/hp/OneDrive/Desktop/MiniProject/Emotion-Detection-Using-Facial-Recognition/src/recognition.py')

class ButtonApp(App):

	def build(self):
		return Button_Widget()

if __name__ == "__main__":
	ButtonApp().run()

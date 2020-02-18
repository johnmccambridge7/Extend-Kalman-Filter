#!/usr/bin/env python
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ControlScreen(GridLayout):
	def __init__(self, **kwargs):
		super(ControlScreen, self).__init__(**kwargs)
		self.cols = 2

		forwardBtn = Button(text='Forward')
		backwardBtn = Button(text='Backward')
		leftBtn = Button(text='Left')
		rightBtn = Button(text='Right')

		self.add_widget(forwardBtn)
		self.add_widget(backwardBtn)
		self.add_widget(leftBtn)
		self.add_widget(rightBtn)

class MyApp(App):
	def build(self):
		self.title = 'ROS-bot controller - John McCambridge'
		return ControlScreen()

if __name__ == '__main__':
	MyApp().run()


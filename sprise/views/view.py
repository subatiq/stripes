import os
import re



class View:
	def __init__(self):
		self._view = ""
		self.backgroundColor = "#CCCCCC"

		self.width = 'auto'
		self.height = 'auto'

	def Color(self, hex = "#000000"):
		self.backgroundColor = hex
		return self

	def Size(self, width='auto', height='auto'):
		self.width, self.height = width, height
		return self

	def apply(self, style):
		return self._view.replace("$sprise-style$", style)

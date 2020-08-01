import os
import re



class View:
	def __init__(self):
		self._view = ""
		self.backgroundColor = "#CCCCCC"

		self.width = 'auto'
		self.height = 'auto'

	def fill(self, hex = "#000000"):
		self.backgroundColor = hex
		return self

	def size(self, width='auto', height='auto'):
		self.width, self.height = width, height
		return self

	def apply(self, style):
		return self._view.replace("$splice-style$", style)

from sprise.views.renderer import open_template, render_view
from sprise.views.view import View
from sprise.views.stacks import ZStack
from sprise.views.text import Text

class Rectangle(View):
	def __init__(self):
		super().__init__()
		self._view = open_template('rectangle')	
		self.color = "#000000"
		self.borderRadius = "5px"

		self._text = ""

	def CornersRadius(self, radius):
		self.CornerRadiusSpecify(radius, radius, radius, radius)
		return self

	def CornerRadiusSpecify(self, lt=5, rt=5, rb=5, lb=5):
		radiuses = " ".join(f"{radius}px" for radius in [lt, rt, rb, lb])
		self.borderRadius = radiuses
		return self

	def Text(self, text):
		
		view = render_view(ZStack(self, Text(text)._view))
		text = Text(text)
		text._view = view

		return text
	
	def TextColor(self, hex):
		self.color = hex
		
		return self

	def apply(self, style):
		return super().apply(style)\
			.replace("$text$", self._text)

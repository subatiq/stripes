from sprise.views.renderer import open_template, render_view
from sprise.views.view import View


class Stack(View):
	def __init__(self, *views, stack_type = ""):
		self._view = open_template(stack_type)
		self._body= "\n".join([render_view(view) if not type(view) is str else view for view in views[0]])

	def apply(self, style):
		return self._view.replace("$sprise-style$", style).replace("$body$", self._body) 


class VStack(Stack):
	def __init__(self, *views):
		super().__init__(views, stack_type = 'vstack')

		self.marginTop = 0


	def Spacing(self, value):
		self.marginTop = value
		return self


class HStack(Stack):
	def __init__(self, *views):
		super().__init__(views, stack_type = 'hstack')
		self.marginRight = 0

	def Spacing(self, value):
		self.marginRight = value
		return self


class ZStack(Stack):
	def __init__(self, *views):
		super().__init__(views, stack_type = 'zstack')


from splice.views.renderer import get_tag, open_template
from splice.views.view import View

class Text(View):
	def __init__(self, text):
		super().__init__()
		self._view = self._view = open_template('text')
		self.color = "#000000"
		self.backgroundColor = "none"
		self._text = text
		self._tag = "p"
		self._caseBackup = self._text

	def font(self, style):
		self._tag = style
		return self

	def upper(self):
		self._text = self._text.upper()
		return self

	def lower(self):
		self._text = self._text.lower()
		return self

	def foregroundColor(self, hex):
		self.color = hex
		return self

	def apply(self, style):
		return super().apply(style)\
			.replace("$style-tag$", self._tag)\
			.replace("$text$", self._text)
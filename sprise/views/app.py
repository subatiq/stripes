from sprise.views.renderer import render_view, open_template
from sprise.views.view import View

class App(View):
        def __init__(self, *views):
                self._template = open_template('body')
                self._views = views

        def render(self):
                rendered = "\n".join([render_view(view) if type(view) is not str else view for view in self._views])
                self._view = self._template.replace("$sprise$", rendered)
                return render_view(self)


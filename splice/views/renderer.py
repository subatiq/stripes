import re
import os

base_path = os.path.abspath(os.path.dirname(__file__))


def get_tag(name, closing=False):
	return f"<{name}>" if not closing else f"</{name}>"


def open_template(name):
	template_path = os.path.join(base_path, f"templates/{name}.html")
	template_file = open(template_path, "r")
	template = template_file.read()
	template_file.close()

	return template


def render_app(body):
	template = open_template('body')

	return template.replace("$splice$", body)


def render_view(view):
	style = f""

	for property in view.__dict__:
		if property.startswith("_"):
			continue

		css_property = re.sub(r'(?<!^)(?=[A-Z])', '-', property).lower()
		style += f"{css_property}: {view.__dict__[property]}; "

	return view.apply(style)


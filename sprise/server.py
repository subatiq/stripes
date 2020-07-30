from flask import Flask
from sprise.views.renderer import render_app

try:
	from settings import main_page
except ImportError:
	main_page = 'app'

page = __import__(main_page)
app = Flask(__name__)

@app.route('/')
def hello_world():
	return page.body.render()


if __name__ == '__main__':
	app.run()
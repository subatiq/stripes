from flask import Flask
from page_example import body
from sprise.views.renderer import render_app

app = Flask(__name__)

@app.route('/')
def hello_world():
	return body.render()


if __name__ == '__main__':
	app.run()
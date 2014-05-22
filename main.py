from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
	html = get_html()
	print('Incoming request, bitches')
	return Response(html)


def get_html():
	html = ''
	f = open('index.html')
	for line in f:
		html += line
	return html

if __name__ == '__main__':
	config = Configurator()
	config.add_route('hello', '/')
	config.add_view(hello_world, route_name='hello')
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 6545, app)
	server.serve_forever()

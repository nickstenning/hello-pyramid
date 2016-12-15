from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(route_name='index', renderer='templates/index.html.jinja2')
def index(request):
    return {}


def create_app():
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_route('index', '/')
    config.add_static_view(name='static', path='static')
    config.scan()
    return config.make_wsgi_app()

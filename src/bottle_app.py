# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run


@route('/')
def hello_world():
    return 'Hello from Bottle Test déploiement 1 !'


application = default_app()

run()


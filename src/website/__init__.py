from .app import app


def get_app(environ, start_response):
    return app
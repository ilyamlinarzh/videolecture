from flask import Flask

from src.exceptions import handler_ValidationError, handler_500, handler_404, handler_Exception
from pydantic import ValidationError


def init_exc_handlers(app: Flask):
    handlers = [
        (ValidationError, handler_ValidationError),
        (500, handler_500),
        (404, handler_404),
        (Exception, handler_Exception)
    ]

    for handler_type, handler_f in handlers:
        app.register_error_handler(handler_type, handler_f)

    return app

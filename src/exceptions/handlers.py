from flask import jsonify
from pydantic import ValidationError


def handler_ValidationError(err: ValidationError):
    errors = err.errors()
    err_msg = "Переданы неверные данные: " + "; ".join([f'{".".join(e["loc"])} ([{e["type"]}] {e["msg"]})' for e in errors])
    return jsonify(
        dict(
            message=err_msg,
            error=True
        )
    ), 400


def handler_500(err: BaseException):
    return jsonify(
        dict(
            message=str(err),
            error=True
        )
    ), 400


def handler_404(err):
    return jsonify(
        dict(
            message="[404] Not Found",
            error=True
        )
    ), 404


def handler_Exception(err: Exception):
    return jsonify(
        dict(
            message=str(err),
            error=True
        )
    ), 400
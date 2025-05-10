from flask import Blueprint, jsonify

bp = Blueprint('other', __name__)


@bp.get('/ping')
def ping_pong():
    return jsonify(
        dict(
            error=False,
            message="Pong",
            result=True
        )
    )
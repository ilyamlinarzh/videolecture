from flask import Blueprint, current_app, jsonify
from .schemas import GenerateRequestSchema

from src.lib.decorators import validator
from .services import process_generation_method, kill_process


bp = Blueprint('generate', __name__)


@bp.post('/')
@validator(GenerateRequestSchema)
def generation_method(data: GenerateRequestSchema):
    tts = current_app.tts_model
    sadtalker = current_app.sadtalker_model
    info = process_generation_method(
        data=data,
        tts_model=tts,
        sadtalker_model=sadtalker
    )

    print(info)

    if not info:
        return jsonify(
            dict(
                error=True,
                message="Генерация уже запущена. Дождитесь её завершения или отмените"
            )
        )

    return jsonify(
        dict(
            error=False,
            message='Процесс запущен',
            result=info
        )
    )


@bp.get('/cancel')
def gen_cancel_method():
    result = kill_process()
    return jsonify(
        dict(
            error=False,
            result=result,
            message=("Генерация остановлена" if result else "Не удалось остановить генерацию")
        )
    )
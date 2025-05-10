from functools import wraps
from flask import request, jsonify

from pydantic import ValidationError, BaseModel



def validator(model: type[BaseModel]):
    """
    Проверяет переданный в тело POST-запроса JSON объект на соответствие заданной pydantic-модели.
    Передает в виде сущности модели в роут-метод как параметр **data**
    :param model: Pydantic-модель для валидации
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Парсим JSON и валидируем через Pydantic
                data = request.get_json()
                if not data:
                    return jsonify({"error": "No JSON data provided"}), 400

                validated_data = model(**data)
                kwargs["data"] = validated_data

                return func(*args, **kwargs)
            except ValidationError as e:
                raise e
                # return jsonify({"error": "Validation failed", "details": e.errors()}), 400
        return wrapper
    return decorator

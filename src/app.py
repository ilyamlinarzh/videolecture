from flask import Flask
from ml import create_xtts_model, SadTalker


from recources.other.router import bp as other_bp
from recources.generation.router import bp as gen_bp

from src.init_exception_handlers import init_exc_handlers

from config import Config


def create_app() -> Flask:
    app = Flask(__name__)

    tts_model = create_xtts_model()
    # tts_model = None
    app.tts_model = tts_model

    sadtalker_model = SadTalker(
        python_path=Config.SAD_TALKER_PYTHON_PATH,
        execute_file_path=Config.SAD_TALKER_INFERENCE,
        sadtalker_dir_path=Config.SAD_TALKER_DIR_PATH
    )
    app.sadtalker_model = sadtalker_model

    app.register_blueprint(other_bp, url_prefix='/')
    app.register_blueprint(gen_bp, url_prefix='/generation')

    init_exc_handlers(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=54547,
        debug=True
    )
    # можно запустить app.py прям из пайчарма, позже разберемся с запуском с консоли
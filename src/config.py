from dataclasses import dataclass
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

_relative_paths = {
    "python3.8": "../SadTalker/venv/bin/python",
    "inference.py": "../SadTalker/inference.py",
    "sadtalker_dir": "../SadTalker",
    "logs": "./logs"
}


@dataclass
class Config:
    SAD_TALKER_PYTHON_PATH = os.path.normpath(os.path.join(BASE_DIR, _relative_paths['python3.8'])) # путь до python под запуск sadtalker
    SAD_TALKER_INFERENCE = os.path.normpath(os.path.join(BASE_DIR, _relative_paths['inference.py']))
    SAD_TALKER_DIR_PATH = os.path.normpath(os.path.join(BASE_DIR, _relative_paths['sadtalker_dir']))

    # Разделитель между частями текста в передаваемом файле с расшифровкой лекции
    LECTURES_TEXT_DELIMITER = '_;'

    LOGS_DIR_PATH = os.path.normpath(os.path.join(BASE_DIR, _relative_paths['logs']))
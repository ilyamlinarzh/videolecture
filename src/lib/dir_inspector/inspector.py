import os
from pathlib import Path


def validate_generated_dir(directory_path: str) -> bool:
    required_folders = [
        'audio_fragments',
        'video_fragments',
        'combined',
        'final'
    ]
    try:
        base_path = Path(directory_path)

        for folder in required_folders:
            folder_path = base_path / folder
            folder_path.mkdir(exist_ok=True)

        return True

    except Exception as e:
        raise Exception("Проблемы с файловой системой. Проверьте директорию /generated")
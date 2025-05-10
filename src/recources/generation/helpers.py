import re
from src.config import Config


def __split_text_advanced(
        text: str,
        sentences_per_part: int = 5,
        words_fallback: int = 65
) -> list[str]:
    normalized_text = ' '.join(text.split())

    sentences = re.split(r'(?<=[.!?])\s+', normalized_text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) > 1:
        parts = [
            ' '.join(sentences[i:i + sentences_per_part])
            for i in range(0, len(sentences), sentences_per_part)
        ]
    else:
        words = normalized_text.split()
        parts = [
            ' '.join(words[i:i + words_fallback])
            for i in range(0, len(words), words_fallback)
        ]

    return parts


def split_lecture_text(lecture_text_path: str):
    lecture = []
    with open(lecture_text_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lecture += content.split(Config.LECTURES_TEXT_DELIMITER)

    lecture_parted = [__split_text_advanced(slide_part) for slide_part in lecture]
    return lecture_parted

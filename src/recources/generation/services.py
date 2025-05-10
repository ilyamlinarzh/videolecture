import threading
from .schemas import GenerateRequestSchema
from .helpers import split_lecture_text
from src.lib import validate_generated_dir

from src.ml import SadTalker

from src import logger

event = threading.Event()
gen_process: threading.Thread = None


def process_generation_method(
        *,
        data: GenerateRequestSchema,
        tts_model: "TTS",
        sadtalker_model: SadTalker
):
    global gen_process
    global event

    if gen_process is not None and gen_process.is_alive():
        return False

    text_parts = split_lecture_text(data.lecture_text_path)
    parts_count = sum([len(sp) for sp in text_parts])
    logger.info(f"Определено {parts_count} частей для генерации")
    validate_generated_dir(data.generated_dir_path)

    event.clear()
    gen_process = threading.Thread(target=process_generation_method_thread, args=(
        data,
        text_parts,
        parts_count,
        tts_model,
        sadtalker_model
    ))
    gen_process.start()

    slides_chunks = []
    n = 1
    for slide in text_parts:
        sl = []
        for _ in slide:
            sl.append(n)
            n += 1

        slides_chunks.append(sl)

    return slides_chunks


def process_generation_method_thread(
        data: GenerateRequestSchema,
        text_parts: list[list[str]],
        parts_count: int,
        tts_model: "TTS",
        sadtalker_model: SadTalker
):
    process_generate_audio(
        text_parts=text_parts,
        voice_path=data.voice_path,
        generated_dir_path=data.generated_dir_path,
        id=data.id,
        tts_model=tts_model
    )

    process_generate_video(
        generated_dir_path=data.generated_dir_path,
        face_path=data.face_path,
        parts_count=parts_count,
        id=data.id,
        sadtalker_model=sadtalker_model
    )


def process_generate_audio(
        *,
        text_parts: list[list[str]],
        voice_path: str,
        generated_dir_path: str,
        id: int,
        tts_model: "TTS"
):
    i = 1
    for slide_part in text_parts:
        for part in slide_part:
            logger.info(f"START GENERATE audio_fragment_{id}_{i}")
            tts_model.tts_to_file(
                text=part,
                file_path=f"{generated_dir_path}/audio_fragments/audio_fragment_{id}_{i}.wav",
                split_sentences=False,
                speaker_wav=voice_path,
                language="ru"
            )
            i += 1


def process_generate_video(
        *,
        generated_dir_path: str,
        face_path: str,
        parts_count: int,
        id: int,
        sadtalker_model: SadTalker
):
    for i in range(1, parts_count + 1):
        logger.info(f"START GENERATE video_fragment_{id}_{i}\n")
        res = sadtalker_model.inference(
            audio_path=f'{generated_dir_path}/audio_fragments/audio_fragment_{id}_{i}.wav',
            image_path=face_path,
            output_filename_base=f'video_fragment_{id}_{i}',
            result_path=f'{generated_dir_path}/video_fragments',
            config=dict(
                still=False
            )
        )

        for info in res.stdout:
            logger.info(info)
        for err in res.stderr:
            logger.error(err)

        print(res)


def kill_process():
    global gen_process
    global event

    if gen_process and gen_process.is_alive():
        event.set()
        return True

    return False

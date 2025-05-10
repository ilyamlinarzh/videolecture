from pydantic import BaseModel


class GenerateRequestSchema(BaseModel):
    face_path: str
    voice_path: str
    lecture_text_path: str
    generated_dir_path: str
    id: int
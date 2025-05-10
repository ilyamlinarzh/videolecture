import torch
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs  # Добавляем XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig

torch.serialization.add_safe_globals([XttsConfig, XttsAudioConfig, XttsArgs, BaseDatasetConfig])


def create_xtts_model():
    device = None
    if torch.backends.mps.is_available():
        device = "mps"  # Mac GPU (Apple Silicon)
    elif torch.cuda.is_available():
        device = "cuda"  # windows/linux gpu
    else:
        device = "cpu"  # cpu

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=(device == 'cuda')).to(device)

    if device == 'mps':
        tts = tts.float()

    return tts

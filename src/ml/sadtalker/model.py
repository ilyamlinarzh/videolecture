import subprocess
import os
from .helpers import rename_result
from .schemas import SadTalkerInferenceConfig
from src.lib import cmd_format


class SadTalker:
    def __init__(
            self,
            python_path: str,
            execute_file_path: str,
            sadtalker_dir_path: str
    ):
        self.python_path = python_path
        self.execute_file_path = execute_file_path
        self.sadtalker_dir_path = sadtalker_dir_path

    def inference(
            self,
            audio_path: str,
            image_path: str,
            output_filename_base: str,
            result_path: str = None,
            config: SadTalkerInferenceConfig = None
    ):
        result_command_part = []
        if result_path is not None:
            result_command_part += ["--result_dir", result_path]

        command_rules = [
            "--driven_audio", audio_path,
            "--source_image", image_path,
            *result_command_part,
            *cmd_format(config)
        ]

        result = self.__subprocess_run(command_rules)
        if result.returncode == 0:
            rename_result(result_path, output_filename_base)

        return result

    def __subprocess_run(self, command_rules: list[str]):
        return subprocess.run(
            [
                self.python_path,
                self.execute_file_path,
                *command_rules
            ],
            cwd=self.sadtalker_dir_path,
            env={
                **os.environ,
                "PYTHONPATH": self.sadtalker_dir_path
            },
            stderr=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            text=True
        )

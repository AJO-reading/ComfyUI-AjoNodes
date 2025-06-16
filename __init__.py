import random
import folder_paths
import torch
from comfy_extras.nodes_audio import SaveAudio as OriginalSaveAudio
from comfy_execution.graph import ExecutionBlocker  # Nécessaire pour le blocage conditionnel
from .vfi_utils import AJO_VfiSkipListCalculator


class AJO_SaveAudio:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                "filename_prefix": ("STRING", {"default": "audio/ComfyUI"}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    RETURN_TYPES = ()
    FUNCTION = "save_audio"
    OUTPUT_NODE = True
    CATEGORY = "audio"

    def save_audio(self, audio, filename_prefix="ComfyUI", prompt=None, extra_pnginfo=None):
        if isinstance(audio, torch.Tensor) and audio.size(0) == 0:
            return ("",)
        sa = OriginalSaveAudio()
        return sa.save_audio(audio, filename_prefix, prompt, extra_pnginfo)


class AJO_PreviewAudio(AJO_SaveAudio):
    def __init__(self):
        self.output_dir = folder_paths.get_temp_directory()
        self.type = "temp"
        self.prefix_append = "_temp_" + "".join(random.choice("abcdefghijklmnopqrstupvxyz") for _ in range(5))

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }


class AJO_AudioCollectAndConcat:
    collected_audio = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                "expected_count": ("INT", {"default": 1, "min": 1, "max": 999}),
            }
        }

    RETURN_TYPES = ("AUDIO", "INT")
    RETURN_NAMES = ("concatenated_audio", "collected_count")
    FUNCTION = "collect_and_concat"
    CATEGORY = "audio"

    def collect_and_concat(self, audio, expected_count):
        self.__class__.collected_audio.append(audio)
        current_count = len(self.__class__.collected_audio)

        if current_count < expected_count:
            return (ExecutionBlocker(None), current_count)

        sample_rate = audio["sample_rate"]
        waveforms = []
        for idx, audio_dict in enumerate(self.__class__.collected_audio):
            if audio_dict["sample_rate"] != sample_rate:
                raise ValueError(
                    f"Sample rate mismatch at index {idx}: {audio_dict['sample_rate']} vs {sample_rate}"
                )
            waveforms.append(audio_dict["waveform"])

        concatenated_waveform = torch.cat(waveforms, dim=-1)
        self.__class__.collected_audio.clear()

        return ({"waveform": concatenated_waveform, "sample_rate": sample_rate}, current_count)


__nodes__ = [AJO_AudioCollectAndConcat]  # Disabled AJO_PreviewAudio and AJO_SaveAudio

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
    "AJO_AudioCollectAndConcat": AJO_AudioCollectAndConcat,
    # "AJO_PreviewAudio": AJO_PreviewAudio,  # Disabled
    # "AJO_SaveAudio": AJO_SaveAudio,        # Disabled
    "AJO_VfiSkipListCalculator": AJO_VfiSkipListCalculator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AJO_AudioCollectAndConcat": "🔊 Audio Collect & Concat",
    # "AJO_PreviewAudio": "🔈 Preview Audio",  # Disabled
    # "AJO_SaveAudio": "💾 Save Audio"         # Disabled
    "AJO_VfiSkipListCalculator": "VFI Frame Skip Calculator (AJO)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

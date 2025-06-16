# ComfyUI-AjoNodes/vfi_utils.py

import math

class AJO_VfiSkipListCalculator:
    """Calculate a frame skip list for RIFE style VFI."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "source_fps": ("INT", {"default": 16, "min": 1, "max": 240, "step": 1}),
                "target_fps": ("INT", {"default": 25, "min": 1, "max": 240, "step": 1}),
                "total_input_frames": ("INT", {"default": 160, "min": 1, "max": 99999, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("skip_list_string", "rife_multiplier")
    FUNCTION = "calculate_skip_list"
    CATEGORY = "AJO-Nodes/VFI"

    def calculate_skip_list(self, source_fps, target_fps, total_input_frames):
        # No interpolation needed if target fps is less or equal to source fps
        if target_fps <= source_fps:
            return ("", 1)

        # For now we only handle up to 2x interpolation.
        base_multiplier = 2
        if target_fps > source_fps * base_multiplier:
            print(
                f"AJO VFI Node WARNING: Cannot achieve {target_fps} from {source_fps} with a 2x multiplier. More complex interpolation needed."
            )
            return ("", base_multiplier)

        # Calculate how many interpolated frames would exist at 2x
        total_frames_at_2x = total_input_frames * base_multiplier
        total_interpolations_possible_at_2x = total_frames_at_2x - total_input_frames

        # Desired total frames for target fps
        desired_total_frames = math.ceil(total_input_frames * (target_fps / source_fps))
        interpolations_to_skip = total_frames_at_2x - desired_total_frames

        # Generate skip list string
        skip_list_string = ""
        if interpolations_to_skip > 0 and total_interpolations_possible_at_2x > 0:
            skip_interval = total_interpolations_possible_at_2x / interpolations_to_skip
            skipped_indices = []
            for i in range(1, int(interpolations_to_skip) + 1):
                skipped_indices.append(round(i * skip_interval))
            skip_list_string = ",".join(map(str, skipped_indices))

        return (skip_list_string, base_multiplier)

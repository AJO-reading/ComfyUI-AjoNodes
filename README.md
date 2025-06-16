# ComfyUI-AjoNodes

A collection of custom nodes designed for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) from the **AJO-reading** organization. It ships with utilities for audio processing and video frame interpolation.

## Features

- **Audio Collect & Concat**
  - Collects multiple audio inputs.
  - Concatenates audio segments into one continuous output.
  - Checks for sample rate mismatches and raises an error if found.
- **VFI Frame Skip Calculator**
  - Generates a skip list for frame interpolation tools like RIFE.
  - Outputs the required interpolation multiplier alongside the list.

## Folder Structure

```
ComfyUI-AjoNodes/
├── __init__.py            # Main module defining the custom nodes.
├── README.md              # This file.
├── vfi_utils.py           # VFI skip list calculator node.
├── docs/                  # Optional documentation assets (images, etc.)
└── web/
    └── ajo_widgets.js     # JavaScript extension for handling node widgets.
```

## Requirements

- **Python 3.x**
- [PyTorch](https://pytorch.org/) – for tensor operations.
- ComfyUI dependencies:
  - `comfy_extras` (for audio utilities)
  - `comfy_execution` (for execution management)
- Ensure you have ComfyUI installed and properly configured before adding custom nodes.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AJO-reading/ComfyUI-AjoNodes.git
   ```

2. **Place the custom node files in your ComfyUI installation:**

   Typically, custom nodes reside in a specific directory within your ComfyUI installation—consult the ComfyUI documentation for details.

3. **Restart ComfyUI** to load the new nodes.

## Usage

Once installed, you will see two categories of AJO nodes inside ComfyUI.

### Audio Collect & Concat
- **Location:** Appears under the `audio` category.
- **Input:** Provide the audio tensor and the expected number of segments.
- **Output:** The concatenated audio and a count of collected segments.

### VFI Frame Skip Calculator
- **Location:** Found under `AJO-Nodes/VFI`.
- **Inputs:**
  - `source_fps` – the frame rate of your input video.
  - `target_fps` – the desired frame rate after interpolation.
  - `total_input_frames` – number of frames in the original clip.
- **Outputs:**
  - `skip_list_string` – a comma-separated list of interpolation indices to skip.
  - `rife_multiplier` – the base multiplier for your VFI node (typically `2`).

### Adding Example Images
Place screenshots or other assets inside the `docs/` directory. You can then
embed them in this README using standard Markdown:

```markdown
![VFI Example](docs/vfi_example.png)
```

Commit the image file along with your changes so it appears on GitHub.

## Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch for your changes, and submit a pull request. Let's innovate together under the AJO-reading banner!

## License

This project is using the MIT License.

## Acknowledgements

- Thanks to the ComfyUI community for their ongoing work.
- Proudly developed by the AJO-reading organization.
- With assistance from @Verevolf, @melmass (MTB) and @manu_le_surikhate_gamer


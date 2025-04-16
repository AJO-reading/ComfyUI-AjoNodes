# ComfyUI-AjoNodes

A collection of custom nodes designed for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) from the **AJO-reading** organization. This repository currently includes the **Audio Collect & Concat** node, which collects multiple audio segments and concatenates them into a single audio stream.

## Features

- **Audio Collect & Concat**
  - Collects multiple audio inputs.
  - Concatenates audio segments into one continuous output.
  - Checks for sample rate mismatches and raises an error if found.

## Folder Structure

```
ComfyUI-AjoNodes/
├── __init__.py            # Main module defining the custom nodes.
├── README.md              # This file.
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

Once installed, you can find the **Audio Collect & Concat** node in the "audio" category within ComfyUI. It is designed to be straightforward:
- **Input:** Provide the audio input and an expected count of audio segments.
- **Output:** Receives the concatenated audio and the count of collected segments.

## Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch for your changes, and submit a pull request. Let's innovate together under the AJO-reading banner!

## License

This project is using the MIT License.

## Acknowledgements

- Thanks to the ComfyUI community for their ongoing work.
- Proudly developed by the AJO-reading organization.
- With assistance from @Verevolf, @melmass (MTB) and @manu_le_surikhate_gamer


# TGC Toolbox

This repository contains a comprehensive toolbox with all of the utils and tools used in various TGC projects. It is more of a collection of tools than a library and will not be as well documented as a library. It is recommended to use this toolbox only if you are familiar with the tools and their usage.

If you want to contribute to the toolbox, please refer to the [Contributing](#contributing) section below and [Builiding package on contribution](#builiding-package-on-contribution) for building the package after making changes. Please make sure to follow those guidelines when submitting a pull request.

- [TGC Toolbox](#tgc-toolbox)
  - [Modules](#modules)
    - [logger.py](#loggerpy)
    - [downloaders.py](#downloaderspy)
    - [ffmpeg.py](#ffmpegpy)
    - [vosk.py](#voskpy)
    - [operations.py](#operationspy)
    - [recorder.py](#recorderpy)
  - [Installation](#installation)
  - [Optional Features](#optional-features)
    - [Audio Support](#audio-support)
    - [Installing the TGC Toolbox with Audio Support](#installing-the-tgc-toolbox-with-audio-support)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Builiding package on contribution](#builiding-package-on-contribution)

## Modules

### `logger.py`

This module provides logging utilities. It includes the following functions and classes:

- `TGCLoggerSetup`: Sets up a custom logger.
- `TGCLogResult`: Logs the result of an operation.
- `log_result`: Alias for `TGCLogResult`.
- `TGCLogger`: A custom logger class.
- `TGCResultsLogger`: A custom logger class for logging results.
- `TGCLoggerFormatter`: A custom formatter for the logger.

### `downloaders.py`

This module provides utilities for downloading files. It includes the following functions:

- `download_vosk_model`: Downloads the Vosk model.
- `download_file`: Downloads a file from a given URL.
- `download_youtube`: Downloads a YouTube video as a WAV file.
- `download_video_as_wav`: Alias for `download_youtube`.

### `vosk.py`

This module provides utilities for working with Vosk. It includes the following functions and classes:

- `transcribe_vosk`: Transcribes streaming audio using vosk. This function is a generator that yields transcriptions. You need to pass pre-instantiated vosk `Model` and `KaldiRecognizer`.

### `ffmpeg.py`

This module provides utilities for working with FFmpeg.

### `operations.py`

This module provides various operations.

### `recorder.py`

This module provides a recorder function for testing. Be warned that this function is not robust at all.

### `sound.py`

This module provides utilities for working with sound.

### `wrappers.py`

This module provides various wrappers.

## Installation

To install the TGC Toolbox, the prefered way is to use [poetry](https://python-poetry.org/docs/#installation):

```shell
poetry add git+https://github.com/TwoGuysCoding/TGCToolbox.git#main
```

This will add the TGC Toolbox to your `pyproject.toml` file and install it in your virtual environment.
Note that it installs from a private repo and thus you must first set up your GitHub identification. Then, you can install the package by running:
  
```shell
poetry install
```

Alternatively, you can use pip to install directly from the source:

```plaintext
pip install git+https://github.com/TwoGuysCoding/tgc-toolbox.git#egg=tgc_toolbox
```

WARNING: Install with pip uses the legacy version of this package, meaning it is not recommended and may not be supported.

This will install the TGC Toolbox and all of its necessary Python dependencies directly from the private GitHub repository.

Alternatively, you can clone the repository and install it locally:

```bash
git clone https://github.com/TwoGuysCoding/tgc-toolbox.git
cd tgc-toolbox
pip install .
```

This will install the TGC Toolbox and all of its necessary Python dependencies from the local repository.

## Optional Features

### Audio Support

The TGC Toolbox offers optional audio functionalities which require additional dependencies, including the pyaudio package, which in turn requires system-level installation of PortAudio.

Installing System Dependencies for Audio Support:

- **Linux (Debian/Ubuntu)**

```bash
sudo apt-get install portaudio19-dev
```

- **macOS**

```bash
brew install portaudio
```

- **Windows**

The necessary PortAudio binaries are typically included with the PyAudio package, so no additional installation should be required.

### Installing the TGC Toolbox with Audio Support

To include audio functionalities when installing from the private GitHub repository, you can specify the audio extras:

- With Poetry:

```shell
poetry add git+https://github.com/TwoGuysCoding/TGCToolbox.git#main[audio]
```

- With pip:

```plaintext
pip install "git+https://github.com/TwoGuysCoding/tgc-toolbox.git#egg=tgc_toolbox[audio]"
```

When installing from the local repository, you can specify the audio extras as well:

```bash
pip install ".[audio]"
```

Please note that audio functionalities are optional and only needed if you plan to use the audio-related features within the TGC Toolbox.

## Usage

To use a function or class from the toolbox, import it from the tgc_toolbox package. For example, to use the TGCLoggerSetup function, you would do:

```python
from tgc_toolbox import TGCLoggerSetup
```

Then, you can call the function as you normally would:

```python
logger = TGCLoggerSetup('my_logger')
```

Please refer to the individual modules for more information on how to use the functions and classes they provide.

## Contributing

If you would like to contribute to the toolbox, please create a pull request with your changes. Make sure to include a detailed description of the changes you made and why you made them. Your pull request will be reviewed by the maintainers before being merged.
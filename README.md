# WhatTheFormat

WhatTheFormat is a Python program that uses `yt-dlp` and `ffmpeg` to download and convert a YouTube video's audio to the desired format, all in one swing. The program can be run either from the command line, via a graphical user interface (GUI), or through the application.

## Installation

In order to use this program, you must have `yt-dlp` and `ffmpeg` installed on your system. You can install them by running `python -m pip install -r requirements.txt` in the terminal.

## Usage

### Command Line

To use the program from the command line, run:

```
python wtfmt.py <link> <filename>
```


Where `<link>` is the YouTube link of the video you want to convert and `<filename>` is the desired output filename (with format).

### GUI

To use the program via the graphical user interface, run:

```
python wtfmt.py --gui
```

This will open a window where you can enter the YouTube link and the desired output filename.

### Application

- Windows : When using wtfmt.exe, replace `python wtfmt.py` with `wtfmt.exe`, and pass arguments as usual.
- Linux : When using wtfmt, replace `python wtfmt.py` with `./wtfmt`, and pass arguments as usual.
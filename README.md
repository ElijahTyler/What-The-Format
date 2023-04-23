# WhatTheFormat

WhatTheFormat is a Python program that uses `yt-dlp` and `ffmpeg` to download and convert a YouTube video to the desired format, all in one swing. The program can be run either from the command line, via a graphical user interface (GUI), or through the application.

## Installation

1. Click on Code -> Download ZIP and extract wherever you like
2. Open Terminal in the project directory and run `python -m pip install -r requirements.txt`

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

When using wtfmt.exe, replace
```
python wtfmt.py
```
with
```
Windows:
wtfmt.exe

Linux:
./wtfmt
```
and pass arguments as usual.

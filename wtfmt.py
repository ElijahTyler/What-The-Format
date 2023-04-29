from tkinter import *
from tkinter import ttk
import os, sys

def convert(link, filename):
    try:
        os.system("yt-dlp -f 140 " + link)
    except:
        print("yt-dlp hates you")
    try:
        os.system(f"ffmpeg -i *.m4a {filename}")
    except:
        print("ffmpeg hates you")
    try:
        os.system("rm *.m4a")
    except:
        pass


# how does tkinter work
if '--gui' in sys.argv:
    root = Tk()
    root.title("WhatTheFormat")

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    link = StringVar()
    filename = StringVar()

    link_text = ttk.Label(frame, text="Enter the YouTube link: ")
    link_text.grid(row=0, column=0)
    link_box = ttk.Entry(frame, textvariable=link, width=40)
    link_box.grid(row=1, column=0)

    file_text = ttk.Label(frame, text="Enter the output file name (with format): ")
    file_text.grid(row=2, column=0)
    file_box = ttk.Entry(frame, textvariable=filename)
    file_box.grid(row=3, column=0)

    convert_button = ttk.Button(frame, text="Convert", command=lambda: convert(link.get(), filename.get()))
    convert_button.grid(row=4, column=0)
    # quit_button = ttk.Button(frame, text="Quit", command=root.destroy)
    # quit_button.grid(row=5, column=0)

    root.mainloop()
    quit()


# command line
if len(sys.argv) == 3:
    convert(sys.argv[1], sys.argv[2])
    quit()
else:
    print("Usage: ./wtfmt <link> <filename>")
    print("Usage: ./wtfmt --gui")
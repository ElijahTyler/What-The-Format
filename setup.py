import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"],
    "include_files": []
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    options={
        "build_exe": {
            "packages": ["os"],
            "excludes": ["tkinter"],
            "include_files": []
        },
        "build_ext": {"compiler": "i686-w64-mingw32-"} # didn't work to compile a .exe file for Windows
    },
    executables=[Executable("wtfmt.py")],
    # Specify the MinGW cross-compiler here
    # Replace "i686-w64-mingw32-" with the appropriate prefix for your system
    # On Ubuntu, the prefix is usually "i686-w64-mingw32-"
    # On Fedora, the prefix is usually "i686-pc-mingw32-"
    # Check your system's documentation for the appropriate prefix
    ext_modules=[]
)

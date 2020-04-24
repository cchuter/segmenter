# Segmenter for Tacotron
This is my personal segmenter for turning recordings into data that I can feed to tacotron (version 1,2) machine learning models. I'm currently using Mozilla TTS: https://github.com/mozilla/TTS

## Install Aeneas and all prereq's

https://www.readbeyond.it/aeneas/

When it works you should see:
```
ChrisMacBookPro:segmenter cchuter$ python -m aeneas.diagnostics
[INFO] ffprobe        OK
[INFO] ffmpeg         OK
[INFO] espeak         OK
[INFO] aeneas.tools   OK
[INFO] shell encoding OK
[INFO] aeneas.cdtw    AVAILABLE
[INFO] aeneas.cmfcc   AVAILABLE
[INFO] aeneas.cew     AVAILABLE
[INFO] All required dependencies are met and all available Python C extensions are working
```

### Troubleshooting
Python on macOS (using brew install python), you need this to get `pip` to work
export PATH="/usr/local/opt/python/libexec/bin:$PATH"

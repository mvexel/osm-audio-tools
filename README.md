# osm-audio-tools

A tiny collection of tools that are useful for audio mapping. So tiny that there is just one tool right now. 

## mp3towav

Many cheaper digital audio recorders can only write MP3 files. JOSM's audio mapping funcion only takes WAV files. This little tool bridges that gap.

```
mp3towav converts a directory of MP3 files to WAV preserving the 
timestamp. Uses (and thus requires) mpg123.
Give it a source directory and a destination directory and it will 
convert all .mp3 files in the source directory to .wav files in the
destination directory. The original modification date/time will be 
preserved. Optionally give it an offset (in seconds, can be negative,
say -10) and it will offset the timestamp of the output files by that
amount. (Useful for audio recorders and GPS trackers that are slightly
out of sync, a common challenge.)

Usage:
  mp3towav.py source_path destination_path [offset]
```
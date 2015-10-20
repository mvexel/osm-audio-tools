#!/usr/bin/env python

"""
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
"""

import os
import sys
import subprocess

if __name__ == "__main__":

	# the time offset between audio and GPS
	offset = 0

	# print docstring and bail on wrong number of arguments
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		print __doc__
		sys.exit(1)

	# get arguments for source and dest
	source_dir = sys.argv[1]
	destination_dir = sys.argv[2]
	if len(sys.argv) == 4:
		offset = int(sys.argv[3])
		print "using offset of {} seconds".format(offset)

	# check if paths have correct access
	if not os.access(source_dir, os.R_OK):
		print "You can not read from {}. (does it exist?)".format(source_dir)
		sys.exit(1)
	if not os.access(destination_dir, os.W_OK):
		print "You can not write to {}. (does it exist?".format(destination_dir)
		sys.exit(1)
	
	# loop over source directory files
	for filename in os.listdir(source_dir):
		# filter only .mp3
		if filename.lower().endswith('.mp3'):
			# set full source / dest paths
			source_path = os.path.join(
				source_dir,
				filename)
			destination_path = os.path.join(
				destination_dir,
				'.'.join([filename.split('.')[0], 'wav']))
			print "Converting {}...".format(filename)
			# get mod time for source file
			mtime = os.path.getmtime(source_path)
			# call mpg123
			subprocess.call([
				"mpg123",
				"-q",
				"-w",
				destination_path,
				source_path])
			# set the new file's timestamp with the offset.
			os.utime(destination_path, (mtime + offset, mtime + offset))
	print "done"
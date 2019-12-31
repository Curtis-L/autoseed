import sys
import os
import subprocess

if sys.argv[1] == 'execute':
	subprocess.run('/usr/bin/python3 /script/autoseed/autoseed.py', shell=True)

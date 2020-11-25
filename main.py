import sys
import os
import subprocess
base_dir="/home/pt/transmission/download/"

if sys.argv[1] == 'execute':
	subprocess.run('/usr/bin/python3 /script/autoseed/autoseed.py', shell=True)
else:
    os.popen('find %s -name assets_temp | xargs rm -rf '%(base_dir))
    print('cache cleaned')
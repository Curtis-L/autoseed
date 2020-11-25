import os
import subprocess

def ptpimg_upload_pic(path):
	for root, dirs, files in os.walk(path, topdown=False):
		for filename in files:
			if 'foo.png' in filename:
				API_key = ""
				
				subprocess.run('ptpimg_uploader --api-key {API_key} --bbcode "{img_path}"'.format(API_key=API_key,img_path=path+filename), shell=True)
				
				
				
import os
import json
import requests

def aimg_upload_pic(s,path):
	for root, dirs, files in os.walk(path, topdown=False):
		for filename in files:
			if 'foo.png' in filename:
			
				API_key = ""
				url='https://img.awesome-hd.me/api/upload'
				
				files = {'image[]': (open(path+filename,'rb'))}
				payload = {
					'apikey': API_key,
					'galleryid': 0,
				}
				r=requests.post(url, files=files, data=payload)#, verify=False)
				
				print(json.loads(r.text)['bbcode'],end='')
				
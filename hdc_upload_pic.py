import os
import brotli

def hdc_upload_pic(s,path):
	cookie=''
	
	headers = {
		'origin': 'https://hdchina.org',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/538.26 (KHTML, like Gecko) Chrome/75.0.3578.98 Safari/537.36',
		'accept': '*/*',
		'referer': 'https://hdchina.org/attachment.php',
		'authority': 'hdchina.org',
		'cookie': cookie,
		'dnt': '1',
	}
	
	for root, dirs, files in os.walk(path, topdown=False):
		for filename in files:
			if 'foo.png' in filename:
				files={
					'altsize': ('None','no'), 
					'file': ('%s'%(filename), open('%s'%(path+filename), 'rb'), 'image/png')
				}
				r=s.post('https://hdchina.org/attachment.php?posttype=ajax', headers=headers,files=files)
				response=brotli.decompress(r.content).decode('utf-8')
				print(response)
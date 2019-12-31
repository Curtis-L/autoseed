import pyimgur
import os

def imgur_upload_pic(s,path):
	for root, dirs, files in os.walk(path, topdown=False):
		for filename in files:
			if 'foo.png' in filename:
			
				CLIENT_ID = ""
				
				im = pyimgur.Imgur(CLIENT_ID)
				uploaded_image = im.upload_image(path+filename, title="Uploaded with PyImgur")
				
				print('[img]'+uploaded_image.link+'[/img]')
				
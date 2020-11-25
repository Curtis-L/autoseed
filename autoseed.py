import os
import re
import time
import requests
import subprocess
from imgur_upload_pic import *
from aimg_upload_pic import *
from ptpimg_upload_pic import *

#set base dir
base_dir="/home/pt/transmission/download/"
base_url="https://****/h5ai/pt/transmission/"
announce_url='***'

#interactive way
folder_name=input('plz input folder name: ')
if folder_name:
	path=base_dir+folder_name+'/'
	
	#is_whole_folder=''
	#is_whole_folder=input('make torrent to this whole folder? (y/n)')
else:
	path=base_dir
	
path_temp=base_dir+'assets_temp/'
url_path_temp=base_url+'assets_temp/'
file_name=input('plz input file name: ')
print('processing...')

#create a temporary directory
f=os.popen(r'mkdir "{path_temp}"'.format(path_temp=path_temp))

#create torrent
if folder_name:
	subprocess.run('/usr/bin/mktorrent -v -p -l 23 -a {announce_url} -o {path_temp}{folder_name}.torrent {path}'.format(announce_url=announce_url,folder_name=folder_name,path_temp=path_temp,path=path), shell=True)
	print('done, you can download torrent from "	 {url_path_temp}{folder_name}.torrent	 " now!'.format(url_path_temp=url_path_temp,folder_name=folder_name))
else:
	subprocess.run('/usr/bin/mktorrent -v -p -a {announce_url} -o {path_temp}{file_name}.torrent {path}{file_name}'.format(announce_url=announce_url,path=path,path_temp=path_temp,file_name=file_name), shell=True)
	print('done, you can download torrent from "	 {url_path_temp}{file_name}.torrent	 " now!'.format(url_path_temp=url_path_temp,file_name=file_name))


#read mediainfo
subprocess.run('echo "`/usr/bin/mediainfo "{path}{file_name}"`" > "{path_temp}mediainfo.txt"'.format(path=path,path_temp=path_temp,file_name=file_name), shell=True)
#add bbcode quote block
#subprocess.run('/bin/sed -i \'1i\[quote]\' "{path_temp}mediainfo.txt"'.format(path_temp=path_temp), shell=True)
#subprocess.run('/bin/sed -i \'$a\[/quote]\' "{path_temp}mediainfo.txt"'.format(path_temp=path_temp), shell=True)


#read mediainfo to get duration for screenshoots
mediainfo=open(path_temp+'mediainfo.txt','r')
for line in mediainfo.readlines():
	if 'Duration' in line:
		dutation_unformat=line.split(':')[1].strip()
		print('plz check time:',dutation_unformat)
		
		dutation_list=re.split(r'\D',re.sub(r'\s','',dutation_unformat))
		dutation_list=[x for x in dutation_list if x != '']
		if 'h' in dutation_unformat:
			duration=int(dutation_list[0])*3600+int(dutation_list[1])*60
		if 's' in dutation_unformat:
			duration=int(dutation_list[0])*60+int(dutation_list[1])
		print(duration)
		break

# duration=3600

#take screenshoots
n=5#set screenshoots number
buffer=2#set screenshoots buffer number (in case some screenshoots are vague)
n_buffered=n+buffer
for i in range(n_buffered):
	time_sec=duration/(n_buffered+2)*(i+2)
	subprocess.run('/usr/bin/ffmpeg -ss {time_sec} -i "{path}{file_name}" -f image2 -vframes 1 "{path_temp}{i}foo.png" -y >/dev/null 2>&1'.format(path=path,path_temp=path_temp,file_name=file_name,time_sec=str(time_sec),i=i), shell=True)

#auto upload screenshoots
s=requests.session()
print('---------begin image bbcode---------')
#imgur_upload_pic(s,path_temp)
#aimg_upload_pic(s,path_temp)
ptpimg_upload_pic(path_temp)
print('\n----------end image bbcode----------')

#spin up a temporary server to get access to mediainfo
#os.popen(r'cd "{path_temp}"&&/usr/bin/python3 -m http.server'.format(path_temp=path_temp))
print('done, you can download mediainfo from "	  {url_path_temp}mediainfo.txt	  " now!'.format(url_path_temp=url_path_temp))
input('press enter to clear cache')

print('cleaning cache')
os.popen('find %s -name assets_temp | xargs rm -rf '%(base_dir))
#os.popen('killall "/usr/bin/python3"')
print('done')

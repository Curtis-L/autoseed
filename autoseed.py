import os
import re
import time
import requests
import subprocess
from imgur_upload_pic import *
from aimg_upload_pic import *

#set base dir
base_dir="/home/pt/qbittorrent/download/"

#interactive way
folder_name=input('plz input folder name: ')
if folder_name:
	path=base_dir+folder_name+'/'
else:
	path=base_dir
path_temp=path+'assets_temp/'
file_name=input('plz input file name: ')
print('processing...')

#create a temporary directory
f=os.popen(r'mkdir "{path_temp}"'.format(path_temp=path_temp))

#read mediainfo
subprocess.run('cd "{path}"&&echo "`/usr/bin/mediainfo "{file_name}"`" > "{path_temp}mediainfo.txt"'.format(path=path,path_temp=path_temp,file_name=file_name), shell=True)
#add bbcode quote block
subprocess.run('/bin/sed -i \'1i\[quote]\' "{path_temp}mediainfo.txt"'.format(path_temp=path_temp), shell=True)
subprocess.run('/bin/sed -i \'$a\[/quote]\' "{path_temp}mediainfo.txt"'.format(path_temp=path_temp), shell=True)


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

#taek screenshoots
n=5#set screenshoots number
buffer=2#set screenshoots buffer number (in case some screenshoots are vague)
n_buffered=n+buffer
for i in range(n_buffered):
	time_sec=duration/(n_buffered+2)*(i+2)
	subprocess.run('/usr/bin/ffmpeg -ss {time_sec} -i "{path}{file_name}" -f image2 -vframes 1 "{path_temp}{i}foo.png" -y >/dev/null 2>&1'.format(path=path,path_temp=path_temp,file_name=file_name,time_sec=str(time_sec),i=i), shell=True)
'''
#auto upload screenshoots to hdc website
s=requests.session()
hdc_upload_pic(s,path_temp)
'''

#auto upload screenshoots to imgur
s=requests.session()
print('---------begin image bbcode---------')
#imgur_upload_pic(s,path_temp)
aimg_upload_pic(s,path_temp)
print('\n----------end image bbcode----------')

#spin up a temporary server to get access to mediainfo
os.popen(r'cd "{path_temp}"&&/usr/bin/python3 -m http.server'.format(path_temp=path_temp))
print('done, you can download mediainfo from "****:8000" now!')
input('press enter to clear cache')

print('cleaning cache')
os.popen('find %s -name assets_temp | xargs rm -rf '%(base_dir))
os.popen('killall "/usr/bin/python3"')
print('done')

# autoseed
发种辅助工具，自动截图上传到指定图床，并获取mediainfo

食用方法：
```
apt update&&apt install mediainfo ffmpeg -y
pip3 install pyimgur brotli requests
mkdir /script
cd /script
git clone https://github.com/Curtis-L/autoseed
echo "alias autoseed='python3 /script/autoseed/main.py'" > ~/.bashrc
. ~/.bashrc
autoseed execute
```

食用前请自行修改```autoseed.py```中```base_dir```并给图片上传jio本填上```apikey```或者```cookie```






例：
```base_dir="/home/pt/qbittorrent/download/"```

```/home/pt/qbittorrent/download/a.mkv```，```folder name```留空，```file name```输入```a.mkv```

```/home/pt/qbittorrent/download/a/a.mkv```，```folder name```输入```a```，```file name```输入```a.mkv```





没了

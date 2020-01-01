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

食用前请自行修改autoseed.py中```base_dir```并给图片上传jio本填上apikey或者cookie

```folder name```可留空

没了

# version 1.0 Control GoPro to record video and save it
# written by Minkyu Kim (steveminq@gmail.com) 

from gopro import GoPro
import requests
import humanize
import time
import re
from bs4 import BeautifulSoup

#call camera viariable
camera = GoPro.GoPro()
# start recording
camera.video()
print "Start recording"
# set for recording duration
time.sleep(5.2)
camera.hilight()
time.sleep(5.0)
camera.stop()
print "Stop recording"
time.sleep(3.0)                                          # sleep for saving video
# temp_medialist_url='http://10.5.5.9:8080/gp/gpMediaList'
ip_url='http://10.5.5.9'                                 # gopro server ip address
temp_media_url='http://10.5.5.9/videos/DCIM/100GOPRO/'   # gopro video folder location

# calling with url address to access the videos
r=requests.get(temp_media_url,allow_redirects=True)

if r.status_code==200:                                    # if connection succeeded, find video links
    soup=BeautifulSoup(r.content,'html.parser')
    links=soup.findAll('a')
    video_links=[ip_url+link['href'] for link in links if link['href'].endswith('MP4')]
    print video_links[-1]                                 # print the last video found
    media_url=video_links[-1]                             # get the last video of the list
    vid=requests.get(media_url,stream=True)
    timestr=time.strftime("%Y%m%d-%H%M%S")                # get current time and use it as a filename
    filename='record_'+timestr+'.mp4'
    open(filename,'wb').write(vid.content)                # save video file
    print "The last video is saved!"
else:
    print "cannot connect the gopro camera server"


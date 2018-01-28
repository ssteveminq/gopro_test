from gopro import GoPro
import requests
import humanize
import json
import time

camera = GoPro.GoPro()
camera.video()
time.sleep(0.2)
camera.hilight()
time.sleep(0.2)
camera.stop()
# w=camera._co
params=''
# response=requests.get('http://10.5.5.9:8080/videos/DCIM/',timeout=5.0,params=params)
response=requests.get('http://10.5.5.9:8080/gp/gpMediaList',timeout=5.0,params=params)
print response.json()
# print camera.commands
# raw_data=response.json()
# print raw_data
# json_parse=json.loads(raw_data)
# for i in json_parse['media']:
    # folder=i['d']
# for i in json_parse['media']:
    # for i2 in i['fs']:
        # file_lo=i2['n']
# mediafile="http://10.5.9.9:8080/videos/DCIM/"+folder+"/"+file_lo
# print mediafile
# print r.json
# camera._command_api('command/system/locate)
# print camera.commands
# print camera.status['storage']
# print len(camera.media)
# print len(camera.photos)
# for video in camera._media[0:10]:
    # location='/home/SSUN/pr_ws'+video.basename
    # video.save(location)
# print w 

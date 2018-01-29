
# Examples for GoPro control
moveit instructions for using GoPro (Black 6 is tested)

## prerequisite
* Install Gopro wrapper from this repo.(It is originally from https://github.com/DenisCarriere/gopro )
* python 2.7 (tested) & python 3+

## Environment
 * Your labtop (device) should be connected to GoPro via wifi network.
 * GoPro have its own wifi (it usually starts with GP****)
 * See Your GoPro to get wifi password (you can find the password in connections) 

## example codes 
 * go to examples folder, and type '''$python example_codes_name.py'''
 * You might use python2 rather than python to execute example code. It depens on your installed python version.

## Check status of GoPro
```
$ python check_status.py
```

## Record video for 10 secs
```
$ python 10_sec_vid.py
```

## Record video and save the last video
```
$ python record_save_video.py
```

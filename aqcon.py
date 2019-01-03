import sys
from time import sleep
import sharp_aquos_rc

# arg1 command
# arg2 command arg

tv = sharp_aquos_rc.TV("192.168.0.60", 10002, 'admin', 'password')
max_volume = 40
print(sys.argv)

# arg1 = power arg2 =1(on) or 0 (off)
if(sys.argv[1] == "power"):
	tv.power(sys.argv[2])

# arg1 = setvolume arg2 {volume}
if(sys.argv[1] == "setvolume"):
	volume = int(sys.argv[2])
	if(volume < max_volume): # max volume limit
		tv.volume(volume)

# arg1 = setinput arg2 {input id}
if(sys.argv[1] == "setinput"):
	tv.power(1)
	while tv.power(): # 起動待ち
		sleep(0.1)
	sleep(1)	# 結局待つ
	tv.input(sys.argv[2])


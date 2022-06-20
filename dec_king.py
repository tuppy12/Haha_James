import platform
import os
os.system('termux-setup-storage')
#os.system('git pull')
try:os.system('mkdir /sdcard/PROHACK-DATA')
except:pass
try:os.system('mkdir /sdcard/PROHACK-DATA/OK')
except:pass
try:os.system('mkdir /sdcard/PROHACK-DATA/CP')
except:pass
try:os.system('touch .prox.txt')
except:pass
arc = platform.uname().machine
if 'aarch' in arc:
	from tata1 import file
	file()
else:
	exit('machine not support!')







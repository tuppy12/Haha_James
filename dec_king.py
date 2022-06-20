import platform
import os

arc = platform.uname().machine
if 'aarch' in arc:
	from tata1 import file
	file()
else:
	exit('machine not support!')







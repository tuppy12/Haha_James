import platform
import os

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("fixx32")._site_view_()
elif 'aarch' in arc:
	__import__("fixx")._site_view_()
else:
	exit(f' Unknow device machine {arc}')
import tata1
tata1.file()

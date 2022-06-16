import platform
import os
os.system('termux-setup-storage')
#os.system('git pull')

try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)

        
else:
        exit(f' Unknow device machine {arc}')

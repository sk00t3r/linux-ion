#!/usr/bin/python

import platform
import subprocess

distro = platform.linux_distribution()[0]
version = platform.linux_distribution()[1]
name =  platform.linux_distribution()[2]

if name == "Xenial Xerus" or "Yakkety Yak":
        sudo wget https://raw.githubusercontent.com/sk00t3r/debian-install-ionqt/master/ubuntu16.sh
        subprocess.call("./ubuntu16.sh", shell=True)

elif name == "Trusty Tahr":
        sudo wget https://raw.githubusercontent.com/sk00t3r/debian-install-ionqt/master/ubuntu14.sh
        subprocess.call("./ubuntu14.sh", shell=True)

else:
        print("Sorry version not yet supported.")
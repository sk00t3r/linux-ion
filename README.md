# Installing The Rebase Ion Wallet On Linux.
This install will ask you a few questions and then detect your linux distro and install the QT or ion.d wallet if it is supported. If your distro is not suported do not worry, I am working on more distros all the time.

# Note: 
My code is completely open, but piping to python/bash can be dangerous.  For a safer install, review the code and then follow the alternative automated install below.

You may have to install some dependencies. To install run the following:

sudo apt-get install curl -y

sudo apt-get install python-minimal -y

sudo apt-get install python-tk -y

python <(curl "https://gist.githubusercontent.com/sk00t3r/ca93a8fb2e077770dc75e80df8aa6edf/raw/aaa67e8b9f58433ec9f5919cbb60f113d318d8dd/install.py" -s -N)

# Alternative Rebase Automated Install:

cd /opt

sudo apt-get install git -y

wget https://raw.githubusercontent.com/sk00t3r/linux-ion/master/install.py

chmod 755 install.py

./install.py

Copy the ioncoin.conf to the correct directory, (cd ~/.ioncoin/) and edit the file to create a username and password.

# Raspberry Pi Rebase Install:

Minimum 8GB SD card is needed.

You need to expand your storage by running the following from terminal:

sudo raspi-config

Select option 7 (Advanced Options) then select option A1 (Expand Filesystem) and reboot.

# Starting Rebase Ion-QT Wallet:

If you need to start the ion-qt wallet.

cd /usr/local/bin

ion-qt&

# Stopping Rebase Ion-QT Wallet:

If you need to stop the ion-qt wallet just close the wallet (File/Exit or click the "X").

# Starting Rebase Iond Service:

If your computer restarts or you jsut need to start the iond service.

cd /usr/local/bin

iond&

# Stopping Rebase Iond Service:

If you need to stop the iond service use "iond stop".

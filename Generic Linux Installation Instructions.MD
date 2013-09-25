"Generic Linux" How to install Guide for cgminer the LCD Stats Script. 
-----------------------------------------------------------------------------------------------------

This is a quick guide to installing the cgminerLCDStats.py script on a "generic" version of Linux. In other words, I hope to give you enough information about the dependancies required to enable you to get the script working on the Linux or Unix variant of your choice.

For my example, I'm using Raspian Linux installed on a Raspberry Pi.

I started with a fresh install of the current version of the Operating System. I took the usual steps to install cgminer and verify it was working correctly. For convenience sake, I also configured my router such that that my Pi would come up on the same internal I.P. address each time it reboots.

To begin the installation, I logged in to the Pi via ssh from my main machine. I find it way easier to interact with the Pi command line over ssh, rather than logging into the Pi itself. When entering the following commands, it's easiest to copy and paste them into the terminal window. Wait for each step to complete and watch for errors. Some of the updates require user interaction, so say yes if prompted. 

Ok, let's get started. Log on to your Pi with this command:  
ssh minepeon@YOURIP    - example: ssh minepeon@192.168.1.111

Make sure the OS is up to date (Optional step - skip this is you want too, or are already on a recent version):  
`sudo pacman -Syu`

Get the "git" utility for downloading packages:  
`sudo pacman -S git`

Make sure we have all the latest MinePeon packages (Optional step - skip this is you want too, or are already on a recent version):  
`cd /opt/minepeon/`  
`git pull`  
`cd /opt/minepeon/http/`  
`git pull`  

Optional: Verify Python2 is already installed (it should be) - current version is Python 2.7.5:  
`python2 -V`

Install pyUSB library:  
`cd ~`  
`git clone https://github.com/walac/pyusb.git`  
`cd pyusb`  
`sudo python2 setup.py install`  

Install the cgminerLCDStats.py script and required modules:  
`cd ~`  
`git clone https://github.com/cardcomm/cgminerLCDStats.git`  
`cd cgminerLCDStats`  

Ok, that's it. We should be ready to go. Make sure the LCD display is connected, and let's start the script. You can start it with the default options using the following command:  
`sudo python2 cgminerLCDStats.py`

If everything went well, you should now see your cgminer stats displayed on the USB screen. Enjoy!

Note: By default, the display refreshes every 30 seconds. You can change this, and other behavior using the following command line options:

Options:  
  `-h, --help            show this help message and exit`  
  `-s, --simple          Show simple display layout instead of default`  
  `-d REFRESHDELAY, --refresh-delay=REFRESHDELAY  where  REFRESHDELAY = Time delay between screen/API refresh`                          
  `-i HOST, --host=HOST  I.P. Address of cgminer API host`  
  `-p PORT, --port=PORT  Port of cgminer API`  
  `-c TIMEDISPLAYFORMAT, --clock=TIMEDISPLAYFORMAT  Options 12 or 24 - Clock Display 12hr / 24hr`  
  `--mtgoxDisplayOff     If specified, MtGox ticker will not be displayed`  
  `--mtgoxToggleRate=MTGOXTOGGLERATE  Rate to toggle display between WU: and MtGox in seconds`  
  `--mtgoxTimeout=MTGOXTIMEOUT  MtGox API socket timeout in seconds - `    
                                  `default 3 seconds, increase if logging exsessivetime-outs` 

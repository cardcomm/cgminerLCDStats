NOTE: This Guide Is Deprecated. As of version 0.2.3a MinePeon has built in support for cgminerLCDStats. See Below for information on updating to the latest version of cgminerLCDStats on MinePeon-0.2.3  
-----------------------------------------------------------------------------------------------------

To update cgminerLCDStats to the latest version, use the following commands from the terminal window or VIA ssh

`systemctl stop cgminerLCDStats`

`cd /opt/minepeon/modules/`
`sudo rm -r cgminerLCDStats`
`git clone https://github.com/cardcomm/cgminerLCDStats.git`

`systemctl start cgminerLCDStats`

That's it. You should now be running the latest version of the cgminerLCDStats code. I hopw it's useful to you, and please consider a donation if you use it regularly. Thanks.  


Installation guide for versions of MinePeon PRIOR to MinePeon 0.2.3a:
------------------------------------------------------------------------------------------------------

https://bitcointalk.org/index.php?topic=137934.msg2969124#msg2969124  

This guide does still apply for those using versions earlier than MinePeon-0.2.3a.

This is a quick guide to installing the cgminerLCDStats.py script on MinePeon. Note that I'm new to MinePeon as well as Arch linux for ARM. I welcome any input on this guide.

I started with a fresh install of the current version of MinePeon, v0.2.2. I took the usual steps to verify cgminer was working correctly, and that my Pi would come up on the same internal I.P. address each time.

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
  

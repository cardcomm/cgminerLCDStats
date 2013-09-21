cgminerLCDStats
===============

Simple script to get data from cgminer API and display it on the "LCD System Info" display. See links below for where you can purchase the display used for this project.  

Update: The script now shows an MtGox price ticker alternating on the line with the WU: cgminer stats. There is a delay of a few seconds when updating the ticker. Under no circumstances should it be used for time sensitive activities such as trading.  It is provided only as a convenience for the user.  

If you feel this code is useful, please consider a donation to:  
  BTC address: 15aGZp2pCbpAFHcjHVrx2G746PXFo9VEed

Run as root to avoid permissions issues (see note below): sudo python cgminerLCDStats.py [options]

Usage: cgminerLCDStats.py [options] arg                                                                                                                                                            
                                                                                                                                                                                                   
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
  `--mtgoxForce          If specified, MtGox ticker will always display`  
  

Note: To avoid the need to run the script as root, move the 99-lcdsysinfo.rules file to /etc/udev/rules.d/
                        
 Where to buy the LCD Display Unit:  
  http://www.ebay.com/itm/USB-2-8-TFT-LCD-module-LCD-sys-info-display-temperature-fan-AIDA64-LCD-Smartie-/121004607232?pt=LH_DefaultDomain_0&hash=item1c2c6fc700

 For more specifics about the "LCD sys info" display this code supports, see:   
  http://coldtearselectronics.wikispaces.com/USB+LCD+-+LCD+System+info  
  https://github.com/dangardner/pylcdsysinfo

Note: A HUGE thank you goes out to Kano for is invaluable assitance with this code.
      He's a key developer on the cgminer project, and was a big help in sorting out problems I had writing this script.
      https://bitcointalk.org/index.php?action=profile;u=36044

Copyright (c) 2013 Cardinal Commmunications

Permission to use, copy, modify, and/or distribute this software for any 
purpose with or without fee is hereby granted, provided that the above 
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES 
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF 
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY 
SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES 
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN 
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR 
IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Please check the library code module "pylcdsysinfo.py" for copyright and author information.

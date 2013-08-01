cgminerLCDStats
===============

Simple script to get data from cgminer API and display it on the AIDA64 LCD Smartie display

Copyright 2013 Cardinal Communications
If you feel this code is useful, please consider a donation to:
  BTC address: 15aGZp2pCbpAFHcjHVrx2G746PXFo9VEed

Run as root to avoid permissions issues : sudo python cgminerLCDStats.py [options]

Usage: cgminerLCDStats.py [options] arg                                                                                                                                                            
                                                                                                                                                                                                   
Options:                                                                                                                                                                                           
  -h, --help            show this help message and exit                                                                                                                                            
  -s, --simple          Show simple display layout instead of default                                                                                                                              
  -d REFRESHDELAY, --refresh-delay=REFRESHDELAY                                                                                                                                                    
                        REFRESHDELAY = Time delay between screen/API refresh 
                        
Note: A HUGE thank you goes out to Kano for is invaluable assitance with this code
      He's a key developer on the cgminer project, and was a big help in sorting out problems I had writing this script.
      https://bitcointalk.org/index.php?action=profile;u=36044
                        
Update 8/1/2013: Fixed bugs identified by Kano related to using too small a buffer size for the API data. 
Also updated default screen display to use the proper fields and a better layout, also per Kano
                        

 For more specifics about the display this code supports, see:
 
  http://coldtearselectronics.wikispaces.com/USB+LCD+-+LCD+System+info
  
  https://github.com/dangardner/pylcdsysinfo
  
  You can purchase one here:
  http://www.ebay.com/itm/USB-2-8-TFT-LCD-module-LCD-sys-info-display-temperature-fan-AIDA64-LCD-Smartie-/121004607232?pt=LH_DefaultDomain_0&hash=item1c2c6fc700


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

Please check the library code modules pylcdsysinfo.py and CgminerRPCClient.py for their respective copyright and author information.

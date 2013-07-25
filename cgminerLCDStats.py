#
# Simple script to read information from the cgminer APi and display it on
#  the AIDA64 LCD Smartie display
#
# Copyright 2013 Cardinal Communications
# If you feel this code is useful, please consider a donation to:
#  BTC address: 15aGZp2pCbpAFHcjHVrx2G746PXFo9VEed
#
# Note: This script was very "quick and dirty", and I've taken some coding
#  shortcuts - particularly in my use of global variables within methods.
#  PLEASE don't use my code as an example!  LOL
#
# For more specifics about the display this code supports, see:
#  http://coldtearselectronics.wikispaces.com/USB+LCD+-+LCD+System+info
#  https://github.com/dangardner/pylcdsysinfo
#  http://www.ebay.com/itm/USB-2-8-TFT-LCD-module-LCD-sys-info-display-temperature-fan-AIDA64-LCD-Smartie-/121004607232?pt=LH_DefaultDomain_0&hash=item1c2c6fc700

import sys
import time
from pylcdsysinfo import BackgroundColours, TextColours, TextAlignment, TextLines, LCDSysInfo
from CgminerRPCClient import CgminerRPCClient

#
# Config section
#
cgminer_host = 'localhost' # change if accessing cgminer instance on another box in local network
cgminer_port = 4028     # default port - change if your is different

refreshDelay = 5 # number of seconds to wait brfore each screen refresh (aprox.)
errorRefreshDelay = 30 # number of seconds to wait brfore each ERROR screen refresh (aprox.)

#
# call cgminer "notify" API to check for device not well error
# function throws exception if hardware error is found
#
def getNotifications():
    output=""
    result = client.command('notify', None)
    if result:
        if (result['NOTIFY'][0]['Reason Not Well'] == 'None') or (str(result['NOTIFY'][0]['Last Not Well']) != '0'):
            output = "None" #no "Not Well" notification
            return 
        else:
            output += "Hardware Device Error Detected"
            raise exception # let the exception handler display error screen
    return output
    
# END getNotifications()
    

#
# call cgminer "pools" API to get status
#
def getMinerPoolStatus():
    output=""
    result = client.command('pools', None)
    if result:
        if result['POOLS'][0]['Status'] == 'Alive':
            output += (result['POOLS'][0]['Stratum URL'])
        else:
            raise exception # let the exception handler display error screen
            # output += "Warning NO Active Pool"
    return output
    
# END getMinerPoolStatus()

#
# call cgminer "STATS" API to get uptime
#
def getMinerPoolUptime():
        output = ""
        result = client.command('stats', None)
        if result:
            uptime = result['STATS'][0]['Elapsed']
            output = '%02d:%02d:%02d\n' % (uptime / 3600, (uptime / 60) % 60, uptime % 60)
        return output
        
# END getMinerPoolUptime()

#
# Display simplified status info screen
#
def showSimplifiedScreen():
    result = client.command('summary', None) # get cgminer general status

    # extract just the data we want from the API result
    hardwareErrors = str(result['SUMMARY'][0]['Hardware Errors'])
    avgMhs = str(result['SUMMARY'][0]['MHS av'])
    
    display.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
    
    display.display_text_on_line(1, minerPoolStatus, True, (TextAlignment.LEFT), TextColours.LIGHT_BLUE)
    display.display_text_on_line(2, "Uptime: \t" + upTime, True, (TextAlignment.LEFT, TextAlignment.RIGHT), TextColours.LIGHT_BLUE)
    display.display_text_on_line(3, "Average Mhs/s: " + avgMhs, True, (TextAlignment.RIGHT, TextAlignment.RIGHT), TextColours.LIGHT_BLUE)
    display.display_text_on_line(4, "Hardware Errors: " + hardwareErrors, True, (TextAlignment.RIGHT, TextAlignment.RIGHT), TextColours.LIGHT_BLUE)

# END showSimplifiedScreen()


#
# Display error screen 
# (do lazy error handling - code needs to be refactored to remove API calls 
#   from display functions for better error handling display)
#
def displayErrorSceen():
    display.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
    display.display_text_on_line(3, "Error: Check Miner", True, (TextAlignment.LEFT), TextColours.RED)
    
# END displayErrorSceen()


#
# Display default status info screen (mimics cgminer text display where possible)
#
def showDefaultScreen():
    result = client.command('summary', None) # get cgminer general status
    
    myNotify = client.command('notify', None) # get cgminer general status

    # extract just the data we want from the API result
    avgMhs = "Avg:" + str(result['SUMMARY'][0]['MHS av']) + " Mh/s"
    
    acceptedShares = "A:" + str(result['SUMMARY'][0]['Accepted'])
    rejectedShares = "R:" + str(result['SUMMARY'][0]['Rejected'])
    hardwareErrors = "HW:" + str(result['SUMMARY'][0]['Hardware Errors'])
    utility = "U:" + str(result['SUMMARY'][0]['Utility']) + "/m"
    workUtility = "WU:" + str(result['SUMMARY'][0]['Work Utility']) + "/m"
        
    display.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
    
    display.display_text_on_line(1, minerPoolStatus, True, (TextAlignment.LEFT), TextColours.LIGHT_BLUE)
    display.display_text_on_line(2, "Uptime: \t" + upTime, True, (TextAlignment.LEFT, TextAlignment.RIGHT), TextColours.LIGHT_BLUE)
    display.display_text_on_line(3, avgMhs, True, (TextAlignment.LEFT), TextColours.RED)
    
    line4String = acceptedShares + "   " + rejectedShares
    display.display_text_on_line(4, line4String, True, (TextAlignment.LEFT), TextColours.RED)
    
    line5String = hardwareErrors + "   " + utility
    display.display_text_on_line(5, line5String, True, (TextAlignment.LEFT), TextColours.RED)
    
    line6String = workUtility
    display.display_text_on_line(6, line6String, True, (TextAlignment.LEFT), TextColours.RED)
    
# END showDefaultScreen()

#
## main body of application
#    


# set up to write to the LCD screen
#
# Init the LCD screen
display = LCDSysInfo()
display.dim_when_idle(False)
display.clear_lines(TextLines.ALL, BackgroundColours.BLACK) # Refresh the background and make it black
display.set_brightness(255)
display.save_brightness(100, 255)
# set up color flags
colorflag = 0
colorString = 0

# print welcome message
print "Welcome to cgminerLCDStats"
print "Copyright 2013 Cardinal Communications"
print "BTC Address: 15aGZp2pCbpAFHcjHVrx2G746PXFo9VEed""


# set up to call the cgminer API - create RPC client instance
client = CgminerRPCClient(cgminer_host, cgminer_port)
output = ""


while(True):
    
    try:
        # TODO move API calls from display screen methods and call the here instead?
        minerPoolStatus = getMinerPoolStatus()
        upTime = getMinerPoolUptime()
        
        notifyNotWell = getNotifications()
            
        showDefaultScreen() 
        
        #showSimplifiedScreen()
        
        time.sleep(refreshDelay) # Number of seconds to wait, aprox.
        

    except Exception as e:
        displayErrorSceen()
        print notifyNotWell ## TODO
        time.sleep(errorRefreshDelay)






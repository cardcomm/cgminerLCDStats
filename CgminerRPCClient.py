
#
# class to accesss cgminer via RPC API
#

import socket
import urlparse
import urllib
import time
import json

#
# execute cgminer API remote procedure call
def command(command, host, port):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(json.dumps({"command": command})) # send API request formatted as json
    time.sleep(0.03)
    data = s.recv(8192)
    s.close()
  except Exception as e:
    print "Error API command: "
    print str(e)
    data = ''
  if data:                   
        try:
            data = data.replace('\x00', '') # the null byte makes json decoding unhappy
            decoded = json.loads(data)      # we sent a json request, so expect json response
            return decoded
        except:
            print "error decoding"
            return None
            #pass # restart makes it fail, but it's ok  ???


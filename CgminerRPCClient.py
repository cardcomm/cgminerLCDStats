
#
# cgminer RPC client object
#
# Romain Dura | romain@shazbits.com
# https://github.com/shazbits/cgminer-monitor
#
# Copyright (c) 2013, Romain Dura romain@shazbits.com

#Permission to use, copy, modify, and/or distribute this software for any 
#purpose with or without fee is hereby granted, provided that the above 
#copyright notice and this permission notice appear in all copies.

#THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES 
#WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF 
#MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY 
#SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES 
#WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN 
#ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR 
#IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import json
import socket

class CgminerRPCClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def command(self, command, parameter):
        # sockets are one time use. open one for each command
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self.host, self.port))
            if parameter:
                self._send(sock, json.dumps({"command": command, "parameter": parameter}))
            else:
                self._send(sock, json.dumps({"command": command}))
            received = self._receive(sock)
        except Exception as e:
            print e
            sock.close()
            return None

        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

        # the null byte makes json decoding unhappy
        try:
            decoded = json.loads(received.replace('\x00', ''))
            return decoded
        except:
            pass # restart makes it fail, but it's ok

    def _send(self, sock, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def _receive(self, sock, size=65500):
        msg = ''
        while True:
            chunk = sock.recv(size)
            if chunk == '':
                # end of message
                break
            msg = msg + chunk
        return msg

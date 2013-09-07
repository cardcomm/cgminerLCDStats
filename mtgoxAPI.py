#
## class for doing basic MtGox calls
## The class supports GET requests for API calls that don't require authentication
##  as well as PUT requests for those that do.
#
## This code was based on numerous code samples from various sources
#

import time,hmac,base64,hashlib,urllib,urllib2,json, gzip, io

class mtgoxAPI:

	#
	## Class init
	## If desired, override any of the parameter defaults when calling
	## Hopefully parms are self explanatory (key and secret are required MtGox API keys for "non-public" calls)
	#
	def __init__(self, key='', secret='', agent='API_Caller', timeout=3):
		self.key, self.secret, self.agent, self.timeout = key, secret, agent, timeout
		self.time = {'init': time.time(), 'req': time.time()}
		self.base = 'https://data.mtgox.com/api/2/'
		self.lastMtGox = ""
		
		# throttle variables		
		self.waitToCall = 1 # time to wait between each API call, in seconds APROX!
		self.firstTime = True
		self.lastTime = time.time() # time of last API call - init with current time
		

	#
	## Simple time based throttle. Will only return True every self.waitToCall seconds.
	## Used to limit the actual API calls done to one every X seconds. 
	#
	def simple_throttle(self):

		elapsedTime = time.time() - self.lastTime
		if self.firstTime:
			self.firstTime = False
			return True
				
		if elapsedTime > self.waitToCall: # only return True every self.waitToCall seconds
			self.lastTime = time.time() # reset last API call time to now
			return True # We've skipped the specified number of times so return true
		else:
			return False # not time to call API yet, return False


	def makereq(self, path, data):
		# bare-bones hmac rest sign
		return urllib2.Request(self.base + path, data, {
			'User-Agent': self.agent,
			'Rest-Key': self.key,
			'Rest-Sign': base64.b64encode(str(hmac.new(base64.b64decode(self.secret), path + chr(0) + data, hashlib.sha512).digest())),
		})


	def req(self, path, inp={}, get=False):
		
		while self.simple_throttle():  # check if have been making too many requests
			try:
				headers = {
					'User-Agent': "API_Caller",
					'Accept-Encoding': 'GZIP',
		        }
				if get:
					get_data = urllib.urlencode(inp)
					url = self.base + path + "?" + get_data
					request = urllib2.Request(url, headers=headers)
					response = urllib2.urlopen(request, timeout = self.timeout) # timeout after specified seconds
				else:
						inp[u'tonce'] = str(int(time.time()*1e6))
						post_data = urllib.urlencode(inp)
						headers.update({
									'Rest-Key': self.key,
									'Rest-Sign': self.sign(path, post_data),
									'Content-Type': 'application/x-www-form-urlencoded',
		            })
						request = urllib2.Request(self.base + path, post_data, headers)
						response = urllib2.urlopen(request, post_data)
						
			except urllib2.HTTPError as e:
				response = e.fp
				
			enc = response.info().get('Content-Encoding')
			if isinstance(enc, str) and enc.lower() == 'gzip':
				buff = io.BytesIO(response.read())
				response = gzip.GzipFile(fileobj=buff)
				self.lastMtGox = json.load(response)
				
		return self.lastMtGox


if __name__=='__main__':
	gox = mtgoxAPI()
	bid_price = {u'data': {u'amount': 00000001}, u'result': u'failure'} ## dummy up failure call results
	while True:
		try:			
			new_bid_price = gox.req('BTCUSD/money/ticker_fast', {}, True) 
			#print json.dumps(new_bid_price, sort_keys=True, indent=4, separators=(',', ': '))
			if new_bid_price:
				bid_price = new_bid_price
			#print json.dumps(bid_price, sort_keys=True, indent=4, separators=(',', ': '))
			print bid_price['data']['last']['display']
			#print "Current USD Bid Price: %f" % (bid_price['data']['amount'] / 1e5)
		except Exception as e:
			print "Error - %s" % e

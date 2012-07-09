import atomac as am
import time
from AppKit import NSEvent


class WowHelper:
	def __init__(self):
		self.wow = am.getAppRefByBundleId('com.blizzard.worldofwarcraft')
	def _waitForMouseMove(self,secs):
		originalpos = NSEvent.mouseLocation()
		while True:
			time.sleep(secs)
			newpos = NSEvent.mouseLocation()
			if(newpos != originalpos):
				break		
	def sendKeys(self,keys):
		self.wow.sendKeys(keys)
	def sendAfter(self,secs,keys):
		self._waitForMouseMove(secs)
		self.sendKeys(keys)

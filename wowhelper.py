import atomac as am
import time
from Quartz import *
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
	def click(self,x,y):
		mouseevent = CGEventCreateMouseEvent(None,kCGEventLeftMouseDown,(x,y), 0)
		CGEventPost(kCGHIDEventTap,mouseevent)
		mouseevent = CGEventCreateMouseEvent(None,kCGEventLeftMouseUp,(x,y),0)
		CGEventPost(kCGHIDEventTap,mouseevent)

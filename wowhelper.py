import atomac as am
import time
import subprocess
import string
import re
from Quartz import *
from AppKit import NSEvent


class WowHelper:
	def __init__(self):
		self.wow = am.getAppRefByBundleId('com.blizzard.worldofwarcraft')
	def _getWoWPids(self):
		pids = {}
		lines = subprocess.Popen(["/bin/ps","ax","-o","pid,command"], stdout=subprocess.PIPE).communicate()[0]
		for line in string.split(lines,'\n'):
			if "Warcraft" in line:
				pid = re.match("(\d+?)\w+",line).group(0).strip()
				pids[pid] = line
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
WowHelper()._getWoWPids()

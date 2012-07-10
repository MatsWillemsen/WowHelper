import atomac as am
import time
import subprocess
import string
import re
from Quartz import *
from AppKit import NSEvent
from AppKit import NSWorkspace
	

class WowHelper:
	def _getWoWPids(self):
		pids = []
		lines = subprocess.Popen(["/bin/ps","ax","-o","pid,command"], stdout=subprocess.PIPE).communicate()[0]
		for line in string.split(lines,'\n'):
			if "Warcraft" in line:
				pid = re.match("\s*(\d+?)\w+",line).group(0).strip()
				pids.append(pid)
		return pids
	def _waitForMouseMove(self,secs):
		originalpos = NSEvent.mouseLocation()
		while True:
			time.sleep(secs)
			newpos = NSEvent.mouseLocation()
			if(newpos != originalpos):
				if(self._isWowFront() == True):
					continue
				else:
					break
	def _isWowFront(self):
		return self.wow.AXFrontmost
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
	def __init__(self):
		pids = self._getWoWPids()
		print(pids)
		if(len(pids) != 0):
			self.wow = am.getAppRefByPid(int(pids[0]))
		else:
			print "World of Warcraft is not running, or is not named 'World of Warcraft'"
			sys.exit(0)
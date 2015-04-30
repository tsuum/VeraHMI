import gps, threading, time, sys
 
class GPSHandler(threading.Thread):
	def __init__(self, gui = None):
		threading.Thread.__init__(self)
		self.session = gps.gps("localhost", "2947")
		self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
		self.deamon = True
		self.GPSValues = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
		self.attributeNames = {'time': 0, 'lon': 1, 'lat': 2, 'alt': 3, 'climb': 4, 'speed': 5, 'device': 6, 'mode': 7, 'ept': 8, 'epx': 9, 'epy': 10, 'epv': 11, 'track': 12, 'epd': 13, 'eps': 14, 'epc': 15}

		self.unavailableCount = 0

		if gui != None:
			self.gui = gui
			self.gui.setGPS(self)
			self.gui.setStatus(1, 1, "Started")
		else:
			self.gui = None

	def run(self):
		while True:
			try:
				report = self.session.next()
				# Wait for a 'TPV' report and display the current time
				# To see all report data, uncomment the line below
				#print report
				if report['class'] == 'TPV':
					if self.gui != None:
						self.gui.connectGPS()
					self.unavailableCount = 0
					for attr in self.attributeNames.keys():
						if hasattr(report, attr):
							#print("attr: " + attr + " number: " + str(self.attributeNames[attr]))
							self.GPSValues[self.attributeNames[attr]] = report[attr]
						else:
							self.GPSValues[self.attributeNames[attr]] = None
							#print("Can't find " + attr)
				else:
					time.sleep(1)
					if self.gui != None:
						self.unavailableCount += 1
						if self.unavailableCount >= 5:
							self.gui.disconnectGPS()
							print("GPS disconnected")

			except KeyError:
				pass
			except StopIteration:
				session = None
				print "GPSD has terminated"

	def getGPSAttr(self, value):
		for attr in self.attributeNames.keys():
			if(attr == value):
				return self.GPSValues[self.attributeNames[attr]]

	def getGPSPos(self):
		return (self.getGPSAttr("lat"), self.getGPSAttr('lon'), self.getGPSAttr('alt'), self.getGPSAttr('speed'))

if __name__ == '__main__':
	try:
		gps = GPSHandler()
		gps.start()
		while True:
			(lat, lon, alt, speed) = gps.getGPSPos()
			print(lat, lon, alt, speed)
			time.sleep(1)

	except (KeyboardInterrupt, SystemExit):
		gps._Thread__stop()
		sys.exit("\n\ntBye...")



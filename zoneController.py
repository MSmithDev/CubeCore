class ledZone():
    def __init__(self, zoneId, indexStart, indexStop):
        self.zoneId = zoneId
        self.indexStart = indexStart
        self.indexStop = indexStop

class zoneController():
    #Manually added zones
    ledZones = [
        ledZone(0,0,49),
        ledZone(1,50,99),
        ledZone(2,100,149),
        ledZone(3,150,199),
        ledZone(4,200,249),
        ledZone(5,250,299),
        ledZone(6,300,349),
        ledZone(7,350,399),
        ledZone(8,400,449),
        ledZone(9,500,549)
    ]

    def addZone(self, zone):
        self.ledZones.append(zone)

    def removeZone(self, zoneId):
        for zone in self.ledZones:
            if(zone.zoneId == zoneId):
                self.ledZones.remove(zone)
                            
    def removeAllZones(self):
        self.ledZones = []

    def getZoneById(self, id):
        for zone in self.ledZones:
            if(zone.zoneId == id):
                return zone

    def printZones(self):
        for zone in self.ledZones:
            print("Zone ",zone.zoneId, "Start: ",zone.indexStart, " Stop: ",zone.indexStop )

    def printZone(self, zone):
        print("Zone ",zone.zoneId, "Start: ",zone.indexStart, " Stop: ",zone.indexStop )

cmd = zoneController()
cmd.printZone(cmd.getZoneById(4))

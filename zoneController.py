class ledZone():
    def __init__(self, zoneId, indexStart, indexSize):
        self.zoneId = zoneId
        self.indexStart = indexStart
        self.indexSize = indexSize

class zoneController():
    #Manually added zones
    ledZones = [
        ledZone(0,0,49),
        ledZone(1,50,49),
        ledZone(2,100,49),
        ledZone(3,150,49),
        ledZone(4,200,49),
        ledZone(5,250,49),
        ledZone(6,300,49),
        ledZone(7,350,49),
        ledZone(8,400,49),
        ledZone(9,500,49)
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

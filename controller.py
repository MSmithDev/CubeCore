import socket
import time
 
 
appsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
udp_app = "127.0.0.1"
app_port = 12345
 
appsock.bind((udp_app,app_port))
 
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 55330
index = 0
 

class appZone():
    def __init__(self, index, red, green, blue):
        self.index = index
        self.red = red
        self.green = green
        self.blue = blue


def parseRawPacket(packet):
    packetLen = len(packet)
    
    if(packetLen == 2):
        print("Keep-Alive Packet")
    elif(packetLen > 5):
        zonesChanged = (packetLen-2)//4
        print("LED Command Data for ", zonesChanged, " zones")
        rawCmd = packet[2:packetLen]
        test = []
        
        for zone in range(zonesChanged):
            zoneIndex = (zone*4)
            zoneR =((zone*4)+1)
            zoneG =((zone*4)+2)
            zoneB =((zone*4)+3)
            test.append(appZone(rawCmd[zoneIndex],rawCmd[zoneR],rawCmd[zoneG],rawCmd[zoneB]))

            #Print test obj
        for x in test:
            print("Zone: ", x.index, "RGB: ", x.red,":",x.green,":",x.blue)
        print("End of packet \n\n")


    else:
        print("Bad Packet")

def ledPop(indexHigh,indexLow,size,r,g,b):
    data = [4,2,indexHigh,indexLow]
    for x in range(size):
        data.append(r)
        data.append(g)
        data.append(b)
    return bytearray(data)

clientSock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

for i in range(999999999):
    data,addr = appsock.recvfrom(1024)
    #print("recv: ",data,"from ",addr)
    app = list(data)
    parseRawPacket(app)
    #print(app)
    #if(len(app) > 6 ):
        #if(app[2] == 0):
            #Message = ledPop(0, 10, 100,app[3],app[4],app[5])
            #clientSock.sendto (Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    #elif(len(app) == 2):
        #Keep Alive packet
        #Message = bytearray([1,255])
        #clientSock.sendto (Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    time.sleep(0.005)






## WARLS Packet Structure

## [1, 255, 0, 181, 186, 193, 1, 63, 67, 73, 2, 27, 33, 38, 3, 39, 41, 42, 4, 43, 43, 43]
#
# [0] = mode
# [1] = timeout
# [2] = LED Index [0]
# [3] = LED R
# [4] = LED G
# [5] = LED B
# [6] = LED Index [1]
# [7] = LED R
# [8] = .....
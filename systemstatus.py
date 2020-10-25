#!/usr/bin/python3
from wiserHeatingAPI import wiserHub
import json
import sys
dev="false" # set to true to see raw data

# Get Wiser Parameters from keyfile
try:
    with open('wiserkeys.params', 'r') as f:
        data = f.read().split('\n')
except FileNotFoundError as e:
    print("{}, {}/{}".format(e.strerror, 'wiserkeys.params', keyfile)    )
else:
    wiserkey=""
    wiserip=""

    for lines in data:
        line=lines.split('=')    
        if line[0]=='wiserkey':
            wiserkey=line[1]
        if line[0]=='wiserhubip':
            wiserip=line[1]

    try:
#    
        try:
            wh = wiserHub.wiserHub(wiserip,wiserkey)
        except:
            print("Unable to connect to Wiser Hub {}".format(sys.exc_info()[1])    )
            print (' Wiser Hub IP= {}'.format(wiserip))
            print (' WiserKey= {}'.format(wiserkey))
        else:
            if dev=="true":
			# Heating State
                print("--------------------------------")
                print ("System Data {} ".format(wh.getSystem()))
                print("--------------------------------")

                print("--------------------------------")
                print ("Hub Data {} ".format(wh.getHubData()))
                print("--------------------------------")

                print("--------------------------------")
                print ("Raw Room Data {} ".format(wh.getRooms()))
                print("--------------------------------")

                print("--------------------------------")
                print ("Device Data {} ".format(wh.getDevices()))
                print ("--------------------------------")

            system=wh.getSystem()
            print ("System\n    {}".format(system.get("LocalDateAndTime")     )   )
            print ("    Heating: {}, HeatingButtonOverride: {}".format(wh.getHeatingRelayStatus(),system.get("HeatingButtonOverrideState")    )    )
            if wh.getHotwater():
                print ("    Hot Water: {}, HotWaterButtonOverride: {}\n".format(wh.getHotwaterRelayStatus(),system.get("HotWaterButtonOverrideState")    )    )
            print ("    Pairing: {}, CloudConnection: {}, OpenThermConnection: {}\n".format(system.get("PairingStatus"),system.get("CloudConnectionStatus"),system.get("OpenThermConnectionStatus")    )    )
            print ("Controller")
            dev=wh.getDevice(0)
            print ("    {},  F/W: {}, Locked: {}".format(dev.get("ModelIdentifier"),system.get("ActiveSystemVersion"),dev.get("DeviceLockEnabled")     )   )
            print ("        WiFi Signal: {}, ReceiveCont: {}".format(dev.get("DisplayedSignalStrength"),dev.get("ReceptionOfController")     )   )
            zig=wh.getHubData().get("Zigbee")
            print ("    Zigbee: {}".format(zig    )    )
            print ("    UpgradeInfo:")
            for firm in wh.getHubData().get("UpgradeInfo"):
                print ("        {}".format(firm))

#           List all Rooms
  
            findValve=0
            roomName=None
            print()
            for room in wh.getRooms():
                smartValves=room.get("SmartValveIds")
                roomStat=room.get("RoomStatId")
                print ("{} - setpoint: {}C, current temp: {}C, Demand: {}%, OutputState: {}".format(room.get("Name"),room.get("CurrentSetPoint")/10,room.get("CalculatedTemperature")/10,room.get("PercentageDemand"),room.get("ControlOutputState")    )    )
                if roomStat:
#                    print ("\troomStatId: {}".format(roomStat))
                    dev=wh.getDevice(roomStat)
                    bat = dev.get("BatteryVoltage")
                    if bat != None:
                        bat = bat/10
                    else:
                        bat = "?.?"
                    batlevel=dev.get("BatteryLevel")                    
                    if batlevel == None:
                       batlevel = "Unknown"
                    print ("    {} H/W: {}, SerialNo: {}, F/W: {}, Batt: {}V {}, Locked: {}".format(dev.get("ProductType"),dev.get("HardwareVersion"),dev.get("SerialNumber"),dev.get("ActiveFirmwareVersion"),bat,batlevel,dev.get("DeviceLockEnabled")     )   )
                    print ("        Signal: {}, ReceiveCont: {}, 'ReceiveDev: {}".format(dev.get("DisplayedSignalStrength"),dev.get("ReceptionOfController"),dev.get("ReceptionOfDevice")     )   )
                if smartValves:
#                    print ("    SmartValveIds: {}".format(smartValves))
                    for smartvalve in smartValves:
                        dev=wh.getDevice(smartvalve)
                        bat = dev.get("BatteryVoltage")
                        if bat != None:
                            bat = bat/10
                        else:
                            bat = "?.?"
                        batlevel=dev.get("BatteryLevel")                    
                        if batlevel == None:
                            batlevel = "Unknown"
                        print ("    {} H/W: {}, SerialNo: {}, F/W: {}, Batt: {}V {}, Locked: {}".format(dev.get("ProductType"),dev.get("HardwareVersion"),dev.get("SerialNumber"),dev.get("ActiveFirmwareVersion"),bat,batlevel,dev.get("DeviceLockEnabled")    )   )
                        print ("        Signal: {}, ReceiveCont: {}, 'ReceiveDev: {}".format(dev.get("DisplayedSignalStrength"),dev.get("ReceptionOfController"),dev.get("ReceptionOfDevice")     )   )

    except json.decoder.JSONDecodeError as ex:
        print("JSON Exception")

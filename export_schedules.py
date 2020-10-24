#!/usr/bin/python3
from wiserHeatingAPI import wiserHub
import json
import sys

# the optional parameter is the name of the file that you want to save it as
# defaults to ./roomschedules.txt if not set

# Get Wiser Parameters from keyfile
try:
    with open('wiserkeys.params', 'r') as f:
        data = f.read().split('\n')
except FileNotFoundError as e:
    print("{}, {}/{}".format(e.strerror, 'wiserkeys.params', keyfile)    )
else:
    if len(sys.argv) > 1:
        filename=sys.argv[1]
    else:
        filename="./roomschedules.txt"

    wiserkey=""
    wiserip=""

    for lines in data:
        line=lines.split('=')    
        if line[0]=='wiserkey':
            wiserkey=line[1]
        if line[0]=='wiserhubip':
            wiserip=line[1]

    try:
        try:
            wh = wiserHub.wiserHub(wiserip,wiserkey)
        except:
            print("Unable to connect to Wiser Hub {}".format(sys.exc_info()[1])    )
            print (' Wiser Hub IP= {} , WiserKey= {}'.format(wiserip,wiserkey))
        else:
            with open(filename, "w") as f:
                for room in wh.getRooms():               
                    id=room.get("id")
                    print("# {} - {}".format(id,room.get("Name")))
                    roomschedule = wh.getRoomSchedule(id)
                    print("{}".format(roomschedule))
                    f.write("# {} - {}\n".format(id,room.get("Name")))
                    json.dump(roomschedule, f)
                    f.write("\n")
                f.close()
                print("\nRoom Schedules saved as {}".format(filename))
    
    except json.decoder.JSONDecodeError as ex:
        print("JSON Exception")

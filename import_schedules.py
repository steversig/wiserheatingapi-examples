#!/usr/bin/python3
from wiserHeatingAPI import wiserHub
import json
import sys

# the optional parameter is the name of the file that you want to import from
# defaults to ./roomschedules.txt if not specified

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
            with open(filename, "r") as f:
                for line in f:                
                    if line[0] == "#":
                        id = line[2:line.find(" -")]  # get room id                
                        room = line[line.find(" -"):] # get room name
                    else:
                        line = line[:-1]  # get rid of \n                  
                        print(line)
                        print("Importing schedule for room {}{}".format(id,room))
                        data = json.loads(line)                        
                        wh.setRoomSchedule(int(id), data)              
            f.close()
    
    except json.decoder.JSONDecodeError as ex:
        print("JSON Exception")

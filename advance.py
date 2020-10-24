#!/usr/bin/python3
from wiserHeatingAPI import wiserHub
import json
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)

# the command line parameter is the name of the room that you want to advance or All for all rooms
# quote any room names with spaces in them eg "Bed 3"

# Get Wiser Parameters from keyfile
try:
    with open('wiserkeys.params', 'r') as f:
        data = f.read().split('\n')
except FileNotFoundError as e:
    _LOGGER.info("{}, {}/{}".format(e.strerror, 'wiserkeys.params', keyfile)    )
else:
    if len(sys.argv) > 1:
        adv_room = sys.argv[1]
    else:
        _LOGGER.info("No room specified")
        sys. exit()

    wiserkey=""
    wiserip=""

    for lines in data:
        line=lines.split('=')    
        if line[0] == 'wiserkey':
            wiserkey = line[1]
        if line[0] == 'wiserhubip':
            wiserip = line[1]

    try:
        try:
            wh = wiserHub.wiserHub(wiserip,wiserkey)
        except:
            _LOGGER.info("Unable to connect to Wiser Hub {}".format(sys.exc_info()[1])    )
            _LOGGER.info(' Wiser Hub IP= {}\n WiserKey= {}'.format(wiserip,wiserkey))
        else:
            for room in wh.getRooms():               
                id = room.get("id")
                name = room.get("Name")
                _LOGGER.info("# {} - {}".format(id,name))
                if adv_room == "All" or name == adv_room:
                    wh.setRoomScheduleAdvance(id)   

    except json.decoder.JSONDecodeError as ex:
        _LOGGER.info("JSON Exception")

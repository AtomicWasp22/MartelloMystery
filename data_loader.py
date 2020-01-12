from Sensor import Sensor
import json

def load_data():

    device_inventory = {}
    #test_sensor = Sensor()
    with open("Murder-on-the-2nd-Floor-Raw-Data.json") as file:
        data = json.load(file)

        with open("coords.json") as coordFile:
            coords = json.load(coordFile)

            for time in data:
                event = data[time]
                device_type = event["device"]
                device_id = event["device-id"]

                if device_id not in device_inventory:
                    _x = coords[device_id]["x"]
                    _y = coords[device_id]["y"]

                    device = Sensor(device_type, device_id, _x, _y)
                    device_inventory.update({device_id: device})

                device_inventory[device_id].addEvent(time, event)

    for dev in device_inventory:
        print(device_inventory[dev].x)
        ##for event in device_inventory[dev].event_log:
            #print(event)
    return device_inventory
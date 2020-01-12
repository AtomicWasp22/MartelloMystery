from Sensor import Sensor
import json

device_inventory = []
#test_sensor = Sensor()
with open("Murder-on-the-2nd-Floor-Raw-Data.json") as file:
    data = json.load(file)
    """
    time = "1578151801"
event = data[time]
device = data[event]["device-id"]

device_inventory[device].addEvent(event)
"""


    for time in data:
        device_type = data[time]["device"]
        device_id = data[time]["device-id"]

        if device_id in device_inventory:
            #device_inventory[device].addEvent(event)
            #print(data[event]["device-id"])
            pass
        else:
            device = Sensor(device_type, device_id)
            device_inventory.append(device)

    print(device_inventory)

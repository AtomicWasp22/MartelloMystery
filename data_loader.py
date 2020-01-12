from Sensor import Sensor
import json

device_inventory = {}
#test_sensor = Sensor()
with open("Murder-on-the-2nd-Floor-Raw-Data.json") as file:
    data = json.load(file)


    for time in data:
        event = data[time]
        device_type = event["device"]
        device_id = event["device-id"]

        if device_id not in device_inventory:
            device = Sensor(device_type, device_id)
            device_inventory.update({device_id: device})

        device_inventory[device_id].addEvent(time, event)

for dev in device_inventory:
    for event in device_inventory[dev].event_log:
        print(event)
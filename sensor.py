from Event import Event
class Sensor:
    """Represents a sensor"""

    def __init__(self, device_type, device_id, x, y):
        self.device_type = device_type
        self.device_id = device_id
        self.event_log = [] #Custom Event Log class
        self.x = x
        self.y = y

    def addEvent(self, time, event):
        self.event_log.append(Event(time, event))

    def __str__(self):
        return "Device Type: %s, Device ID: %s" % (self.device_type, self.device_id)

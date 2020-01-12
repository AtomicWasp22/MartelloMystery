from EventLog import EventLog
class Sensor:
    """Represents a sensor"""

    events = EventLog

    def __init__(self, device_type, device_id):
        self.device_type = device_type
        self.device_id = device_id
        self.event_log = EventLog() #Custom Event Log class

    def addEvent(self, time, event):
        self.events += event

    def 
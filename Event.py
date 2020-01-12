class Event:

    def __init__(self, time, event):
        self.time = time
        self.type = event["event"]
        self.guest = event["guest-id"]

    def __str__(self):
        return "Time: %s Event Type: %s Guest: %s" % (self.time, self.type, self.guest)

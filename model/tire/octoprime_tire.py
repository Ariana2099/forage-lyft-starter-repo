from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors
    
    def needs_service(self):
        for i in range(0, len(self.sensors)):
            sum = sum + self.sensors[i]

        return sum >= 3
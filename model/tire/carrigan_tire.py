from tire import Tire

class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors
    
    def needs_service(self):
        i = 0
        while i < len(self.sensors):
            if self.sensors[i] >= 0.9:
                return True
            i += 1
        return False

        


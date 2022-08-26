from abc import ABC, abstractclassmethod

class Tire(ABC):
    def __init__(self, sensors):
        self.sensors = sensors

    @abstractclassmethod
    def needs_service(self):
        pass
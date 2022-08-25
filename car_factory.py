from car import Car
from parts import Engine
from parts import Battery

class CarFactory(Car, Engine, Battery):

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = Engine.CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = Battery.SpindlerBattery(last_service_date, current_date)
        return Car(capulet_engine, spindler_battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = Engine.WilloughbyEngine(last_service_mileage, current_mileage)
        spindler_battery = Battery.SpindlerBattery(last_service_date, current_date)
        return Car(willoughby_engine, spindler_battery)

    def create_pallindrome(self, current_date, last_service_date, warning_light_on):
        sternman_engine = Engine.SternmanEngine(warning_light_on)
        nubbin_battery = Battery.NubbinBattery(last_service_date, current_date)
        return Car(sternman_engine, nubbin_battery)

    def create_rorshach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = Engine.WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin_battery = Battery.NubbinBattery(last_service_date, current_date)
        return Car(willoughby_engine, nubbin_battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = Engine.CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = Battery.NubbinBattery(last_service_date, current_date)
        return Car(capulet_engine, nubbin_battery)

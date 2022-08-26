import unittest
import numpy
from datetime import datetime

from model import Engine
from model import Battery
from model import Tire


class testCapulet(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        cap_eng = Engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(cap_eng.needs_service())

    def test_engine_needs_service(self):
        current_mileage = 50000
        last_service_mileage = 0
        cap_eng = Engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(cap_eng.needs_service())

    def test_engine_should_not_be_serviced_threshold(self):
        current_mileage = 30000
        last_service_mileage = 0
        cap_eng = Engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(cap_eng.needs_service())

    def test_engine_needs_service_threshold(self):
        current_mileage = 30001
        last_service_mileage = 0
        cap_eng = Engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(cap_eng.needs_service())

class testWilloughby(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        wil_eng = Engine.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(wil_eng.needs_service())

    def test_engine_needs_service(self):
        current_mileage = 80000
        last_service_mileage = 0
        wil_eng = Engine.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(wil_eng.needs_service())

    def test_engine_should_not_be_serviced_threshold(self):
        current_mileage = 60000
        last_service_mileage = 0
        wil_eng = Engine.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(wil_eng.needs_service())

    def test_engine_needs_service_threshold(self):
        current_mileage = 60001
        last_service_mileage = 0
        wil_eng = Engine.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(wil_eng.needs_service())

class testSternman(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        indicator_on = False
        stern_eng = Engine.SternmanEngine(indicator_on)
        self.assertFalse(stern_eng.needs_service())

    def test_engine_needs_service(self):
        indicator_on = True
        stern_eng = Engine.SternmanEngine(indicator_on)
        self.assertTrue(stern_eng.needs_service())

class testSpindler(unittest.TestCase):
    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4)
        spin_bat = Battery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spin_bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        spin_bat = Battery.SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spin_bat.needs_service())

    def test_battery_needs_service_threshold(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3, day = current_date.day + 10)
        spin_bat = Battery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spin_bat.needs_service())

    def test_battery_should_not_be_service_threshold(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        spin_bat = Battery.SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spin_bat.needs_service())

class testNubbin(unittest.TestCase):
    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        nub_bat = Battery.NubbinBattery(last_service_date, current_date)
        self.assertTrue(nub_bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        nub_bat = Battery.NubbinBattery(last_service_date, current_date)
        self.assertFalse(nub_bat.needs_service())

    def test_battery_needs_service_threshold(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4, day = current_date.day + 10)
        nub_bat = Battery.NubbinBattery(last_service_date, current_date)
        self.assertTrue(nub_bat.needs_service())

    def test_battery_should_not_be_service_threshold(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4)
        nub_bat = Battery.NubbinBattery(last_service_date, current_date)
        self.assertFalse(nub_bat.needs_service())

class testCarriagan(unittest.TestCase):
    def test_one_tire_needs_service(self):
        sensors = numpy.array([0, 0, 0, 1])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())

    def test_two_tires_needs_service(self):
        sensors = numpy.array([0, 0, 1, 1])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())

    def test_three_tires_needs_service(self):
        sensors = numpy.array([0, 1, 1, 1])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())
    
    def test_all_tires_needs_service(self):
        sensors = numpy.array([1, 1, 1, 1])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())

    def test_one_tire_needs_service_threshold(self):
        sensors = numpy.array([0, 0, 0, 0.9])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())

    def test_two_tires_needs_service_threshold(self):
        sensors = numpy.array([0, 0, 0.9, 0.9])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())

    def test_three_tires_needs_service_threshold(self):
        sensors = numpy.array([0, 0.9, 0.9, 0.9])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())

    def test_all_tires_needs_service_threshold(self):
        sensors = numpy.array([0.9, 0.9, 0.9, 0.9])
        car_tire = Tire.CarriganTire(sensors)
        self.assertTrue(car_tire.needs_service())
    
    def test_tires_should_not_be_serviced(self):
        sensors = numpy.array([0, 0, 0, 0])
        car_tire = Tire.CarriganTire(sensors)
        self.assertFalse(car_tire.needs_service())

class testOctoprime(unittest.TestCase):
    def test_tire_needs_service(self):
        sensors = numpy.array([0.5, 1, 1, 0.7])
        octo_tire = Tire.OctoprimeTire(sensors)
        self.assertTrue(octo_tire.needs_service())

    def test_tire_needs_service_threshold(self):
        sensors = numpy.array([0, 1, 1, 1])
        octo_tire = Tire.OctoprimeTire(sensors)
        self.assertTrue(octo_tire.needs_service())

    def test_tires_should_not_be_serviced(self):
        sensors = numpy.array([0, 0.2, 1, 0.1])
        octo_tire = Tire.OctoprimeTire(sensors)
        self.assertFalse(octo_tire.needs_service())

if __name__ == '__main__':
    unittest.main()

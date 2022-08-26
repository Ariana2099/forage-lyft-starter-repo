import unittest
from datetime import datetime

from model import Engine
from model import Battery


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
        last_service_date = current_date.replace(year = current_date.year - 3)
        spin_bat = Battery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spin_bat.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        spin_bat = Battery.SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spin_bat.needs_service())

    def test_battery_needs_service_threshold(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 2, day = current_date.day + 10)
        spin_bat = Battery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spin_bat.needs_service())

    def test_battery_should_not_be_service_threshold(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 2)
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
    

if __name__ == '__main__':
    unittest.main()

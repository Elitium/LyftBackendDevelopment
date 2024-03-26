import unittest
import datetime

from battery.battery_type.nubbin_battery import NubbinBattery
from battery.battery_type.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2010, 5, 9)
        last_service_date = datetime.datetime(2007,5,8)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2008, 5, 9)
        last_service_date = datetime.datetime(2007,5,8)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2011, 5, 9)
        last_service_date = datetime.datetime(2007,5,8)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2010, 5, 9)
        last_service_date = datetime.datetime(2007,5,8)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

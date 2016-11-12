import unittest

from lsstbroker import observation


class TestObservation(unittest.TestCase):

    def test_constructor(self):
        time = 0
        light = 50.2
        error = 0.005

        test_observation = observation.Observation(time, light, error)

        self.assertEquals(time, test_observation.time)
        self.assertEquals(light, test_observation.light)
        self.assertEquals(error, test_observation.error)

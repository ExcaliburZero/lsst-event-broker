import unittest

from lsstbroker import observation


class TestObservation(unittest.TestCase):
    def test_constructor(self):
        object_id = "LSST-00001"
        time = 0
        light = 50.2
        error = 0.005

        test_observation = observation.Observation(object_id, time, light, error)

        self.assertEquals(object_id, test_observation.object_id)
        self.assertEquals(time, test_observation.time)
        self.assertEquals(light, test_observation.light)
        self.assertEquals(error, test_observation.error)

    def test_eq(self):
        object_id = "LSST-00001"
        time = 0
        light = 50.2
        error = 0.005

        test_observation = observation.Observation(object_id, time, light, error)

        self.assertTrue(test_observation == test_observation)

        # Test two observations with the same data
        test_observation2 = observation.Observation(object_id, time, light, error)

        self.assertTrue(test_observation2 == test_observation)

        # Test two observations with different data
        test_observation3 = observation.Observation("123", 4, 2, 0.5)

        self.assertFalse(test_observation3 == test_observation)

        # Test comparing a non observation
        self.assertFalse(test_observation == 5)

    def test_to_tuple(self):
        test_observations = [
            observation.Observation("LSST-00001", 0, 50.2, 0.005),
            observation.Observation("LSST-00002", 5, 49.9, 0.005)
        ]

        expected_observation_data = [
            ("LSST-00001", 0, 50.2, 0.005),
            ("LSST-00002", 5, 49.9, 0.005)
        ]

        actual_observation_data = [
            test_observations[0].to_tuple(),
            test_observations[1].to_tuple()
        ]

        self.assertEquals(expected_observation_data[0], actual_observation_data[0])
        self.assertEquals(expected_observation_data[1], actual_observation_data[1])

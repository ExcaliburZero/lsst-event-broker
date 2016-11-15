import unittest

from lsstbroker import handler
from lsstbroker import observation


class TestMySqlDatabaseHandler(unittest.TestCase):

    def test_constructor(self):
        test_host = "localhost"
        test_database_name = "Database1"
        test_username = "bob"
        test_password = "hunter2"

        test_handler = handler.MySqlDatabaseHandler(test_host, test_database_name, test_username, test_password)

        self.assertEquals(test_host, test_handler.host)
        self.assertEquals(test_database_name, test_handler.database_name)
        self.assertEquals(test_username, test_handler.username)
        self.assertEquals(test_password, test_handler.password)

    def test_parse_observations(self):
        test_observation_data = [
            ["LSST-00001", 0, 50.2, 0.005],
            ["LSST-00001", 5, 49.9, 0.005]
        ]

        expected_observations = [
            observation.Observation("LSST-00001", 0, 50.2, 0.005),
            observation.Observation("LSST-00001", 5, 49.9, 0.005)
        ]

        actual_observations = handler.parse_observations(test_observation_data)

        self.assertEquals(expected_observations, actual_observations)

import unittest

from lsstbroker import binary_classifier
from lsstbroker import observation


class TestBinaryClassifier(unittest.TestCase):

    def test_run(self):
        def function(_): return 0.5
        test_binary_classifier = binary_classifier.BinaryClassifier("001", function)

        observations = [observation.Observation("LSST-00001", 0, 50.2, 0.005)]
        results = ("LSST-00001", 0, "001", 0.5)
        self.assertEquals(results, test_binary_classifier.run(observations))

        # Test creating multiple BinaryClassifiers
        def function2(_): return 0.7
        test_binary_classifier2 = binary_classifier.BinaryClassifier("002", function2)

        results2 = ("LSST-00001", 0, "002", 0.7)
        self.assertEquals(results2, test_binary_classifier2.run(observations))

    def test_constructor(self):
        def function(_): return 0.5
        name = "001"
        test_binary_classifier = binary_classifier.BinaryClassifier(name, function)

        self.assertEquals(name, test_binary_classifier.name)
        self.assertEquals(function, test_binary_classifier.classifying_function)
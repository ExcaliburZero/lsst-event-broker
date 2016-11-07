import unittest

from lsstbroker import binary_classifier


class TestBinaryClassifier(unittest.TestCase):

    def test_run(self):
        def function(_): return 0.5
        test_binary_classifier = binary_classifier.BinaryClassifier(function)

        observations = []
        self.assertEquals(0.5, test_binary_classifier.run(observations))

        # Test creating multiple BinaryClassifiers
        def function2(_): return 0.7
        test_binary_classifier2 = binary_classifier.BinaryClassifier(function2)

        self.assertEquals(0.7, test_binary_classifier2.run(observations))


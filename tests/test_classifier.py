import unittest

from lsstbroker import binary_classifier
from lsstbroker import classifier


class TestClassifier(unittest.TestCase):

    def test_add_binary_classifier(self):
        def function(_): return 0.5
        test_binary_classifier = binary_classifier.BinaryClassifier("001", function)
        test_classifier = classifier.Classifier()

        test_classifier.add_binary_classifier(test_binary_classifier)

        self.assertEquals(test_binary_classifier, test_classifier.binary_classifiers[0])

        # Try to add None
        test_classifier2 = classifier.Classifier()

        test_classifier2.add_binary_classifier(None)

        self.assertEquals([], test_classifier2.binary_classifiers)

    def test_set_determining_classifier(self):
        def function(_): return 0.7
        test_determining_classifier = binary_classifier.BinaryClassifier("D001", function)

        def continue_function(x):
            (_, value) = x
            return value > 0.5
        test_classifier = classifier.Classifier()

        test_classifier.set_determining_classifier(test_determining_classifier, continue_function)

        self.assertEquals(test_determining_classifier, test_classifier.determining_classifier)
        self.assertEquals(continue_function, test_classifier.continue_function)

        # Run with just a determining classifier
        no_observations = []
        expected_results = [("D001", 0.7)]
        self.assertEquals(expected_results, test_classifier.run(no_observations))

    def test_run_no_determining(self):
        def function(_): return 0.7
        test_binary_classifier = binary_classifier.BinaryClassifier("001", function)
        test_classifier = classifier.Classifier()

        test_classifier.add_binary_classifier(test_binary_classifier)

        observations = []
        results = [("001", 0.7)]
        self.assertEquals(results, test_classifier.run(observations))

        # Test multiple BinaryClassifiers
        def function2(_): return 0.5
        test_binary_classifier2 = binary_classifier.BinaryClassifier("002", function2)

        test_classifier.add_binary_classifier(test_binary_classifier2)

        results2 = [("001", 0.7), ("002", 0.5)]
        self.assertEquals(results2, test_classifier.run(observations))

    def test_run_with_determining(self):
        # Test continue function evaluating to true
        def function(_): return 0.7
        test_determining_classifier = binary_classifier.BinaryClassifier("D001", function)

        def function2(_): return 0.6
        test_binary_classifier = binary_classifier.BinaryClassifier("002", function2)

        def continue_function(x):
            (_, value) = x
            return value > 0.5
        test_classifier = classifier.Classifier()

        test_classifier.set_determining_classifier(test_determining_classifier, continue_function)
        test_classifier.add_binary_classifier(test_binary_classifier)

        observations = []
        results = [("D001", 0.7), ("002", 0.6)]
        self.assertEquals(results, test_classifier.run(observations))

        # Test continue function evaluating to false
        def function3(_): return 0.3
        test_determining_classifier2 = binary_classifier.BinaryClassifier("D003", function3)
        test_classifier.set_determining_classifier(test_determining_classifier2, continue_function)

        observations = []
        results = [("D003", 0.3)]
        self.assertEquals(results, test_classifier.run(observations))

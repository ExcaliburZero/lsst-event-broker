import unittest

from lsstbroker import binary_classifier
from lsstbroker import classifier
from lsstbroker import classifier_box
from lsstbroker import observation


class TestClassifierBox(unittest.TestCase):

    def test_add_classifier(self):
        test_classifier = classifier.Classifier()
        test_classifier_box = classifier_box.ClassifierBox()

        test_classifier_box.add_classifier(test_classifier)

        self.assertEquals([test_classifier], test_classifier_box.classifiers)

    def test_run_none(self):
        test_classifier_box = classifier_box.ClassifierBox()
        one_observation = [observation.Observation("LSST-00001", 0, 50.2, 0.005)]

        result = test_classifier_box.run(one_observation)
        self.assertEquals([], result)

    def test_run_one(self):
        def function(_): return 0.7
        test_binary_classifier = binary_classifier.BinaryClassifier("001", function)
        test_classifier = classifier.Classifier()
        test_classifier_box = classifier_box.ClassifierBox()

        test_classifier.add_binary_classifier(test_binary_classifier)
        test_classifier_box.add_classifier(test_classifier)

        one_observation = [observation.Observation("LSST-00001", 0, 50.2, 0.005)]
        expected_results = [[("LSST-00001", 0, "001", 0.7)]]

        actual_results = test_classifier_box.run(one_observation)
        self.assertEquals(expected_results, actual_results)

    def test_run_multiple(self):
        def function1(_): return 0.7
        test_binary_classifier1 = binary_classifier.BinaryClassifier("001", function1)
        def function2(_): return 0.8
        test_binary_classifier2 = binary_classifier.BinaryClassifier("002", function2)
        test_classifier1 = classifier.Classifier()
        test_classifier2 = classifier.Classifier()
        test_classifier_box = classifier_box.ClassifierBox()

        test_classifier1.add_binary_classifier(test_binary_classifier1)
        test_classifier2.add_binary_classifier(test_binary_classifier2)
        test_classifier_box.add_classifier(test_classifier1)
        test_classifier_box.add_classifier(test_classifier2)

        one_observation = [observation.Observation("LSST-00001", 0, 50.2, 0.005)]
        expected_results = [[("LSST-00001", 0, "001", 0.7)], [("LSST-00001", 0, "002", 0.8)]]

        actual_results = test_classifier_box.run(one_observation)
        self.assertEquals(expected_results, actual_results)

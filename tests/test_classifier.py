import unittest

from lsstbroker import binary_classifier
from lsstbroker import classifier


class TestClassifier(unittest.TestCase):

    def test_add_binary_classifier(self):
        def function(_): return 0.5
        test_binary_classifier = binary_classifier.BinaryClassifier(function)
        test_classifier = classifier.Classifier()

        test_classifier.add_binary_classifier(test_binary_classifier)

        self.assertEquals(test_binary_classifier, test_classifier.binary_classifiers[0])

        # Try to add None
        test_classifier2 = classifier.Classifier()

        test_classifier2.add_binary_classifier(None)

        self.assertEquals([], test_classifier2.binary_classifiers)

    def test_set_determining_classifier(self):
        def function(_): return 0.5
        test_binary_classifier = binary_classifier.BinaryClassifier(function)
        test_classifier = classifier.Classifier()

        with self.assertRaises(NotImplementedError) as context:
            test_classifier.set_determining_classifier(test_binary_classifier)

        self.assertTrue("Have not yet implemented Determining Classifiers" in context.exception)

    def test_run(self):
        def function(_): return 0.7
        test_binary_classifier = binary_classifier.BinaryClassifier(function)
        test_classifier = classifier.Classifier()

        test_classifier.add_binary_classifier(test_binary_classifier)

        observations = []
        self.assertEquals([0.7], test_classifier.run(observations))

        # Test multiple BinaryClassifiers
        def function2(_): return 0.5
        test_binary_classifier2 = binary_classifier.BinaryClassifier(function2)

        test_classifier.add_binary_classifier(test_binary_classifier2)

        self.assertEquals([0.7, 0.5], test_classifier.run(observations))


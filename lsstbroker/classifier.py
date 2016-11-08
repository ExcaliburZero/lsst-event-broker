class Classifier(object):
    """
    Represents a single Classifier composed of various BinaryClassifiers.
    """

    determining_classifier = None
    binary_classifiers = None

    def __init__(self):
        self.binary_classifiers = []

    def set_determining_classifier(self, binary_classifier):
        """
        Sets the given BinaryClassifier to be the Classifier's Determining Classifier.
        """
        raise NotImplementedError("Have not yet implemented Determining Classifiers")

    def add_binary_classifier(self, binary_classifier):
        """
        Adds the given BinaryClassifier to the Classifier.
        """
        if binary_classifier is not None:
            self.binary_classifiers.append(binary_classifier)

    def run(self, observations):
        """
        Runs the given Observation data through the Classifier's BinaryClassifiers and returns the results as a list.
        """
        results = []
        for binary_classifier in self.binary_classifiers:
            results.append(binary_classifier.run(observations))
        return results

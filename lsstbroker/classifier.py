from dask import delayed


class Classifier(object):
    """
    Represents a single Classifier composed of various BinaryClassifiers.
    """

    determining_classifier = None
    continue_function = None
    binary_classifiers = None

    def __init__(self):
        self.binary_classifiers = []

    def set_determining_classifier(self, determining_classifier, continue_function):
        """
        Sets the determining classifier and continue function of the Classifier, these are used to determine whether the
        observation data should be run through all of the binary classifiers or not.

        :param determining_classifier: A Binary Classifier that is used in determining whether to run the rest of the
        BinaryClassifiers.
        :param continue_function: A function that takes the results of the determining classifier and tells whether to
        run the rest of the BinaryClassifiers.
        """
        self.determining_classifier = determining_classifier
        self.continue_function = continue_function

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
        run_all_classifiers = True
        if self.determining_classifier is not None:
            determining_result = self.determining_classifier.run(observations)
            results.append(determining_result)
            should_continue = self.continue_function(determining_result)
            if not should_continue:
                run_all_classifiers = False

        if run_all_classifiers:
            calculations = []
            for binary_classifier in self.binary_classifiers:
                calc = delayed(binary_classifier.run)(observations)
                calculations.append(calc)
            results = results + delayed(calculations).compute()

        return results

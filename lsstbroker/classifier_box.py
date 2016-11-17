from dask import delayed


class ClassifierBox(object):

    classifiers = None

    def __init__(self):
        self.classifiers = []

    def add_classifier(self, classifier):
        """
        This method adds a specific classifier to the ClassifierBox
        """
        if classifier is not None:
            self.classifiers.append(classifier)

    def run(self, observations):
        """
        Method to be called to run the observations data that was
        aquired from the transient observation class
        """
        calculations = []
        for classifier in self.classifiers:
            calc = delayed(classifier.run)(observations)
            calculations.append(calc)

        results = delayed(calculations).compute()

        return results

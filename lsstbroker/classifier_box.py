class ClassifierBox(object):

    classifiers = []

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
        results = []
        for classifier in self.classifiers:
            result = classifier.run(observations)
            results.append(result)

        return results

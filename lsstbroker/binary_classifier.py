class BinaryClassifier(object):
    """
    Represents a Binary Classification function which takes in a list of Observations and returns a probability value.

    >>> def function(x): return 0.5
    >>> bc = BinaryClassifier(function)
    >>> bc.run([])
    0.5
    """

    classifying_function = None

    def __init__(self, classifying_function):
        """
        Constructor for the classification
        """
        self.classifying_function = classifying_function

    def run(self, observations):
        """
        Method to be called to run the observations data that was
        aquired from the transient observation class
        """
        return self.classifying_function(observations)

class BinaryClassifier(object):
    """
    Represents a Binary Classification function which takes in a list of Observations and returns a probability value.

    >>> def function(x): return 0.5
    >>> bc = BinaryClassifier("001", function)
    >>> bc.run([])
    ('001', 0.5)
    """

    classifying_function = None
    name = None

    def __init__(self, name, classifying_function):
        """
        Constructor for the classification
        """
        self.name = name
        self.classifying_function = classifying_function

    def run(self, observations):
        """
        Method to be called to run the observations data that was
        aquired from the transient observation class
        """
        result = self.classifying_function(observations)
        last_obs = observations[-1]
        return last_obs.object_id, last_obs.time, self.name, result

"""
This class will get the time value and error observation from each transient
and store that data into each specific transient. Afterwards this data can be used
to classify the data based on this information.
"""


class Observation(object):

    object_id = None
    time = None
    light = None
    error = None

    def __init__(self, object_id, time, light_value, error):
        """
        this method is to be called on by the event broker when it wants
        to geneerate a transients time, light-value and error, it will return
        a tuple.
        """
        self.object_id = object_id
        self.time = time
        self.light = light_value
        self.error = error

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            same_id = self.object_id == other.object_id
            same_time = self.time == other.time
            same_light = self.light == other.light
            same_error = self.error == other.error
            are_same = same_id and same_time and same_light and same_error
            return are_same
        else:
            return False

    def to_tuple(self):
        return self.object_id, self.time, self.light, self.error

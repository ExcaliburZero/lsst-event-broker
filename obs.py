from lsstbroker.binary_classifier import BinaryClassifier
from lsstbroker.observation import Observation

from rrLyraeBinaryClassifier import rrLyraeBinary

def main():

    input_file = "OGLE-SMC-RRLYR-0001.dat"
    (times, light_values, errors) = get_observations(input_file)

    observations = []
    for i in range(len(times)):
        obs = Observation(input_file, times[i], light_values[i], errors[i])
        observations.append(obs)

    binary_classifier = BinaryClassifier("Period", run)
    result = binary_classifier.run(observations)

    print result

def run(observations):
    rr_lyrae_binary = rrLyraeBinary(None, None)
    result = rr_lyrae_binary.run(observations)
    return result


def get_observations(input_file):
    lines = [line.rstrip('\n').split(" ") for line in open(input_file)]

    # Parse in the input data
    times = [line[0] for line in lines]
    light_values = [line[1] for line in lines]
    errors = [line[2] for line in lines]
    
    return times, light_values, errors

main()

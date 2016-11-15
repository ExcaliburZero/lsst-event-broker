import MySQLdb

import observation


class MySqlDatabaseHandler(object):

    host = None
    database_name = None
    username = None
    password = None
    classifier_box = None

    def __init__(self, host, database_name, username, password):
        self.host = host
        self.database_name = database_name
        self.username = username
        self.password = password

    def set_classifier_box(self, classifier_box):
        self.classifier_box = classifier_box

    def run(self, obs):
        # Put observation into database
        self.input_observation(obs)

        # Pull out related observations
        object_id = obs.object_id
        all_observations = self.pull_observations(object_id)

        # Process observations
        if self.classifier_box is not None:
            results = self.classifier_box.run(all_observations)

            # Put results in database
            self.push_results(results)

    def connect(self):
        connection = MySQLdb.connect(
            host=self.host,
            user=self.username,
            passwd=self.password,
            db=self.database_name
        )
        return connection

    def input_observation(self, obs):
        connection = self.connect()
        cursor = connection.cursor()

        # Take apart and insert Observation
        observation_tuple = obs.to_tuple()
        cursor.execute("INSERT INTO Observation VALUES (%s, %s, %s, %s)", observation_tuple)

        connection.commit()
        connection.close()

    def pull_observations(self, object_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Observation WHERE id = %s", (object_id,))
        results = cursor.fetchall()

        observations = parse_observations(results)

        connection.close()
        return observations

    def push_results(self, results):
        connection = self.connect()
        cursor = connection.cursor()

        # Insert results
        for result_set in results:
            for result in result_set:
                cursor.execute("INSERT INTO Result VALUES (%s, %s, %s, %s)", result)

        connection.commit()
        connection.close()


def parse_observations(observation_data):
    observations = []
    for row in observation_data:
        object_id = row[0]
        time = row[1]
        light = row[2]
        error = row[3]
        o = observation.Observation(object_id, time, light, error)
        observations.append(o)

    return observations

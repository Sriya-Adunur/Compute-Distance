# Defines a type representing one-way roads connecting cities.
# CSC 101, Project 5
# Given code, Winter '23

class Road:
    """ A road connecting two cities """

    def __init__(self, start, end, distance):
        """
        Create a new Road and add this Road to its Cities.
        TODO: Complete this method.

        :param start: The City at the start of this Road
        :param end: The City at the end of this Road
        :param distance: The length of this Road
        """
        self.start = start
        self.end = end
        self.distance = distance

        self.start.roads[self.end.name] = self 

    def __eq__(self, other):
        """
        Determine whether or not this Road is equal to another.
        TODO: Complete this method.

        :param other: Another value
        :return: Whether or not the other value is a Road with the same
                 starting City, ending City, and distance
        """
        if type(other) == Road and self.start == other.start and self.end == other.end and self.distance == other.distance:
            return True
        else:
            return False

    def __repr__(self):
        """
        Convert this Road into a string.
        TODO: Complete this method.

        :return: The starting and ending City names and distance of this Road,
                 as a string of the form "START to END (DISTANCE)"
        """
        return str(self.start.name) + " to " + str(self.end.name) + " (" + str(self.distance) + ")"

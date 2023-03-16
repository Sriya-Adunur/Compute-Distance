# Defines a type representing cities connected by roads.
# CSC 101, Project 5
# Given code, Winter '23

class City:
    """ A city connected by roads """

    def __init__(self, name):
        """
        Create a new City with no Roads.
        TODO: Complete this method. 

        :param name: The name of this City
        """
        self.name = name
        self.roads = {}

    def __eq__(self, other):
        """
        Determine whether or not this City is equal to another.
        TODO: Complete this method.

        :param other: Another value
        :return: Whether or not the other value is a City with the same name;
                 you may assume Cities with the same name have the same Roads
        """
        if self.name == other.name:
           return True
        else:
           return False

    def __repr__(self):
        """
        Convert this City into a string.
        TODO: Complete this method.

        :return: The name of this City
        """
        return str(self.name)

"""
A module that defines the Ship class.
"""
from abc import ABC, abstractmethod


class Ship(ABC):  # pylint: disable=too-many-instance-attributes
    """A class to represent a ship."""

    def __init__(self, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0,
                 id=10.4):
        # pylint: disable=invalid-name
        # pylint: disable=too-many-arguments
        # pylint: disable=redefined-builtin
        """
        Constructs all the necessary attributes for the ship object.

        Args:
        name (str): The name of the ship.
        captain (str): The name of the ship's captain.
        current_port (str): The current port where the ship is located.
        max_speed (float): The maximum speed of the ship.
        max_capacity (float): The maximum load capacity of the ship.
        current_load (float): The current load of the ship.
        current_speed (float): The current speed of the ship.
        id (float): The ID of the ship.
        """
        self.id = id  # pylint: disable=invalid-name
        self.name = name
        self.captain = captain
        self.current_port = current_port
        self.max_speed = max_speed
        self.max_capacity = max_capacity
        self.current_load = current_load
        self.current_speed = current_speed

    def __str__(self):
        """
            Returns a string representation of the ship object for convenient display.

            Returns:
                str: A string representation of the ship.
            """
        return (f"Ship: {self.name}, {self.captain}, {self.current_port}, {self.max_speed}, "
                f"{self.max_capacity}, {self.current_load}, {self.current_speed}, {self.id}"
                )

    def dock(self):
        """
           Prints the current port where the ship is located.
           """
        print("Current port of", self.name, ":", self.current_port)

    def set_speed(self, speed):
        """
            Sets the current speed of the ship if it is within the maximum speed.

            Args:
                speed (float): The desired speed for the ship.
            """
        if speed <= self.max_speed:
            self.current_speed = speed
            print("Current speed of", self.name, ":", self.current_speed)
        else:
            print("Reduce ship speed!")
        return self.current_speed

    def load(self, weight):
        """
        Loads the specified weight onto the ship if it does not exceed the maximum load capacity.

        Args:
            weight (float): The weight of the cargo to be loaded.
        """
        if self.current_load + weight <= self.max_capacity:
            self.current_load += weight
            print("You can add cargo.")
        else:
            print("Unable to load, reach maximum load capacity.")

    def unload(self, weight):
        """
            Unloads the specified weight from the ship if it does not result in a negative load.

            Args:
                weight (float): The weight of the cargo to be unloaded.
            """
        if self.current_load - weight >= 0:
            self.current_load -= weight
            print("You can delete the load.")
        else:
            print("It is not possible to unload, there is no cargo.")

    @abstractmethod
    def get_total_people_count(self):
        """
            Abstract method to be implemented in subclasses.
            Returns the total number of people on the ship.
            """

    @abstractmethod
    def calculate_load_time(self):
        """
        Abstract method to be implemented in subclasses.
        Calculates the time required to load the cargo on the ship.
        """

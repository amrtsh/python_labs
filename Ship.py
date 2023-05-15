class Ship:
    __instance = None

    def __init__(self, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0, id=10.4):
        self.id = id
        self.name = name
        self.captain = captain
        self.current_port = current_port
        self.max_speed = max_speed
        self.max_capacity = max_capacity
        self.current_load = current_load
        self.current_speed = current_speed

    """Returns a string representation of the object for convenient display"""

    def __str__(self):
        return (f"Film: {self.name}, {self.captain}, {self.current_port}, {self.max_speed}, "
                f"{self.max_capacity}, {self.current_load}, {self.current_speed}, {self.id}"
                )

    """Return current port"""

    def dock(self):
        print("Current port:", self.current_port)

    """Return current speed"""

    def set_speed(self, speed):
        if speed <= self.max_speed:
            self.current_speed = speed
            print("Current speed", self.current_speed)
        else:
            print("Reduce ship speed!")

    """Return whether it is possible to load more cargo"""

    def load(self, weight):
        if self.current_load + weight <= self.max_capacity:
            self.current_load += weight
            print("You can add cargo.")
        else:
            print("Unable to load, reach maximum load capacity.")

    """Return whether the ship can be unloaded"""

    def unload(self, weight):
        if self.current_load - weight >= 0:
            self.current_load -= weight
            print("You can delete the load.")
        else:
            print("It is not possible to unload, there is no cargo.")

    """Return instance"""

    @staticmethod
    def get_instance():
        if not Ship.__instance:
            Ship.__instance = Ship()
        return Ship.__instance

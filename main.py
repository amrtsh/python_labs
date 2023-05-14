class Ship:
    instance = None

    def __init__(self, name=None, captain=None, current_port=None, max_speed=0.0,
                 max_capacity=0.0, current_load=0.0, current_speed=0.0, id=10.4):
        self.__id = id
        self.__name = name
        self.__captain = captain
        self.__current_port = current_port
        self.__max_speed = max_speed
        self.__max_capacity = max_capacity
        self.__current_load = current_load
        self.__current_speed = current_speed

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def captain(self):
        return self.__captain

    @property
    def current_port(self):
        return self.__current_port

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def max_capacity(self):
        return self.__max_capacity

    @property
    def current_load(self):
        return self.__current_load

    @property
    def current_speed(self):
        return self.__current_speed

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @captain.setter
    def captain(self, captain):
        self.__captain = captain

    @current_port.setter
    def current_port(self, current_port):
        self.__current_port = current_port

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        self.__max_capacity = max_capacity

    @current_load.setter
    def current_load(self, current_load):
        self.__current_load = current_load

    @current_speed.setter
    def current_speed(self, current_speed):
        self.__current_speed = current_speed

    def __str__(self):
        return f"Film({self.__name}, {self.__captain}, {self.__current_port}, {self.__max_speed}," \
               f"{self.__max_capacity}, {self.__current_load}, {self.__current_speed}, {self.__id})"

    def dock(self):
        print("Current port:", self.__current_port)

    def set_speed(self, speed):
        if speed <= self.__max_speed:
            self.__current_speed = speed
            print("Current speed", self.__current_speed)
        else:
            print("Reduce ship speed!")

    def load(self, weight):
        if self.__current_load + weight <= self.__max_capacity:
            self.__current_load += weight
            print("You can add cargo.")
        else:
            print("Unable to load, reach maximum load capacity.")

    def unload(self, weight):
        if self.__current_load - weight >= 0:
            self.__current_load -= weight
            print("You can delete the load.")
        else:
            print("It is not possible to unload, there is no cargo.")

    @staticmethod
    def get_instance():
        if not Ship.instance:
            Ship.instance = Ship()
        return Ship.instance


ships = [Ship("Talisman", "Carl Brick", "Mariupol", 46.3, 10000, 325, 40, 8),
         Ship("Serenity", "William Kidd", "Shenzhen", 26.3, 10000, 456, 43),
         Ship.get_instance()]

for ship in ships:
    ship.dock()
    ship.set_speed(40)
    ship.load(9000)
    ship.unload(10000)
    ship.get_instance()

    print(ship)

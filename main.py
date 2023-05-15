from Ship import Ship

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

arr = list(range(50, 101))
print(arr[::2])

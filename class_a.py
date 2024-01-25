# -*- config: utf-8 -*-

class Building:
    total = 0

    def __init__(self):
        Building.total += 1


list_total = []
while Building.total < 40:
    building = Building()
    list_total.append(Building.total)

print(list_total)
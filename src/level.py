import cube
import utils.settings as s

cubes = []
score = 0
lines_cleared = 0


def add(c: cube.Cube):
    if c not in cubes:
        cubes.append(c)


def remove(c: cube.Cube):
    cubes.remove(c)


def draw():
    for i in cubes:
        i.draw()


def check_line():
    places = {}
    for i in cubes:
        if i.tag == "block":
            if i.position[1] in places.keys():
                places[i.position[1]] += 1
            else:
                places[i.position[1]] = 1
    to_pop = []
    for key, value in places.items():
        if value == 13:
            to_pop.append(key)
    return to_pop


def clear_lines():
    to_pop = check_line()
    global score
    global lines_cleared
    score += len(to_pop)**2
    lines_cleared += len(to_pop)
    change_speed(lines_cleared)
    to_remove = []
    if not to_pop:
        return
    for i in cubes:
        if i.tag == "block" and i.position[1] in to_pop:
            to_remove.append(i)
    for i in to_remove:
        remove(i)
    for i in sorted(to_pop):
        for j in cubes:
            if j.tag == "block" and j.position[1] < i:
                x = j.position[0]
                y = j.position[1]
                j.position = (x, y+1)


def change_speed(lines):
    if lines_cleared > 80:
        s.speed = 10
        return
    if lines_cleared > 70:
        s.speed = 15
        return
    if lines_cleared > 60:
        s.speed = 20
        return
    if lines_cleared > 50:
        s.speed = 25
        return
    if lines_cleared > 40:
        s.speed = 30
        return
    if lines_cleared > 30:
        s.speed = 35
        return
    if lines_cleared > 20:
        s.speed = 40
        return
    if lines_cleared > 10:
        s.speed = 45
        return

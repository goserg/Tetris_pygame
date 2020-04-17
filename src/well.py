from cube import Cube
import stats.score

cubes = []
lines_cleared = 0


def add(c: Cube) -> None:
    if c not in cubes:
        cubes.append(c)


def remove(c: Cube) -> None:
    cubes.remove(c)


def draw() -> None:
    for i in cubes:
        i.draw()


def check_line() -> list:
    places = {}
    for i in cubes:
        if i.tag == "Block":
            if i.position[1] in places.keys():
                places[i.position[1]] += 1
            else:
                places[i.position[1]] = 1
    to_pop = []
    for key, value in places.items():
        if value == 10:
            to_pop.append(key)
    return to_pop


def clear_lines() -> None:
    to_pop = check_line()
    global lines_cleared
    stats.score.add(len(to_pop))
    to_remove = []
    if not to_pop:
        return
    for i in cubes:
        if i.tag == "Block" and i.position[1] in to_pop:
            to_remove.append(i)
    for i in to_remove:
        remove(i)
    for i in sorted(to_pop):
        for j in cubes:
            if j.tag == "Block" and j.position[1] < i:
                x = j.position[0]
                y = j.position[1]
                j.position = (x, y + 1)

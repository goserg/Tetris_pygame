from cube import Cube
import stats.score
from typing import Dict, List

cubes: List[Cube] = []
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
    places: Dict[float, float] = {}
    for i in cubes:
        if i.tag == "Block":
            if i.position.y in places.keys():
                places[i.position.y] += 1
            else:
                places[i.position.y] = 1
    to_pop: List[float] = []
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
        if i.tag == "Block" and i.position.y in to_pop:
            to_remove.append(i)
    for i in to_remove:
        remove(i)
    for i in sorted(to_pop):
        for j in cubes:
            if j.tag == "Block" and j.position.y < i:
                j.position.y += 1

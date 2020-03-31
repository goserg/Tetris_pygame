import cube
cubes = []
score = 0


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
    score += len(to_pop)**2
    to_remove = []
    if not to_pop:
        return
    print(score)
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

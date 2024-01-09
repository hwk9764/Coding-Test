row, colum = map(int, input().split())
x, y, d = map(int, input().split())
state = True
global world
world = []
direction = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}
result = 1

for _ in range(row):
    data = list(map(int, input().split()))
    world.append(data)

def rotate(x, y, d):
    state = True
    for _ in range(4):
        d = d-1 if d != 0 else 3
        dx, dy = direction[d]
        temp_x = x+dx
        temp_y = y+dy
        if world[temp_x][temp_y] == 0:
            x = temp_x
            y = temp_y
            world[x][y] = 2
            return x, y, d, state

    state = False
    return x, y, d, state

while(True):
    world[x][y] = 2
    x, y, d, state = rotate(x, y, d)

    if state:
        result += 1
        continue

    else:
        dx, dy = direction[d]
        x -= dx
        y -= dy
        if world[x][y] == 1:
            break
print('result : ', result)
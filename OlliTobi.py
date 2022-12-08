import random
matrix = [[0 for x in range(10)] for y in range(10)]
ships = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

def place_ships(matrix, ships):    
    for ship in ships:
        print(ship)
        x = int(input("x: "))
        y = int(input("y: "))
        direction = input("direction: ")
        if direction == "h":
            for i in range(ships[ship]):
                matrix[x][y+i] = 1
        else:
            for i in range(ships[ship]):
                matrix[x+i][y] = 1
        print_matrix(matrix)
    print_matrix(matrix)

def check_out_of_bounds(x, y, dir, ship):
    if dir == "h":
        return y + ships[ship] <= 9
    else:
        return x + ships[ship] <= 9
def has_collision(x, y, dir, ship, matrix):
    print(dir)
    if dir == "h":
        for i in range(ships[ship]):
            print(i)
            if (y+i >= 9 or matrix[x][y+i] == 1 or matrix[x+1][y+i] == 1 or matrix[x-1][y+i] == 1 or matrix[x][y+i+1] == 1 or matrix[x][y+i-1] == 1):
                return False
        return True
    else:
        for i in range(ships[ship]):
            print(i)
            if (x+i >= 9 or matrix[x+i][y] == 1 or matrix[x+i][y+1] == 1 or matrix[x+i][y-1] == 1 or matrix[x+i+1][y] == 1 or matrix[x+i-1][y] == 1):
                return False
        return True
            
def auto_place_ships(matrix, ships):
    for ship in ships.keys():
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        direction = random.choice(["h", "v"])
        while not check_out_of_bounds(x,y,direction, ship) or not has_collision(x,y,direction, ship, matrix):
                x = random.randint(0, 8)
                y = random.randint(0, 8)
        if direction == "h":
            for i in range(ships[ship]):
                matrix[x][y+i] = 1
        else:
            for i in range(ships[ship]):
                matrix[x+i][y] = 1
    print_matrix(matrix)

t = input("manual or auto? ")
if t == "manual":
    place_ships(matrix, ships)
else:
    auto_place_ships(matrix, ships)
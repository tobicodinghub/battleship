common_ships = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}

import random
class Sea:
    def __init__(self, ships):
        self.matrix = [[0 for x in range(10)] for y in range(10)]
        self.ships = ships

    def print_matrix(self, matrix):
        for row in matrix:
            print(" ".join(str(cell) for cell in row))

    def place_ships(self, matrix):    
        for ship in self.ships:
            print(ship)
            x = int(input("x: "))
            y = int(input("y: "))
            direction = input("direction: ")
            if direction == "h":
                for i in range(self.ships[ship]):
                    matrix[x][y+i] = 1
            else:
                for i in range(self.ships[ship]):
                    matrix[x+i][y] = 1
        self.print_matrix(matrix)

    def check_out_of_bounds(self, x, y, dir, ship):
        if dir == "h":
            return y + self.ships[ship] <= 9
        else:
            return x + self.ships[ship] <= 9
    def has_collision(self, x, y, dir, ship, matrix):
        if dir == "h":
            for i in range(self.ships[ship]):
                if (y+i >= 9 or matrix[x][y+i] == 1 or matrix[x+1][y+i] == 1 or matrix[x-1][y+i] == 1 or matrix[x][y+i+1] == 1 or matrix[x][y+i-1] == 1):
                    return False
            return True
        else:
            for i in range(self.ships[ship]):
                if (x+i >= 9 or matrix[x+i][y] == 1 or matrix[x+i][y+1] == 1 or matrix[x+i][y-1] == 1 or matrix[x+i+1][y] == 1 or matrix[x+i-1][y] == 1):
                    return False
            return True
                
    def auto_place_ships(self, matrix):
        for ship in self.ships.keys():
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            direction = random.choice(["h", "v"])
            while not self.check_out_of_bounds(x,y,direction, ship) or not self.has_collision(x,y,direction, ship, matrix):
                    x = random.randint(0, 8)
                    y = random.randint(0, 8)
            if direction == "h":
                for i in range(self.ships[ship]):
                    matrix[x][y+i] = 1
            else:
                for i in range(self.ships[ship]):
                    matrix[x+i][y] = 1
        self.print_matrix(matrix)


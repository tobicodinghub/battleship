import random
common_ships = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}


class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.winner = None
        self.play_game()

    def play_game(self):
        while not self.winner:
            self.take_turn()
            self.check_winner()
        print("Player {} wins!".format(self.winner))

    def take_turn(self):
        if self.turn == 1:
            self.player1.sea.print_matrix(self.player2.sea.matrix)
            self.player1.take_shot()
            self.turn = 2
        else:
            self.player2.auto_take_shot()
            self.player2.print_matrix()
            self.turn = 1

    def check_winner(self):
        if self.player1.ships_sunk == 5:
            self.winner = 2
        elif self.player2.ships_sunk == 5:
            self.winner = 1


class Player():
    def __init__(self, sea):
        self.sea = sea
        self.sea.place_ships()
        self.ships_sunk = 0

    def take_shot(self):
        x = int(input("x: "))
        y = int(input("y: "))
        if self.sea.matrix[x][y] == 1:
            print("Hit!")
            self.sea.matrix[x][y] = 2
            self.check_sunk(x, y)
        else:
            print("Miss!")
        self.sea.print_matrix()

    def check_sunk(self, x, y):
        if self.sea.matrix[x][y-1] == 1 or self.sea.matrix[x][y+1] == 1 or self.sea.matrix[x-1][y] == 1 or self.sea.matrix[x+1][y] == 1:
            return
        else:
            self.ships_sunk += 1
            print("Ship sunk!")


class Computer():
    def __init__(self, sea):
        self.sea = sea
        self.sea.auto_place_ships()
        self.ships_sunk = 0

    def auto_take_shot(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while self.sea.matrix[x][y] == 2:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        if self.sea.matrix[x][y] == 1:
            print("Hit!")
            self.sea.matrix[x][y] = 2
            self.check_sunk(x, y)
        else:
            print("Miss!")


class Sea:
    def __init__(self, ships):
        self.matrix = [[0 for x in range(10)] for y in range(10)]
        self.ships = ships

    def print_matrix(self, matrix):
        for row in matrix:
            print(" ".join(str(cell) for cell in row))
        print('\n')

    def place_ships(self):
        for ship in self.ships:
            print(ship)
            x = int(input("x: "))
            y = int(input("y: "))
            direction = input("direction: ")
            if direction == "h":
                for i in range(self.ships[ship]):
                    self.matrix[x][y+i] = 1
            else:
                for i in range(self.ships[ship]):
                    self.matrix[x+i][y] = 1
            self.print_matrix(self.matrix)
        self.print_matrix(self.matrix)

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

    def auto_place_ships(self):
        for ship in self.ships.keys():
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            direction = random.choice(["h", "v"])
            while not self.check_out_of_bounds(x, y, direction, ship) or not self.has_collision(x, y, direction, ship, self.matrix):
                x = random.randint(0, 8)
                y = random.randint(0, 8)
            if direction == "h":
                for i in range(self.ships[ship]):
                    self.matrix[x][y+i] = 1
            else:
                for i in range(self.ships[ship]):
                    self.matrix[x+i][y] = 1
        self.print_matrix(self.matrix)


game1 = Game(Player(Sea(common_ships)), Computer(Sea(common_ships)))

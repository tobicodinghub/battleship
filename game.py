import random
from tkinter import *
import tkinter as tk
common_ships = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}


class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Battleship")
        self.window.geometry("1920x1080")
        self.bgimg = tk.PhotoImage(file="battleship.png")
        self.limg = Label(self.window, image=self.bgimg)
        self.limg.pack()

    def initialize_matrix(self, matrix, xc, yc):
        btns_frame = Frame(self.window)
        btns_frame.pack()
        water = tk.PhotoImage(file="crosscircle.png")
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                i = matrix[row][col]
                b = Button(btns_frame, text=str(i), height=3, width=5, padx="5px",
                           pady="5px", activeforeground="blue", activebackground="red")
                b.grid(row=row + 1, column=col)
        btns_frame.place(x=xc, y=yc)

    def place_ships(self, matrix, ships):
        i = 0
        x = []
        y = []
        z = []
        for ship in ships:
            Label(self.window, text=ship, font=("Arial", 40)).place(x=1200, y=150 + 150*i)
            x.append(Entry(self.window).place(x=1200, y=250 + 150*i))
            y.append(Entry(self.window).place(x=1350, y=250 + 150*i))
            z.append(Entry(self.window).place(x=1500, y=250 + 150*i))
            i += 1
        
        for ship in ships:
            i = 0
            a = x[i].get()
            b = y[i].get()
            dir = z[i].get()
            if dir == "h":
                    for i in range(self.ships[ship]):
                        matrix[a][b+i] = 1
            else:
                for i in range(self.ships[ship]):
                    self.matrix[a+i][b] = 1    
            i += 1

class Game():
    def __init__(self, window, player1, computer):
        self.window = window
        self.player1 = player1
        self.computer = computer
        self.window.initialize_matrix(self.player1.sea.matrix, 170, 150)
        self.window.place_ships(self.player1.sea.matrix,
                                self.player1.sea.ships)
        #self.window.initialize_matrix(self.computer.sea.matrix, 1175, 150)

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
            print("Hier ist deine Matrix")
            self.player1.sea.print_matrix()
            print("Hier ist die Computermatrix")
            self.player1.print_visible_matrix()
            self.player1.take_shot(self.computer)
            self.turn = 2
        else:
            self.computer.auto_take_shot(self.player1)
            self.turn = 1

    def check_winner(self):
        if self.player1.tiles_sunk == 17:
            self.winner = 2
        elif self.computer.tiles_sunk == 17:
            self.winner = 1


class Player():
    def __init__(self, sea):
        self.sea = sea
        self.tiles_sunk = 0
        self.visible_matrix = [[0 for x in range(10)] for y in range(10)]

    def print_visible_matrix(self):
        for row in self.visible_matrix:
            print(" ".join(str(cell) for cell in row))
        print('\n')

    def take_shot(self, computer):
        x = int(input("x: "))-1
        y = int(input("y: "))-1
        if computer.sea.matrix[x][y] == 1:
            print("Hit!")
            computer.sea.matrix[x][y] = 2
            self.visible_matrix[x][y] = "H"
            self.tiles_sunk += 1
        else:
            print("Miss!")
            computer.sea.matrix[x][y] = 3
            self.visible_matrix[x][y] = "W"


class Computer():
    def __init__(self, sea):
        self.sea = sea
        self.sea.auto_place_ships()
        self.tiles_sunk = 0

    def auto_take_shot(self, player):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while player.sea.matrix[x][y] == (2 or 3):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        if player.sea.matrix[x][y] == 1:
            print("Computer Hit!")
            player.sea.matrix[x][y] = 2
            self.tiles_sunk += 1
        else:
            print("Computer Miss!")
            player.sea.matrix[x][y] = 3


class Sea:
    def __init__(self, ships):
        self.matrix = [[0 for x in range(10)] for y in range(10)]
        self.ships = ships

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(str(cell) for cell in row))
        print('\n')

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


game1 = Game(Window(), Player(Sea(common_ships)), Computer(Sea(common_ships)))

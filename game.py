import random
from tkinter import *
from functools import partial
import tkinter as tk
from PIL import ImageTk, Image
common_ships = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
number_to_path = {
    0: "sea-waves.png",
    1: "rec.png",
    2: "crosscircle.png",
    3: "minus.png",
    "H": "cross-sig.png",
    "W": "minus.png"
}

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Battleship")
        self.geometry("1920x1080")
        self.bgimg = tk.PhotoImage(file="battleship.png")
        self.limg = Label(self, image=self.bgimg)
        self.limg.pack()

    def initialize_matrix(self, matrix, xc, yc):
        btns_frame = Frame(self)
        btns_frame.pack()
        

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                i = matrix[row][col]
                img = Image.open(str(number_to_path[i]))
                img = img.resize((64, 64), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(img)
                label = Label(btns_frame, image=test)
                label.image = test
                #b = Button(btns_frame, text = i, image = test, height=3, width=5, padx="5px",
                #pady="5px", activeforeground="blue", compound="center")
                label.grid(row=row + 1, column=col)
                

        btns_frame.place(x=xc, y=yc)

    def place_ships(self, matrix, ships):
        a = []
        b = []
        c = []
        i = 0
        x1 = tk.StringVar(self)
        x2 = tk.StringVar(self)
        x3 = tk.StringVar(self)
        x4 = tk.StringVar(self)
        x5 = tk.StringVar(self)
        y1 = tk.StringVar(self)
        y2 = tk.StringVar(self)
        y3 = tk.StringVar(self)
        y4 = tk.StringVar(self)
        y5 = tk.StringVar(self)
        dir1 = tk.StringVar(self)
        dir2 = tk.StringVar(self)
        dir3 = tk.StringVar(self)
        dir4 = tk.StringVar(self)
        dir5 = tk.StringVar(self)
        var1 = tk.IntVar()
        for ship in ships:
            Label(self, text=ship, font=("Arial", 40)).place(
                x=1200, y=150 + 150*i)
            i += 1
        e1 = Entry(self, textvariable=x1).place(x=1200, y=250)
        e2 = Entry(self, textvariable=y1).place(x=1350, y=250)
        e3 = Entry(self, textvariable=dir1).place(x=1500, y=250)
        button1 = Button(self, text="Place Ship", command=partial(
            self.get_ship, x1, y1, dir1, a, b, c)).place(x=1650, y=250)
        e4 = Entry(self, textvariable=x2).place(x=1200, y=400)
        e5 = Entry(self, textvariable=y2).place(x=1350, y=400)
        e6 = Entry(self, textvariable=dir2).place(x=1500, y=400)
        button2 = Button(self, text="Place Ship", command=partial(
            self.get_ship, x2, y2, dir2, a, b, c)).place(x=1650, y=400)
        e7 = Entry(self, textvariable=x3).place(x=1200, y=550)
        e8 = Entry(self, textvariable=y3).place(x=1350, y=550)
        e9 = Entry(self, textvariable=dir3).place(x=1500, y=550)
        button3 = Button(self, text="Place Ship", command=partial(
            self.get_ship, x3, y3, dir3, a, b, c)).place(x=1650, y=550)
        e10 = Entry(self, textvariable=x4).place(x=1200, y=700)
        e11 = Entry(self, textvariable=y4).place(x=1350, y=700)
        e12 = Entry(self, textvariable=dir4).place(x=1500, y=700)
        button4 = Button(self, text="Place Ship", command=partial(
            self.get_ship, x4, y4, dir4, a, b, c)).place(x=1650, y=700)
        e13 = Entry(self, textvariable=x5).place(x=1200, y=850)
        e14 = Entry(self, textvariable=y5).place(x=1350, y=850)
        e15 = Entry(self, textvariable=dir5).place(x=1500, y=850)
        button5 = Button(self, text="Place Ship", command=partial(
            self.get_last_ship, x5, y5, dir5, a, b, c, matrix, ships, var1))
        button5.place(x=1650, y=850)
        button5.wait_variable(var1)

    def destroy_frame(self):
        for children in self.winfo_children():
            if (children.winfo_class() == "Button" or children.winfo_class() == "Entry" or children.winfo_class() == "Label") and children.winfo_geometry() != "1920x1080+0+0":
                children.destroy()
                self.limg.pack()

    def get_ship(self, x, y, dir, a, b, c):
        a.append(x.get())
        b.append(y.get())
        c.append(dir.get())

    def get_last_ship(self, x, y, dir, a, b, c, matrix, ships, var):
        a.append(x.get())
        b.append(y.get())
        c.append(dir.get())
        self.destroy_frame()
        self.place_ship(matrix, ships, a, b, c)
        self.initialize_matrix(matrix, 150, 150)
        var.set(1)

    def place_ship(self, matrix, ships, a, b, c):
        for ship in ships:
            if ship == "carrier":
                x = a[0]
                y = b[0]
                dir = c[0]
            elif ship == "battleship":
                x = a[1]
                y = b[1]
                dir = c[1]
            elif ship == "cruiser":
                x = a[2]
                y = b[2]
                dir = c[2]
            elif ship == "submarine":
                x = a[3]
                y = b[3]
                dir = c[3]
            elif ship == "destroyer":
                x = a[4]
                y = b[4]
                dir = c[4]
            if dir == "h":
                for i in range(ships[ship]):
                    matrix[int(x)][int(y) + i] = 1
            else:
                for i in range(ships[ship]):
                    matrix[int(x) + i][int(y)] = 1

    def return_coords(self, player, computer):
        var2 = tk.IntVar()
        xcoord = StringVar()
        ycoord = StringVar()
        entry1 = Entry(self, textvariable=xcoord).place(x=820, y=800)
        entry2 = Entry(self, textvariable=ycoord).place(x=950, y=800)
        button6 = tk.Button(self, text="Submit coords", command=partial(
            self.return_coords2, xcoord, ycoord, player, computer, var2))
        button6.place(x=900, y=850)
        button6.wait_variable(var2)

    def return_coords2(self, xcoord, ycoord, player, computer, var):
        global x
        x = xcoord.get()
        global y
        y = ycoord.get()
        var.set(1)
        player.take_shot(computer, x, y)


class Game():
    def __init__(self, player1, computer):
        self.window = Window()
        self.player1 = player1
        self.computer = computer
        self.window.initialize_matrix(self.player1.sea.matrix, 150, 150)
        self.turn = 1
        self.winner = None
        self.play_game()
        self.window.mainloop()

    def play_game(self):
        self.window.place_ships(self.player1.sea.matrix,
                                self.player1.sea.ships)
        self.window.initialize_matrix(self.player1.visible_matrix, 1200, 150)
        while not self.winner:
            self.take_turn()
            self.window.initialize_matrix(
                self.player1.visible_matrix, 1200, 150)
            self.window.initialize_matrix(self.player1.sea.matrix, 150, 150)
            self.check_winner()

    def take_turn(self):
        if self.turn == 1:
            self.window.return_coords(self.player1, self.computer)
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

    def take_shot(self, computer, x, y):
        if computer.sea.matrix[int(x)][int(y)] == 1:
            print("Hit!")
            computer.sea.matrix[int(x)][int(y)] = 2
            self.visible_matrix[int(x)][int(y)] = "H"
            self.tiles_sunk += 1
        else:
            print("Miss!")
            computer.sea.matrix[int(x)][int(y)] = 3
            self.visible_matrix[int(x)][int(y)] = "W"


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
            print("1")
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            direction = random.choice(["h", "v"])
            while not self.check_out_of_bounds(x, y, direction, ship) or not self.has_collision(x, y, direction, ship, self.matrix):
                print(2)
                x = random.randint(0, 8)
                y = random.randint(0, 8)
            if direction == "h":
                for i in range(self.ships[ship]):
                    self.matrix[x][y+i] = 1
            else:
                for i in range(self.ships[ship]):
                    self.matrix[x+i][y] = 1


game1 = Game(Player(Sea(common_ships)), Computer(Sea(common_ships)))

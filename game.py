import random
from functools import partial
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import winsound
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
    "H": "cross-sign.png",
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
            l = Label(btns_frame, text=str(row + 1), font=('Futura', 12))
            l.grid(row=0, column=row+1)
            for col in range(len(matrix[row])):
                if row == 0:
                    l = Label(btns_frame, text=str(
                        col + 1), font=('Futura', 12))
                    l.grid(row=col+1, column=0)
                i = matrix[row][col]
                img = Image.open(str(number_to_path[i]))
                img = img.resize((64, 64))
                test = ImageTk.PhotoImage(img)
                label = Label(btns_frame, image=test)
                label.image = test
                label.grid(row=row + 1, column=col+1)

        btns_frame.place(x=xc, y=yc)

    def place_ships(self, player):
        matrix = player.sea.matrix
        ships = player.sea.ships
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
        i = 0
        l = ["carrier.png", "battleship2.png",
             "cruiser.png", "submarine.png", "destroyer.png"]
        for shippies in l:
            img = Image.open(shippies)
            img = img.resize((700, 33))
            test = ImageTk.PhotoImage(img)
            label = Label(self, image=test)
            label.image = test
            label.place(x=1000, y=200 + 150*i)
            i += 1
        img = Image.open("button.png")
        test = ImageTk.PhotoImage(img)
        e1 = Entry(self, textvariable=x1, font=(
            'Futura', 12)).place(x=1000, y=250)
        e2 = Entry(self, textvariable=y1, font=(
            'Futura', 12)).place(x=1200, y=250)
        e3 = Entry(self, textvariable=dir1, font=(
            'Futura', 12)).place(x=1400, y=250)
        button1 = Button(self, text="Place Ship", image=test, command=partial(
            self.get_ship, x1, y1, dir1, a, b, c, matrix, "carrier", ships, player)).place(x=1600, y=250)
        e4 = Entry(self, textvariable=x2, font=(
            'Futura', 12)).place(x=1000, y=400)
        e5 = Entry(self, textvariable=y2, font=(
            'Futura', 12)).place(x=1200, y=400)
        e6 = Entry(self, textvariable=dir2, font=(
            'Futura', 12)).place(x=1400, y=400)
        button2 = Button(self, text="Place Ship", image=test, command=partial(
            self.get_ship, x2, y2, dir2, a, b, c, matrix, "battleship", ships, player)).place(x=1600, y=400)
        e7 = Entry(self, textvariable=x3, font=(
            'Futura', 12)).place(x=1000, y=550)
        e8 = Entry(self, textvariable=y3, font=(
            'Futura', 12)).place(x=1200, y=550)
        e9 = Entry(self, textvariable=dir3, font=(
            'Futura', 12)).place(x=1400, y=550)
        button3 = Button(self, text="Place Ship", image=test, command=partial(
            self.get_ship, x3, y3, dir3, a, b, c, matrix, "cruiser", ships, player)).place(x=1600, y=550)
        e10 = Entry(self, textvariable=x4, font=(
            'Futura', 12)).place(x=1000, y=700)
        e11 = Entry(self, textvariable=y4, font=(
            'Futura', 12)).place(x=1200, y=700)
        e12 = Entry(self, textvariable=dir4, font=(
            'Futura', 12)).place(x=1400, y=700)
        button4 = Button(self, text="Place Ship", image=test, command=partial(
            self.get_ship, x4, y4, dir4, a, b, c, matrix, "submarine", ships, player)).place(x=1600, y=700)
        e13 = Entry(self, textvariable=x5, font=(
            'Futura', 12)).place(x=1000, y=850)
        e14 = Entry(self, textvariable=y5, font=(
            'Futura', 12)).place(x=1200, y=850)
        e15 = Entry(self, textvariable=dir5, font=(
            'Futura', 12)).place(x=1400, y=850)
        button5 = Button(self, text="Place Ship", image=test, command=partial(
            self.get_last_ship, x5, y5, dir5, a, b, c, matrix, "destroyer", var1, ships, player))
        button5.place(x=1600, y=850)
        button5.wait_variable(var1)

    def destroy_frame(self):
        for children in self.winfo_children():
            if (children.winfo_class() == "Button" or children.winfo_class() == "Entry" or children.winfo_class() == "Label") and children.winfo_geometry() != "1920x1080+0+0":
                children.destroy()
                self.limg.pack()

    def get_ship(self, x, y, dir, a, b, c, matrix, ship, ships, player):
        if not player.sea.check_out_of_bounds(int(x.get())-1, int(y.get())-1, dir.get(), ship) or not player.sea.has_collision(int(x.get())-1, int(y.get())-1, dir.get(), ship, matrix):
            tk.messagebox.showerror("Error", "Invalid ship placement")
            return
        a.append(x.get())
        b.append(y.get())
        c.append(dir.get())
        self.place_ship(matrix, ship, a, b, c, ships)
        self.initialize_matrix(matrix, 150, 200)

    def get_last_ship(self, x, y, dir, a, b, c, matrix, ship, var, ships, player):
        if not player.sea.check_out_of_bounds(int(x.get())-1, int(y.get())-1, dir.get(), ship) or not player.sea.has_collision(int(x.get())-1, int(y.get())-1, dir.get(), ship, matrix):
            tk.messagebox.showerror(
                title="Error", message="Invalid ship placement")
            return
        a.append(x.get())
        b.append(y.get())
        c.append(dir.get())
        self.destroy_frame()
        self.place_ship(matrix, ship, a, b, c, ships)
        self.initialize_matrix(matrix, 150, 200)
        var.set(1)

    def place_ship(self, matrix, ship, a, b, c, ships):
        if ship == "carrier":
            x = a[0]
            y = b[0]
            dir = c[0]
        if ship == "battleship":
            x = a[1]
            y = b[1]
            dir = c[1]
        if ship == "cruiser":
            x = a[2]
            y = b[2]
            dir = c[2]
        if ship == "submarine":
            x = a[3]
            y = b[3]
            dir = c[3]
        if ship == "destroyer":
            x = a[4]
            y = b[4]
            dir = c[4]
        if dir == "h":
            for i in range(ships[ship]):
                matrix[int(x)-1][int(y) + i - 1] = 1
        else:
            for i in range(ships[ship]):
                matrix[int(x)-1 + i][int(y)-1] = 1

    def return_coords(self, player, computer):
        var2 = tk.IntVar()
        xcoord = StringVar()
        xcoord.set("1")
        ycoord = StringVar()
        ycoord.set("1")
        OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        OptionMenu(self, xcoord, *OPTIONS).place(x=900, y=500)
        OptionMenu(self, ycoord, *OPTIONS).place(x=900, y=540)
        img = Image.open("coordsbutton.png")
        img = img.resize((120, 70), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)
        button6 = tk.Button(self, image=test, command=partial(
            self.return_coords2, xcoord, ycoord, player, computer, var2))
        button6.place(x=860, y=580)
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
        self.window.initialize_matrix(self.player1.sea.matrix, 150, 200)
        self.turn = 1
        self.winner = None
        self.play_game()
        self.window.mainloop()

    def play_game(self):
        self.window.place_ships(self.player1)
        self.window.initialize_matrix(self.player1.visible_matrix, 1000, 200)
        while not self.winner:
            self.take_turn()
            self.window.initialize_matrix(
                self.player1.visible_matrix, 1000, 200)
            self.window.initialize_matrix(self.player1.sea.matrix, 150, 200)
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
            winsound.PlaySound('win.wav', winsound.SND_FILENAME)
        elif self.computer.tiles_sunk == 17:
            self.winner = 1
            winsound.PlaySound('win.wav', winsound.SND_FILENAME)


class Player():
    def __init__(self, sea):
        self.sea = sea
        self.tiles_sunk = 0
        self.visible_matrix = [[0 for x in range(10)] for y in range(10)]

    def take_shot(self, computer, x, y):
        if computer.sea.matrix[int(x)-1][int(y)-1] == 1:
            winsound.PlaySound('hit.wav', winsound.SND_FILENAME)
            computer.sea.matrix[int(x)-1][int(y)-1] = 2
            self.visible_matrix[int(x)-1][int(y)-1] = "H"
            self.tiles_sunk += 1
        else:
            winsound.PlaySound('miss.wav', winsound.SND_FILENAME)
            computer.sea.matrix[int(x)-1][int(y)-1] = 3
            self.visible_matrix[int(x)-1][int(y)-1] = "W"


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
            winsound.PlaySound('hit.wav', winsound.SND_FILENAME)
            player.sea.matrix[x][y] = 2
            self.tiles_sunk += 1
        else:
            winsound.PlaySound('miss.wav', winsound.SND_FILENAME)
            player.sea.matrix[x][y] = 3


class Sea:
    def __init__(self, ships):
        self.matrix = [[0 for x in range(10)] for y in range(10)]
        self.ships = ships

    def check_out_of_bounds(self, x, y, dir, ship):
        if dir == "h":
            return y + self.ships[ship] <= 10
        else:
            return x + self.ships[ship] <= 10

    def has_collision(self, x, y, dir, ship, matrix):
        print(x)
        print(y)
        print(type(x))
        print(type(y))
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


game1 = Game(Player(Sea(common_ships)), Computer(Sea(common_ships)))

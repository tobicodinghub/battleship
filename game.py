import random #import all the modules needed
from functools import partial
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import winsound
common_ships = { #dictionary of ships and their sizes
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
number_to_path = { #dictionary of the fields numbers and letters and their corresponding images
    0: "sea-waves.png", #will become more clear when reading the shot functions
    1: "rec.png",
    2: "crosscircle.png",
    3: "minus.png",
    "H": "cross-sign.png",
    "W": "minus.png"
}


class Window(tk.Tk): #class for the window
    def __init__(self): #initialization of the window
        super().__init__() #superclass initialization of the window class (tkinter)
        self.title("Battleship") #title of the window
        self.geometry("1920x1080") #size of the window
        self.bgimg = tk.PhotoImage(file="battleship.png") #background image
        self.limg = Label(self, image=self.bgimg) #label for the background image
        self.limg.pack() #pack the label (place it in the window)

    def initialize_matrix(self, matrix, xc, yc): #function to show the matrices, xc and yc are the coordinates of the top left corner of the matrix, update_matrix would be more fitting but I'm too lazy to change it
        btns_frame = Frame(self) #create a frame for the matrix labels
        btns_frame.pack() #pack the frame (place it in the window)

        for row in range(len(matrix)): #iteration trough the rows of the 2D matrix (the matrix is a list of lists) for each row
            l = Label(btns_frame, text=str(row + 1), font=('Futura', 12)) #create a label with the row number so the player knows which row he is placing the ships in
            l.grid(row=0, column=row+1) #place the label in the frame in the right place
            for col in range(len(matrix[row])): #iteration trough the columns of the 2D matrix
                if row == 0: #condition to create the column labels only once per column 
                    l = Label(btns_frame, text=str( #create a label with the column letter so the player knows which column he is placing the ships in
                        col + 1), font=('Futura', 12))
                    l.grid(row=col+1, column=0) #place the label in the frame in the right place
                i = matrix[row][col] #get the value of the field in the matrix
                img = Image.open(str(number_to_path[i])) #each sea has a matrix which consists of numbers for easier handling, the numbers are used to get the corresponding image from the dictionary
                img = img.resize((64, 64)) #resize the image to 64x64 pixels
                test = ImageTk.PhotoImage(img) #convert the image to a tkinter image
                label = Label(btns_frame, image=test) #create a label for the image
                label.image = test #set the image of the label to the image
                label.grid(row=row + 1, column=col+1) #place the image in the grid in the right place

        btns_frame.place(x=xc, y=yc) #place the frame in the window at the coordinates xc and yc

    def place_ships(self, player): #function to place the ships when the player initializes his sea
        matrix = player.sea.matrix #get the matrix of the players sea
        ships = player.sea.ships #get the ships of the players sea
        a = [] #create lists for the x coordinates, y coordinates and directions of the ships
        b = []
        c = []
        x1 = tk.StringVar(self) #create tkinter variables for the x coordinates, y coordinates and directions of the ships to store the values of the entries
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
        var1 = tk.IntVar() #create a tkinter variable to pause until the player places all the ships
        i = 0
        l = ["carrier.png", "battleship2.png",
             "cruiser.png", "submarine.png", "destroyer.png"] #list of the ship button images (buttons were created in figma)
        for shippies in l: #iteration trough the list of ship images
            img = Image.open(shippies) #open the image
            img = img.resize((700, 33))#resize the image to 700x33 pixels
            test = ImageTk.PhotoImage(img)#convert the image to a tkinter image
            label = Label(self, image=test)#create a label for the image
            label.image = test#set the image of the label to the image
            label.place(x=1000, y=200 + 150*i) #place the image in the window in the right place
            i += 1 #increase the counter by 1
        img = Image.open("button.png") #open the image for the place ship button
        test = ImageTk.PhotoImage(img) #convert the image to a tkinter image
        e1 = Entry(self, textvariable=x1, font=( #create entries for the x coordinates, y coordinates and directions of the ships
            'Futura', 12)).place(x=1000, y=250)
        e2 = Entry(self, textvariable=y1, font=(
            'Futura', 12)).place(x=1200, y=250)
        e3 = Entry(self, textvariable=dir1, font=(
            'Futura', 12)).place(x=1400, y=250)
        button1 = Button(self, text="Place Ship", image=test, command=partial(
            self.get_ship, x1, y1, dir1, a, b, c, matrix, "carrier", ships, player)).place(x=1600, y=250) #create a button to place the ship and call the get_ship function when the button is pressed
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
        button5.wait_variable(var1) #wait until the player places all the ships

    def destroy_frame(self): #function to clear the window once the ships are placed
        for children in self.winfo_children(): #iterate through all the widgets in the window
            if (children.winfo_class() == "Button" or children.winfo_class() == "Entry" or children.winfo_class() == "Label") and children.winfo_geometry() != "1920x1080+0+0": #if the widget is a button, entry or label and it is not the background image
                children.destroy() #destroy the widget
                self.limg.pack()#pack the background image

    def get_ship(self, x, y, dir, a, b, c, matrix, ship, ships, player): #function to get the coordinates and direction of the ship when button is pressed  and place the ship on the matrix
        if not player.sea.check_out_of_bounds(int(x.get())-1, int(y.get())-1, dir.get(), ship) or not player.sea.has_collision(int(x.get())-1, int(y.get())-1, dir.get(), ship, matrix): #check if user input is valid
            tk.messagebox.showerror("Error", "Invalid ship placement") #show error message if user input is invalid
            return #return from the function so the ship doesn't get placed
        a.append(x.get()) #add the x coordinate to the list of x coordinates
        b.append(y.get()) #add the y coordinate to the list of y coordinates
        c.append(dir.get())#add the direction to the list of directions
        self.place_ship(matrix, ship, a, b, c, ships) #call the place_ship function to place the ship on the matrix
        self.initialize_matrix(matrix, 150, 200) #call the initialize_matrix function to display the matrix on the window

    def get_last_ship(self, x, y, dir, a, b, c, matrix, ship, var, ships, player): #function to get the coordinates and direction of the ship when button is pressed last and place the ship on the matrix
        if not player.sea.check_out_of_bounds(int(x.get())-1, int(y.get())-1, dir.get(), ship) or not player.sea.has_collision(int(x.get())-1, int(y.get())-1, dir.get(), ship, matrix): #check if user input is valid
            tk.messagebox.showerror( #show error message if user input is invalid
                title="Error", message="Invalid ship placement")
            return
        a.append(x.get()) #add the x coordinate to the list of x coordinates
        b.append(y.get())#add the y coordinate to the list of y coordinates
        c.append(dir.get())#add the direction to the list of directions
        self.destroy_frame()#call the destroy_frame function to clear the window
        self.place_ship(matrix, ship, a, b, c, ships)#call the place_ship function to place the ship on the matrix
        self.initialize_matrix(matrix, 150, 200)#call the initialize_matrix function to display the matrix on the window
        var.set(1)#set the variable to 1 so the wait_variable function in the place_ships function can continue and the game can start

    def place_ship(self, matrix, ship, a, b, c, ships): #function to place the ship on the matrix
        if ship == "carrier": #check which ship is being placed
            x = a[0]#get the x coordinate of the ship
            y = b[0]#get the y coordinate of the ship
            dir = c[0]#get the direction of the ship
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
        if dir == "h": #check the direction of the ship
            for i in range(ships[ship]): #iterate through the length of the ship
                matrix[int(x)-1][int(y) + i - 1] = 1 #place the ship on the matrix by changing the value of the matrix at the coordinates of the ship to 1 and changing the y coordinate ships[ship] times
        else:
            for i in range(ships[ship]): #iterate through the length of the ship
                matrix[int(x)-1 + i][int(y)-1] = 1 #place the ship on the matrix by changing the value of the matrix at the coordinates of the ship to 1 and changing the x coordinate ships[ship] times

    def return_coords(self, player, computer): #function to return the coordinates of the player's shot
        var2 = tk.IntVar() #create a variable to use with the wait_variable function
        xcoord = StringVar()#create a variable to store the x coordinate of the shot
        xcoord.set("1")#set the default value of the variable to 1
        ycoord = StringVar()#create a variable to store the y coordinate of the shot
        ycoord.set("1")#set the default value of the variable to 1
        OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]#create a list of the options for the coordinates
        OptionMenu(self, xcoord, *OPTIONS).place(x=975, y=500)#create a drop down menu for the x coordinate
        OptionMenu(self, ycoord, *OPTIONS).place(x=975, y=540)#create a drop down menu for the y coordinate
        img = Image.open("coordsbutton.png")#open the image for the button that will be used to submit the coordinates
        img = img.resize((120, 70), Image.ANTIALIAS)#resize the image
        test = ImageTk.PhotoImage(img)#convert the image to a PhotoImage
        button6 = tk.Button(self, image=test, command=partial(#create a button that will be used to submit the coordinates
            self.return_coords2, xcoord, ycoord, player, computer, var2))
        button6.place(x=925, y=580)#place the button on the window
        button6.wait_variable(var2)#wait for the button to be pressed before continuing

    def return_coords2(self, xcoord, ycoord, player, computer, var):#function to get the coordinates of the player's shot and give the shot to the player
        global x #create a global variable to store the x coordinate of the shot
        x = xcoord.get()#get the x coordinate of the shot from the drop down menu
        global y#create a global variable to store the y coordinate of the shot
        y = ycoord.get()#get the y coordinate of the shot from the drop down menu
        var.set(1) #set the variable to 1 so the wait_variable function in the return_coords function can continue and the game can continue
        player.take_shot(computer, x, y) #call the take_shot function to give the shot to the player


class Game(): #class to run the game
    def __init__(self, player1, computer): #function to initialize the game
        self.window = Window()#create a window object to display the game 
        self.player1 = player1 #create a player object to represent the player
        self.computer = computer #create a computer object to represent the computer
        self.window.initialize_matrix(self.player1.sea.matrix, 150, 200) #call the initialize_matrix function to display the player's matrix on the window
        self.turn = 1 #create a variable to store whose turn it is (1 for the player and 2 for the computer)
        self.winner = None #create a variable to store the winner of the game
        self.play_game() #call the play_game function to start the game
        self.window.mainloop() #call the mainloop function to start the window

    def play_game(self): #function to play the game
        self.window.place_ships(self.player1) #call the place_ships function to place the ships on the player's matrix
        self.window.initialize_matrix(self.player1.visible_matrix, 1125, 200) #the player is not allowed to see the computer's matrix so the player's visible matrix is displayed on the window
        while not self.winner: #loop until there is a winner
            self.take_turn()#call the take_turn function to take a turn
            self.window.initialize_matrix( #call the initialize_matrix function to display the player's visible matrix on the window
                self.player1.visible_matrix, 1125, 200)
            self.window.initialize_matrix(self.player1.sea.matrix, 150, 200)#call the initialize_matrix function to display the player's matrix on the window
            self.check_winner() #call the check_winner function to check if there is a winner

    def take_turn(self): #function to take a turn
        if self.turn == 1: #check whose turn it is
            self.window.return_coords(self.player1, self.computer) #call the return_coords function to get the coordinates of the player's shot and give the shot to the player
            self.turn = 2 #change the turn to the computer
        else: #if it is the computer's turn
            self.computer.auto_take_shot(self.player1)#call the auto_take_shot function to give the shot to the computer
            self.turn = 1#change the turn to the player

    def check_winner(self):#function to check if there is a winner
        if self.player1.tiles_sunk == 17:#check if the player has sunk all of the computer's ships
            self.winner = 2#set the winner to the player
            winsound.PlaySound('win.wav', winsound.SND_FILENAME)#play the win sound
        elif self.computer.tiles_sunk == 17:#check if the computer has sunk all of the player's ships
            self.winner = 1#set the winner to the computer
            winsound.PlaySound('win.wav', winsound.SND_FILENAME)#play the win sound


class Player():#class to represent the player
    def __init__(self, sea):#function to initialize the player
        self.sea = sea#store the sea object that the player will use
        self.tiles_sunk = 0#store the number of tiles that the player has sunk
        self.visible_matrix = [[0 for x in range(10)] for y in range(10)]#create a matrix to store the player's visible matrix (the player can only see the tiles that they have shot at)

    def take_shot(self, computer, x, y): #function to give the shot to the player
        if computer.sea.matrix[int(x)-1][int(y)-1] == 1: #check if the shot hit a ship or not in the computer's matrix
            winsound.PlaySound('hit.wav', winsound.SND_FILENAME) #play the hit sound
            computer.sea.matrix[int(x)-1][int(y)-1] = 2#change the value of the tile in the computer's matrix to 2 to show that it has been hit
            self.visible_matrix[int(x)-1][int(y)-1] = "H"#change the value of the tile in the player's visible matrix to "H" to show that it has been hit, this is converted into images in the initialize_matrix function
            self.tiles_sunk += 1#increase the number of tiles that the player has sunk by 1
        else: #if the shot did not hit a ship
            winsound.PlaySound('miss.wav', winsound.SND_FILENAME) #play the miss sound
            computer.sea.matrix[int(x)-1][int(y)-1] = 3 #change the value of the tile in the computer's matrix to 3 to show that it has been missed
            self.visible_matrix[int(x)-1][int(y)-1] = "W" #change the value of the tile in the player's visible matrix to "W" to show that it has been missed, this is converted into images in the initialize_matrix function


class Computer(): #class to represent the computer
    def __init__(self, sea): #function to initialize the computer
        self.sea = sea #store the sea object that the computer will use
        self.sea.auto_place_ships() #call the auto_place_ships function to place the ships on the computer's matrix automatically
        self.tiles_sunk = 0 #store the number of tiles that the computer has sunk

    def auto_take_shot(self, player): #function to give the shot to the computer
        x = random.randint(0, 9) #generate a random number between 0 and 9
        y = random.randint(0, 9)
        while player.sea.matrix[x][y] == (2 or 3): #check if the tile has already been shot at
            x = random.randint(0, 9) #generate a new random number between 0 and 9
            y = random.randint(0, 9)
        if player.sea.matrix[x][y] == 1: #check if the shot hit a ship or not in the player's matrix
            winsound.PlaySound('hit.wav', winsound.SND_FILENAME) #play the hit sound
            player.sea.matrix[x][y] = 2 #change the value of the tile in the player's matrix to 2 to show that it has been hit
            self.tiles_sunk += 1 #increase the number of tiles that the computer has sunk by 1
        else:
            winsound.PlaySound('miss.wav', winsound.SND_FILENAME) #play the miss sound
            player.sea.matrix[x][y] = 3 #change the value of the tile in the player's matrix to 3 to show that it has been missed


class Sea: #class to represent the sea
    def __init__(self, ships): #function to initialize the sea
        self.matrix = [[0 for x in range(10)] for y in range(10)] #create a matrix to store the sea
        self.ships = ships #store the ships that the sea will use

    def check_out_of_bounds(self, x, y, dir, ship): #function to check if the ship is out of bounds --> has a coordinate outside of the sea
        if dir == "h": #check if the ship is placed horizontal or vertical
            return y + self.ships[ship] <= 10  #return true if the ship is not out of bounds
        else: #if the ship is placed vertical
            return x + self.ships[ship] <= 10 #also return true if the ship is not out of bounds, counterintuitive --> true means that the ship is not out of bounds

    def has_collision(self, x, y, dir, ship, matrix): #function to check if the ship has a collision with another ship
        if dir == "h": #check if the ship is placed horizontally or vertically
            for i in range(self.ships[ship]): #loop through the length of the ship
                if (y+i >= 9 or matrix[x][y+i] == 1 or matrix[x+1][y+i] == 1 or matrix[x-1][y+i] == 1 or matrix[x][y+i+1] == 1 or matrix[x][y+i-1] == 1): #check if the ship has a collision with another ship or the edge of the sea by checking the tiles around the ship 
                    return False #return false if the ship has a collision
            return True #return true if the ship does not have a collision
        else: #if the ship is placed vertically
            for i in range(self.ships[ship]): #loop through the length of the ship
                if (x+i >= 9 or matrix[x+i][y] == 1 or matrix[x+i][y+1] == 1 or matrix[x+i][y-1] == 1 or matrix[x+i+1][y] == 1 or matrix[x+i-1][y] == 1): #check if the ship has a collision with another ship or the edge of the sea by checking the tiles around the ship
                    return False #return false if the ship has a collision
            return True #return true if the ship does not have a collision

    def auto_place_ships(self): #function to place the ships on the sea automatically
        for ship in self.ships.keys(): #loop through the ships
            x = random.randint(0, 8) #generate a random number between 0 and 8
            y = random.randint(0, 8)
            direction = random.choice(["h", "v"]) #generate a random direction for the ship to be placed in
            while not self.check_out_of_bounds(x, y, direction, ship) or not self.has_collision(x, y, direction, ship, self.matrix): #check if the ship is out of bounds or has a collision
                x = random.randint(0, 8) #generate a new random number between 0 and 8
                y = random.randint(0, 8)
            if direction == "h": #check if the ship is placed horizontally or vertically
                for i in range(self.ships[ship]): #loop through the length of the ship
                    self.matrix[x][y+i] = 1 #change the value of the tile in the sea to 1 to show that it has a ship on it by placing the ship on the same x coordinate and increasing the y coordinate by 1 each time 
            else:
                for i in range(self.ships[ship]): #loop through the length of the ship
                    self.matrix[x+i][y] = 1#same as with h but with x and y reversed


game1 = Game(Player(Sea(common_ships)), Computer(Sea(common_ships))) #create a game object with a player and a computer


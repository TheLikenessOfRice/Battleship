"""
                if direction == 'N':
                    for i in range(self.ships[ship]-1):
                        X -= 1
                        if X < 0 or Y < 0 or X > 9 or Y > 9:
                            print("Cannot place ship there")
                            while X != O_X:
                                X += 1
                                self.gridY[X][Y] = '.'
                            break
                        self.gridY[X][Y] = ship[0].upper()
                        finished = True
                elif direction == 'S':
                    for i in range(self.ships[ship]-1):
                        X += 1
                        if X < 0 or Y < 0 or X > 9 or Y > 9:
                            print("Cannot place ship there")
                            while X != O_X:
                                X -= 1
                                self.gridY[X][Y] = '.'
                            break
                        self.gridY[X][Y] = ship[0].upper()
                        finished = True
                elif direction == 'E':
                    for i in range(self.ships[ship]-1):
                        Y += 1
                        if X < 0 or Y < 0 or X > 9 or Y > 9:
                            print("Cannot place ship there")
                            while Y != O_Y:
                                Y -= 1
                                self.gridY[X][Y] = '.'
                            break
                        self.gridY[X][Y] = ship[0].upper()
                        finished = True
                elif direction == 'W':
                    for i in range(self.ships[ship]-1):
                        Y -= 1
                        if X < 0 or Y < 0 or X > 9 or Y > 9:
                            print("Cannot place ship there")
                            while Y != O_Y:
                                print("looping")
                                Y += 1
                                self.gridY[X][Y] = '.'
                            else:
                                break
                        self.gridY[X][Y] = ship[0].upper()
                        print("making it here")
                        finished = True
"""
import os
import os.path
import pickle


def line():
        print("----------------------------------------------------------")


class Player(object):
    """hits = 0
    misses = 0
    ships_sunk = 0
    ships_afloat = 5
    gridY = []
    gridT = []
    ships = {
        'patrol': 2,
        'battleship': 4,
        'aircraft carrier': 5,
        'submarine': 3,
        'destroyer': 3
    }
    rows = 10
    columns = 10
"""
    def __init__(self, name, player):
        self.hits = 0
        self.misses = 0
        self.ships_sunk = 0
        self.ships_afloat = 5
        self.ship_char = ''
        self.gridY = []
        self.gridT = []
        self.ships = {
            'patrol': 2,
            'battleship': 4,
            'aircraft carrier': 5,
            'submarine': 3,
            'destroyer': 3
        }
        self.ship_hits = {
            'P': 2,
            'B': 4,
            'A': 5,
            'S': 3,
            'D': 3
        }
        self.rows = 10
        self.columns = 10
        self.name = name
        self.player = player
        for i in range(self.rows):
            self.gridY.append(['.']*self.columns)
            self.gridT = [['.']*self.columns for x in range(9)]


    def place_ship(self):
        unplaced_ships = self.ships

        count = 0
        ship = ""
        while len(self.ships) > 0:
            print("Available ships are: ", end="")
            for i in unplaced_ships:
                print(i, end="")
                print(" ", end="")
            print()

            isin_dict = False
            while not isin_dict:
                ship = input("Which ship do you want to place? ")
                ship = ship.lower()

                isin_dict = self.ships.get(ship, False)

                if isin_dict:
                    break
            finished = False
            while not finished:
                finished = False
                while True:
                    while True:
                        c_p = True

                        start = input("Where do you want one end of the ship to be placed(ex. A3)? ")

                        print("F:", finished)
                        direction = input("What direction do you want the ship pointed(N/S/E/W)? ")
                        direction = direction.upper()

                        if c_p and len(start) > 3 or len(start) < 2:
                            print("length error")
                            c_p = False

                        if c_p and not (ord(start[0].upper()) > 64 and ord(start[0].upper()) < 123):
                            print(start[0].upper())
                            print("1")
                            c_p = False

                        if c_p and (len(direction) > 1):
                            c_p = False


                        if c_p and (ord(start[1]) > 57 or ord(start[1]) < 48):
                            c_p = False

                        if c_p and len(start) > 2:
                            if ord(start[2]) > 57 or ord(start[2]) < 48:
                                c_p = False

                        if c_p:
                            for i in range(int(start[1:])):
                                if i < 0 and i > 11:
                                    print(start[1:])
                                    print("2")
                                    c_p = False

                        if c_p:
                            X = ord(start[0].upper())-65
                            Y = int(start[1:])-1

                            O_X = X
                            O_Y = Y

                        if c_p and self.gridY[X][Y] != '.':
                            c_p = False

                        if c_p:
                            break
                        else:
                            print("Incorrect input")



                    print("made it here")

                    if X < 0 or Y < 0 or X > 9 or Y > 9:
                        print("Invalid ship placment")
                    else:
                        break

                self.gridY[X][Y] = ship[0].upper()

                finished = self.check_board(direction, X, Y, O_X, O_Y, ship)
                print("F:", finished)
                if finished:
                    break
            del self.ships[ship]
            os.system('cls')
            #os.system('clear')
            self.print_score()
            self.print_grid()
            if len(self.ships) == 0:
                break

        os.system('cls')

    def check_board(self, direction, X, Y, O_X, O_Y, ship):

        print("X:", X)
        print("Y:", Y)
        print("O_X:", O_X)
        print("O_Y:", O_Y)
        print("Ship", ship)
        print("SL:", self.ships[ship]-1)

        if direction == 'N':
            for i in range(self.ships[ship]-1):
                X -= 1

                if X < 0 or Y < 0 or X > 9 or Y > 9:
                    print("Cannot place ship there")
                    while X != O_X:
                        X += 1
                        self.gridY[X][Y] = '.'
                    return False

                if self.gridY[X][Y] != '.':
                    print("Cannot place ship there")
                    while X != O_X:
                        X += 1
                        self.gridY[X][Y] = '.'
                    return False

                self.gridY[X][Y] = ship[0].upper()
            return True

        elif direction == 'S':
            for i in range(self.ships[ship]-1):
                print("looping")
                X += 1
                if X < 0 or Y < 0 or X > 9 or Y > 9:
                    print("Cannot place ship there")
                    while X != O_X:
                        X -= 1
                        self.gridY[X][Y] = '.'
                    return False

                if self.gridY[X][Y] != '.':
                    print("Cannot place ship there")
                    while X != O_X:
                        X -= 1
                        self.gridY[X][Y] = '.'
                    return False


                self.gridY[X][Y] = ship[0].upper()
            return True

        elif direction == 'E':
            for i in range(self.ships[ship]-1):
                Y += 1
                if X < 0 or Y < 0 or X > 9 or Y > 9:
                    print("Cannot place ship there")
                    while Y != O_Y:
                        Y -= 1
                        self.gridY[X][Y] = '.'
                    return False

                if self.gridY[X][Y] != '.':
                    print("Cannot place ship there")
                    while Y != O_Y:
                        Y -= 1
                        self.gridY[X][Y] = '.'
                    return False

                self.gridY[X][Y] = ship[0].upper()
            return True


        elif direction == 'W':
            for i in range(self.ships[ship]-1):
                Y -= 1
                if X < 0 or Y < 0 or X > 9 or Y > 9:
                    print("Cannot place ship there")
                    while Y != O_Y:
                        print("looping")
                        Y += 1
                        self.gridY[X][Y] = '.'
                    return False

                if self.gridY[X][Y] != '.':
                    print("Cannot place ship there")
                    while Y != O_Y:
                        print("looping")
                        Y += 1
                        self.gridY[X][Y] = '.'
                    return False

                self.gridY[X][Y] = ship[0].upper()
                print("making it here")
            return True



    def print_score(self):
        line()
        print("Player: " + self.name)
        print("Ships Afloat: ", self.ships_afloat)
        print("-----Accuracy------")
        print("Hits: " + str(self.hits) + " Misses: " + str(self.misses))
        print("Ships Sunk: " + str(self.ships_sunk))
        line()



    def print_grid(self):
        alph = ['A', 'B','C','D','E','F','G','H','I','J']
        num = ['1', '2', '3','4','5','6','7','8','9','10']
        row = ""
        top_row = "   "

        print("Top")
        for j in range(10):
            top_row = top_row + num[j] + " "
        else:
            for i in range(13):
                top_row = top_row + " "

        print (top_row)
        for i in range(9):
            row = row + alph[i] + " |"
            for a in range(10):
                #print("I: " , i, " A: ", a)
                #print("TG:", self.gridT)
                row = row + self.gridT[i][a] + " "
            row = row + "|" + "\n"
        print (row)

        row = ""

        print("Bottom")

        print (top_row)
        for i in range(9):
            row = row + alph[i] + " |"
            for a in range(10):
                row = row + self.gridY[i][a] + " "

            """ for a in range(10):
                row = row + " "
            else:
                row = row + alph[i] + " |"
            for a in range(len(grid2[i])):
                row = row + grid2[i][a] + " "
            """
            row = row + "|" + "\n"

        print (row)

    def check_hit(self, coord):
        X = ord(coord[0].upper())-65
        Y = int(coord[1:])-1

        if self.gridY[X][Y] != '.':
            self.gridY[X][Y] = 'H'
            return True
        else:
            self.gridY[X][Y] = 'M'
            return False

    def get_char(self, X, Y):
        return self.gridY[X][Y]

    def attack(self):
        self.print_score()
        self.print_grid()
        hit = False
        while True:
            c_p = True
            print("------Attacking------")
            coord = input("Enter guess for attack: ")
            print("coord0: " + coord[0])
            print("coord1: " + coord[1])
            if(len(coord) > 2):
                print("coord2: " + coord[2])

            if c_p and len(coord) > 3 or len(coord) < 2:
                print("length error")
                c_p = False

            if c_p and not (ord(coord[0].upper()) > 64 and ord(coord[0].upper()) < 74):
                print(coord[0].upper())
                print("1")
                c_p = False

            if c_p and (ord(coord[1]) >57 or ord(coord[1]) <= 48):
                print("error2")
                c_p = False

            if c_p and len(coord) > 2:
                print("error3")
                if coord[2] != '0':
                    print(coord[2])
                    c_p = False

            if c_p:
                X = ord(coord[0].upper())-65
                Y = int(coord[1:])-1
                print("here", self.gridY[X][Y])
                if self.gridT[X][Y] == 'H' or self.gridT[X][Y] == 'M':
                    print("Cannot attack there")
                    c_p = False
                else:
                    break


        if(self.player == 1):
            ship_char = P2.get_char(X,Y)
        else:
            ship_char = P1.get_char(X,Y)


        if self.player == 1:
            hit = P2.check_hit(coord)
        else:
            hit = P1.check_hit(coord)

        if hit == False:
            print("miss")
            self.gridT[X][Y] = 'M'
            self.misses += 1
            input("Press Enter To Continue")
        elif hit == True:
            print("HIT")
            self.gridT[X][Y] = 'H'
            self.hits += 1
            if self.player == 1:
                P2.adjust_ships(X,Y, ship_char)
            else:
                P1.adjust_ships(X,Y, ship_char)
            input("Press Enter To Continue")
        else:
            print("error")
        os.system('cls')

    def turn_change(self):
        line()
        for i in range(10):
            print()

        print("             Turn:", self.name)
        print("             Press Enter to continue")

        for i in range(10):
            print()
        line()
        input()
        os.system('cls')

    def adjust_ships(self, X, Y, char):
        self.ship_hits[char] -= 1
        if(self.ship_hits[char] == 0):
            print("Ship Sunk")
            self.ships_afloat -= 1
            if(self.player == 1):
                P2.ships_sunk += 1
            else:
                P1.ships_sunk += 1

    def check_winner(self):
        if(self.player == 1):
            if(P1.get_largest() == 0):
               return True
            return False
        else:
            if(P2.get_largest() == 0):
                return True
            return False


    def get_largest(self):
        largest = 0
        for key in self.ship_hits:
            if self.ship_hits[key] > largest:
                largest = self.ship_hits[key]

        return largest



    def set_variables(self, save_data, offset):

        self.hits = save_data[2 + offset]
        self.misses = save_data[3 + offset]
        self.ships_sunk = save_data[4 + offset]
        self.ships_afloat = save_data[5 + offset]
        self.gridY = save_data[6 + offset]
        self.gridT = save_data[7 + offset]
        self.ships = save_data[8 + offset]

        """self.hits = int(save_game.readline().rstrip())
        self.misses = int(save_game.readline().rstrip())
        self.ships_sunk = save_game.readline().rstrip()
        self.ships_afloat = save_game.readline().rstrip()
        #self.gridY = save_game.readline().rstrip()
        self.gridY = pickle.load(save_game)
        self.gridT = pickle.load(save_game)
        print("GY: ", isinstance(self.gridY, str))
        #self.gridT = save_game.readline().rstrip()
        print("GT: ", isinstance(self.gridT, str))
        self.ships = save_game.readline().rstrip()
        """

    def save_game(self, save_game, save_list):

        print("P:", self.player)

        save_list.append(self.hits)

        save_list.append(self.misses)

        save_list.append(self.ships_sunk)

        save_list.append(self.ships_afloat)

        save_list.append(self.gridY)

        save_list.append(self.gridT)

        save_list.append(self.ships)

        return save_list


        """save_game.write(str(self.hits) + '\n')
        save_game.write(str(self.misses) + '\n')
        save_game.write(str(self.ships_sunk) + '\n')
        save_game.write(str(self.ships_afloat) + '\n')
        pickle.dump(self.gridY, save_game)
        pickle.dump(self.gridT, save_game)
        #save_game.write(self.gridY + '\n')
        #save_game.write((self.gridT) + '\n')
        save_game.write(str(self.ships) + '\n')
        """


def save_file(save):
    save_list = []
    if(save == 'Y'):
        filename = input("What do you want the name of your saved game to be?")
        filename = str(filename) + ".txt"

        file_exists = os.path.isfile(filename)
        if file_exists:
            overwrite = input("Saved game already exists. Do you want to overwrite?(Y/N)")
            overwrite = overwrite.upper()
            if overwrite == 'Y':
                directory = os.getcwd() + '\\' + filename
                os.remove(directory)
                save_game = open(filename, 'wb')
        else:
            save_game = open(filename, 'wb')

        save_list.append(P1_name)
        save_list.append(P2_name)

        list1 = P1.save_game(save_game, save_list)
        list2 = P2.save_game(save_game, save_list)

        save_list.append(list1)
        save_list.append(list2)

        pickle.dump(save_list, save_game)

    #save_game.close()











#Start Game

#ShipsP1 = ['patrol', 'battleship', 'aircraft carrier', 'submarine', 'destroyer']

#Welcome the Player

print("Welcome to Battleship")

load = input("Do you want to load a saved game?(Y/N) ")
load = load.upper()

if load == 'Y':
    filename = input("What is the name of the save game? ")
    filename = str(filename) + ".txt"
    save_game = open(filename, "rb")
    save_data = pickle.load(save_game)
    print(save_data)
    P1_name = save_data[0]
    P2_name = save_data[1]
    #P1_name = save_game.readline().rstrip()
    #P2_name = save_game.readline().rstrip()

else:
    P1_name = "Bob"#input("What is Player 1's name?")
    P2_name = "Gregory"#input("What is Player 2's name?")

P1 = Player(P1_name, 1)
P2 = Player(P2_name, 2)

if load == 'Y':
    P1.set_variables(save_data, 0)
    P2.set_variables(save_data, 7)



print("Welcome " + P1_name + " and " + P2_name + "!")
line()

#grid[1][2] = "X"
#grid[2][0] = "X"

winner = False

if load == 'N':
    save = input("Do you want to save the game?(Y/N)")
    save = save.upper()
    if save == 'Y':
        save_file(save)



if load == 'N':
    P1.turn_change()

    P1.print_score()

    P1.print_grid()

    P1.place_ship()

    P2.turn_change()

    P2.print_score()

    P2.print_grid()

    P2.place_ship()

if load == 'N':
    save = input("Do you want to save the game?(Y/N)")
    save = save.upper()
    if save == 'Y':
        save_file(save)

"""if(save == 'Y'):
    filename = input("What do you want the name of your saved game to be?")
    filename = str(filename) + ".txt"

    file_exists = os.path.isfile(filename)
    if file_exists:
        overwrite = input("Saved game already exists. Do you want to overwrite?(Y/N)")
        overwrite = overwrite.upper()
        if overwrite == 'Y':
            directory = '/' + filename
            os.remove(directory)
            save_game = open(filename, 'w')
    else:
        save_game = open(filename, 'w')

    save_game.write(P1_name + '\n')
    save_game.write(P2_name + '\n')

    P1.save_game(save_game)
    P2.save_game(save_game)

save_game.close()
"""


while not winner:

    P1.turn_change()

    P1.attack()

    if(P1.check_winner() and not P2.check_winner()):
        os.system('cls')
        line()
        print("Player 2 Wins!")
        line()
        break
    elif(not P1.check_winner() and P2.check_winner()):
        os.system('cls')
        line()
        print("Player 1 Wins!")
        line()
        break

    P2.turn_change()

    P2.attack()

    if(P1.check_winner() and not P2.check_winner()):
        os.system('cls')
        line()
        print("Player 2 Wins!")
        line()
        break
    elif(not P1.check_winner() and P2.check_winner()):
        os.system('cls')
        line()
        print("Player 1 Wins!")
        line()
        break

    save = input("Do you want to save the game?(Y/N)")
    save = save.upper()
    if save == 'Y':
        save_file(save)






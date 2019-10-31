from settings import *
import sys
import time
from game_func import Action

class Game:
    def __init__(self):
        pass

    def run_command(self):
        self.uc = 'Unknown command'
        if len(self.c) != 0: # check if list empty
            if self.c[0] == '?':# Option '?'
                for i in C_ALL:
                    print(i, end='\n')
            elif self.c[0] == 'quit': # Option 'quit'
                sys.exit()
            #========================LIST================================
            elif self.c[0] == 'list': # Option 'list'
                if len(self.c) == 1: # Check if just 'list'
                    print('list <attribute>')
                elif self.c[1] == '?': # Option 'list ?'
                    for i in C_LIST:
                        print(i, end='\n')
                else:
                    print(uc)
            #=========================PLAYER==============================
            elif self.c[0] == 'player': # Option 'player'
                if len(self.c) > 1:
                    print(self.uc)
                else:
                    print('\nName:     ', PLAYER['name'])
                    print('Level:    ', PLAYER['level'])
                    print('Ship name:', PLAYER['shipname'])
                    print('ISK:      ', PLAYER['isk'])
            #=========================Status==============================
            elif self.c[0] == 'status': # View player status
                d = ''
                if len(self.c) > 1:
                    print(self.uc)
                else:
                    if STATUS['docked'] == True:
                        d = 'Yes'
                    else:
                        d = 'No'
                    print('Docked:    ', d)
                    if STATUS['docked'] == True:
                        print('Station:   ', STATUS['station'])
                    print('Sector:    ', STATUS['sector'])

            #=========================Station=============================
            elif self.c[0] == 'station':
                if len(self.c) == 1:    # If command is one word
                    print('station <attribute>')
                elif self.c[1] == '?':
                    for i in C_STATION1:
                        print(i, end='\n')
                elif self.c[1] == 'dock':   # Dock at station
                    if STATUS['docked'] == False:
                        STATUS['docked'] = True
                        print('You are now docked at', STATUS['station'])
                    else:
                        print('You are already docked')
                elif self.c[1] == 'undock': # Undock from station
                    if STATUS['docked'] == True:
                        STATUS['docked'] = False
                        STATUS['station'] == ''
                        print('You are undocking from', STATUS['station'])
                else:
                    print(self.uc)
            #===========================Warp==============================
            elif self.c[0] == 'warp': # Warp to
                if len(self.c) == 1:
                    print('warp <attribute>')
                elif self.c[1] == '?':
                    for i in C_SECTORS:
                        print(i, end='\n')
                elif len(self.c) == 2:
                    if STATUS['docked'] == True:
                        print('You cannot warp while docked')
                    else:
                        if self.c[1] == 'Verran': # Verran Sector
                            if STATUS['sector'] == 'Verran':
                                print('You are already in the Verran Sector')
                            else:
                                STATUS['sector'] = 'Verran'
                                Action.warp_to(self.c[1])
                        elif self.c[1] == 'Terran': # Terran Sector
                            if STATUS['sector'] == 'Terran':
                                print('You are already in the Terran Sector')
                            else:
                                STATUS['sector'] = 'Terran'
                                Action.warp_to(self.c[1])
                        elif self.c[1] == 'Martian': # Martian Sector
                            if STATUS['sector'] == 'Martian':
                                print('You are already in the Martian Sector')
                            else:
                                STATUS['sector'] = 'Martian'
                                Action.warp_to(self.c[1])
                        elif self.c[1] == 'Jupiter': # Jupiter Sector
                            if STATUS['sector'] == 'Jupiter':
                                print('You are already in the Jupiter Sector')
                            else:
                                STATUS['sector'] = 'Jupiter'
                                Action.warp_to(self.c[1])
                        elif self.c[1] == 'Saturn': # Saturn Sector
                            if STATUS['sector'] == 'Saturn':
                                print('You are already in the Saturn Sector')
                            else:
                                STATUS['sector'] = 'Saturn'
                                Action.warp_to(self.c[1])
                        elif self.c[1] == 'Chaos': # Chaos Sector
                            if STATUS['sector'] == 'Chaos':
                                print('You are already in the Chaos Sector')
                            else:
                                STATUS['sector'] = 'Chaos'
                                Action.warp_to(self.c[1])
                        else:
                            print(self.uc)
                else:
                    print(self.uc)

            #=============================Scan============================
            elif self.c[0] == 'scan':       ### Make function in main.py
                if len(self.c) == 1:    # If length of command is 1
                    print('Scanning...')
                    time.sleep(3)
                else:
                    print(self.uc)

            #=============================END=============================
            else:
                print(self.uc)

    def read_command(self, command): # Function that handles commands
        command = command
        command = command.strip()
        c = command.split()# Converted string to a list
        return c

    def new_game(self):
        if PLAYER['name'] == '' and PLAYER['shipname'] == '':
            p_name = input('Pilot name: ')
            s_name = input('Ship name: ')
            PLAYER['name'] = p_name
            PLAYER['shipname'] = s_name
            while True:
                command = input('> ')
                c = read_command(command)
                run_command(c)
        else:
            print('<<player dictionary error>>')# Let know of problem with names in 'player'

g = Game()
g.new_game()
    # wait for command

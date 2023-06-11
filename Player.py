import Game
import Bestiary
import random

class Player:

    def __init__(self, id):
        self.id = id
        self.bestiary = None
        self.game = None
        
    # parses command to then calls other commands
    def handle_command(self, message):
        command = str(message.content).lower()[1:].split()

        if command[0] == "r" or command[0] == "roll":
            return self.roll(command)
        elif command[0] == "i" or command[0] == "init" or command[0] == "initiative":
            pass
        elif command[0] == "r" or command[0] == "rem" or command[0] == "remove":
            pass
        elif command[0] == "spell":
            pass
        elif command[0] == "pc":
            pass
        elif command[0] == "start":
            pass
        elif command[0] == "end":
            pass
        elif command[0] == "help":
            pass
        elif command[0] == "bestiary" or command[0] == "beast" or command[0] == "b":
            pass

        return
    
    # roll a die, with the following format
    # ?[r|roll] [dis|adv|#d#] [-#|+#|_]
    # if you want to roll a flat d20, then skip middle and you can do + or - or nothing
    def roll(self, command) -> str:
        # roll a d20
        if len(command) == 1:
            return str(random.randint(1,20)) 
        elif len(command) == 2 or len(command) == 3:
                # d20 rolls
                if command[1] == 'dis' or command[1] == 'adv':
                    bonus = 0
                    # check if command has a bonus
                    if len(command) == 3:
                        val = command[2][1:]
                        if val.isdigit():
                            if command[2].startswith('+'):
                                bonus = bonus + int(val)
                            elif command[2].startswith('-'):
                                bonus = bonus - int(val)
                        # return w/o sending because of incorrect format
                        return                        
                    r1 = random.randint(1,20)
                    r2 = random.randint(1,20)
                    if command[1] == 'dis':
                        result = min(r1,r2)
                    else:    
                        result = max(r1,r2)

                    return str(r1) + ' ' + str(r2) + ' = ' + '' 
                elif command[1].startswith('+') and command[1][1:].isdigit():
                    pass
                elif command[1].startswith('-') and command[1][1:].isdigit():
                    pass
                else:
                    dice = command[1].split('d')
                    if len(dice) == 2 and (dice[0] == '' or dice[0].isdigit()) and dice[1].isdigit():
                        if  dice[0] == '':
                            i = 1

    def initiative(self, message, command):
        return
    def remove(self, message, command):
        return
    def spell(self, message, command):
        return
    def pc(self, message, command):
        return
    def bestiary(self, message, command):
        return
    def start(self, message, command):
        return
    def end(self, message, command):
        return
    
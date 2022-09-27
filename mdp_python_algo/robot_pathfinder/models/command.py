from mdp_python_algo.robot_pathfinder.config.constants import Moves


class Command:
    
    def __init__(self, move: Moves):
        self.move = move
        self.repeat = 1
        self.zero = "0"
   
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.repeat>10:
            return f'{self.move.name}{self.repeat*10}'
        else:
            if self.move.name == "l" or self.move.name == "r" or self.move.name == "m" or self.move.name == "o":
                return f'{self.move.name}{self.zero}{90}'
            return f'{self.move.name}{self.zero}{self.repeat*10}'
    def inc_repeat(self):
        self.repeat += 1

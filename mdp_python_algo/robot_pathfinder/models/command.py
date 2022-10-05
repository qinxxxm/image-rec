from mdp_python_algo.robot_pathfinder.config.constants import Moves


class Command:
    
    def __init__(self, move: Moves):
        self.move = move
        self.repeat = 1
        self.zero = "0"
   
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.move.name == "l" or self.move.name == "r" or self.move.name == "m" or self.move.name == "o":
            return f'{self.move.name}{str(self.repeat*90).zfill(3)}'
        return f'{self.move.name}{str(self.repeat*10).zfill(3)}'
        
    def inc_repeat(self):
        self.repeat += 1

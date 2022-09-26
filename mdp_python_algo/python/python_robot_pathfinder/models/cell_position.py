from utils.position_utils import *


class CellPosition:
    
    def __init__(self, cell_x: int, cell_y: int, facing: Facing) -> None:
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.facing = facing
    
    def __repr__(self):
        return self.__str__()    
        
    def win_pos(self):
        return cellpos_winpos(self.cell_pos2d())    
    
    def pos(self):
        return cellpos_pos(self.cell_pos2d())
    
    def cell_pos2d(self):
        return self.cell_x, self.cell_y

    def __str__(self):
        return f'x: {self.cell_x}, y: {self.cell_y}, facing: {self.facing.name}'
    


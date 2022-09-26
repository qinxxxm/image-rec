from typing import Union

from models.cell_position import CellPosition


class Node:
    
    def __init__(self, cell_pos: CellPosition):
        self.h = 0.
        self.g = 0.
        self.open = False
        self.close = False
        self.cell_pos = cell_pos
        self.move = None
        self.predecessor: Union[Node, None] = None
    
    def __gt__(self, other):
        return self.score().__gt__(other.score())

    def score(self) -> float:
        return self.h + self.g

    def __str__(self):
        return f'{self.cell_pos}, g: {self.g}, h: {self.h}, open: {self.open}'
    
    def __cmp__(self, other):
        return self.score().__cmp__(other.score())

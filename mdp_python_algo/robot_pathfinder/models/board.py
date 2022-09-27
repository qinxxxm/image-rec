"""
Helper data structure for hybrid astar
"""
from typing import List
from mdp_python_algo.robot_pathfinder.models.arena import Arena
from mdp_python_algo.robot_pathfinder.models.node import Node
from mdp_python_algo.robot_pathfinder.models.cell_position import CellPosition
from mdp_python_algo.robot_pathfinder.config.constants import ArenaConst, Facing



class Board:
    
    def __init__(self):
        self.start: Node
        self.goal = Node        
        self.nodes: List[List[List[Node]]]
        self.valid = List[List[bool]]
    
    @classmethod
    def from_arena(cls, arena: Arena) -> 'Board':
        rows, cols = ArenaConst.NUM_ROWS, ArenaConst.NUM_COLS
        nodes = [[[Node(CellPosition(cell_x, cell_y, facing))
                   for facing in Facing]
                  for cell_x in range(cols)]
                 for cell_y in range(rows)]
        
        valid = [[True for _ in range(cols)] for _ in range(rows)]
        for obstacle in arena.obstacles:
            center = ArenaConst.VIRTUAL_OBSTACLE_RADIUS  # 1
            for dx in range(ArenaConst.VIRTUAL_OBSTACLE_RADIUS * 2 + 1):  # 3
                for dy in range(ArenaConst.VIRTUAL_OBSTACLE_RADIUS * 2 + 1):  # 3
                    cell_x = dx - center + obstacle.cell_pos.cell_x
                    cell_y = dy - center + obstacle.cell_pos.cell_y
                    if 0 <= cell_x < cols and 0 <= cell_y < rows:
                        valid[cell_y][cell_x] = False
        for y in range(rows):
            valid[y][0] = False
            valid[y][cols - 1] = False
        
        for x in range(cols):
            valid[0][x] = False
            valid[rows - 1][x] = False
        
        board = cls()
        board.nodes = nodes
        board.valid = valid
        return board

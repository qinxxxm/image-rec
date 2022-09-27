from mdp_python_algo.robot_pathfinder.models.cell_position import CellPosition


class Robot:
    
    def __init__(self, cell_pos: CellPosition) -> None:
        self.cell_pos = cell_pos

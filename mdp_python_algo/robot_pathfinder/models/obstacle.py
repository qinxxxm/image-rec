from mdp_python_algo.robot_pathfinder.config.constants import ObstacleImage, Facing, ArenaConst
from mdp_python_algo.robot_pathfinder.models.cell_position import CellPosition


class Obstacle:
    
    def __init__(self, cell_pos: CellPosition, image: ObstacleImage) -> None:
        self.cell_pos = cell_pos
        self.image = image
    
    def get_target_position(self) -> CellPosition:
        target_cell_x, target_cell_y, target_facing = self.cell_pos.cell_x, self.cell_pos.cell_y, self.cell_pos.facing
        
        if self.cell_pos.facing == Facing.UP:
            target_cell_y += ArenaConst.DETECT_CELL_DISTANCE
            target_facing = Facing.DOWN
        elif self.cell_pos.facing == Facing.DOWN:
            target_cell_y -= ArenaConst.DETECT_CELL_DISTANCE
            target_facing = Facing.UP
        elif self.cell_pos.facing == Facing.RIGHT:
            target_cell_x += ArenaConst.DETECT_CELL_DISTANCE
            target_facing = Facing.LEFT
        elif self.cell_pos.facing == Facing.LEFT:
            target_cell_x -= ArenaConst.DETECT_CELL_DISTANCE
            target_facing = Facing.RIGHT

        return CellPosition(target_cell_x, target_cell_y, target_facing)
    
    def __str__(self):
        return f'<Obstacle x: {self.cell_pos.cell_x}, y: {self.cell_pos.cell_y}, image: {self.image.name}>'
    
    def __repr__(self):
        return self.__str__()

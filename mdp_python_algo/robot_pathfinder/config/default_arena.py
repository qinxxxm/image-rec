from mdp_python_algo.robot_pathfinder.config.constants import Facing, ObstacleImage
from mdp_python_algo.robot_pathfinder.models.arena import Arena
from mdp_python_algo.robot_pathfinder.models.cell_position import CellPosition
from mdp_python_algo.robot_pathfinder.models.obstacle import Obstacle

ARENAS = list()

arena0 = Arena()
ARENAS.append(arena0)

arena0.add_obstacle(Obstacle(CellPosition(18, 6, Facing.LEFT), ObstacleImage.A))
arena0.add_obstacle(Obstacle(CellPosition(14, 1, Facing.UP), ObstacleImage.B))
arena0.add_obstacle(Obstacle(CellPosition(5, 13, Facing.DOWN), ObstacleImage.C))
arena0.add_obstacle(Obstacle(CellPosition(17, 19, Facing.DOWN), ObstacleImage.LEFT))
arena0.add_obstacle(Obstacle(CellPosition(8, 17, Facing.RIGHT), ObstacleImage.ONE))

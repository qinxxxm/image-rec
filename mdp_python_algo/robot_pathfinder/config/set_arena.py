from mdp_python_algo.robot_pathfinder.config.constants import Facing, ObstacleImage
from mdp_python_algo.robot_pathfinder.models import obstacle
from mdp_python_algo.robot_pathfinder.models.arena import Arena
from mdp_python_algo.robot_pathfinder.models.cell_position import CellPosition
from mdp_python_algo.robot_pathfinder.models.obstacle import Obstacle


def set_arena(pos_dict_full):
    pos_dict_obstacle = pos_dict_full
    pos_dict_obstacle.popitem()
    print('pos_dict_obstacle: ',pos_dict_obstacle)

    ARENAS = list()

    arena0 = Arena()
    ARENAS.append(arena0)


    for key in pos_dict_obstacle:
        arena0.add_obstacle(Obstacle(CellPosition((pos_dict_obstacle[key][0]), pos_dict_obstacle[key][1], pos_dict_obstacle[key][2]), ObstacleImage.A))

    return ARENAS

# # old arena obstacle values:
# arena0.add_obstacle(Obstacle(CellPosition(18, 6, Facing.LEFT), ObstacleImage.A))
# arena0.add_obstacle(Obstacle(CellPosition(14, 1, Facing.UP), ObstacleImage.B))
# arena0.add_obstacle(Obstacle(CellPosition(5, 13, Facing.DOWN), ObstacleImage.C))
# arena0.add_obstacle(Obstacle(CellPosition(17, 19, Facing.DOWN), ObstacleImage.LEFT))
# arena0.add_obstacle(Obstacle(CellPosition(8, 17, Facing.RIGHT), ObstacleImage.ONE))



    
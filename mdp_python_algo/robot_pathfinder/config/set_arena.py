from mdp_python_algo.robot_pathfinder.config.constants import Facing, ObstacleImage
from mdp_python_algo.robot_pathfinder.models import obstacle
from mdp_python_algo.robot_pathfinder.models.arena import Arena
from mdp_python_algo.robot_pathfinder.models.cell_position import CellPosition
from mdp_python_algo.robot_pathfinder.models.obstacle import Obstacle


def set_arena(pos_dict_full):
    # pos_dict_full contains obstacle and robot pos
    pos_dict_obstacle = pos_dict_full
    # remove the robot pos, hence only have obstacle pos
    pos_dict_obstacle.pop('ROBOT',None)
    #print('pos_dict_obstacle: ',pos_dict_obstacle)

    ARENAS = list()

    arena0 = Arena()
    ARENAS.append(arena0)

    # put obstacle pos into ARENAS
    for key in pos_dict_obstacle:
        # error handling for x, y value that falls on the boarder where car cannot aim at center of obstacle
        # shift such obstacles 1 grid towards center of arena
        if (pos_dict_obstacle[key][0] == 0 and (pos_dict_obstacle[key][2] == Facing.DOWN or pos_dict_obstacle[key][2] == Facing.UP)):
            pos_dict_obstacle[key][0] = 1
        elif (pos_dict_obstacle[key][0] == 19 and (pos_dict_obstacle[key][2] == Facing.DOWN or pos_dict_obstacle[key][2] == Facing.UP)):
            pos_dict_obstacle[key][0] = 18

        if (pos_dict_obstacle[key][1] == 0 and (pos_dict_obstacle[key][2] == Facing.LEFT or pos_dict_obstacle[key][2] == Facing.RIGHT)):
            pos_dict_obstacle[key][1] = 1
        elif (pos_dict_obstacle[key][1] == 19 and (pos_dict_obstacle[key][2] == Facing.LEFT or pos_dict_obstacle[key][2] == Facing.RIGHT)):
            pos_dict_obstacle[key][1] = 18

        arena0.add_obstacle(Obstacle(CellPosition((pos_dict_obstacle[key][0]), pos_dict_obstacle[key][1], pos_dict_obstacle[key][2]), ObstacleImage.A))
    #print('adjusted pos_dict_obstacle', pos_dict_obstacle)
    return ARENAS

# # old arena obstacle values:
# arena0.add_obstacle(Obstacle(CellPosition(18, 6, Facing.LEFT), ObstacleImage.A))
# arena0.add_obstacle(Obstacle(CellPosition(14, 1, Facing.UP), ObstacleImage.B))
# arena0.add_obstacle(Obstacle(CellPosition(5, 13, Facing.DOWN), ObstacleImage.C))
# arena0.add_obstacle(Obstacle(CellPosition(17, 19, Facing.DOWN), ObstacleImage.LEFT))
# arena0.add_obstacle(Obstacle(CellPosition(8, 17, Facing.RIGHT), ObstacleImage.ONE))



    
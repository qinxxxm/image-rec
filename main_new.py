from path_getter import returnPath
from mdp_python_algo.robot_pathfinder.config.constants import Facing

pos_dict_full = {1: [18,6,Facing.LEFT], 2:[14,1,Facing.UP], 3:[5,13,Facing.DOWN],4:[17,19,Facing.DOWN],5:[8,17,Facing.RIGHT],'ROBOT':[1,1,Facing.UP]}
returnPath(pos_dict_full)
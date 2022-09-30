from path_getter import returnPath
from mdp_python_algo.robot_pathfinder.config.constants import Facing

# pos_dict_full = {'ROBOT':[1,1,Facing.UP],'1': [18,6,Facing.LEFT], '2':[14,1,Facing.UP], '3':[5,13,Facing.DOWN],'4':[17,19,Facing.DOWN],'5':[8,17,Facing.RIGHT]}
pos_dict_full = {'ROBOT':[0,0,Facing.UP],'1': [18,6,Facing.LEFT], '2':[14,0,Facing.UP], '3':[5,13,Facing.DOWN],'4':[17,19,Facing.DOWN],'5':[8,17,Facing.RIGHT]}

rd = returnPath(pos_dict_full)
print(rd)
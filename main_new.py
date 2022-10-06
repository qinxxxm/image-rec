from path_getter import returnPath
from mdp_python_algo.robot_pathfinder.config.constants import Facing
# import json

pos_dict_full = {'ROBOT':[1,1,Facing.UP], '1':[7,14,Facing.LEFT],'2':[5,9,Facing.DOWN], '3':[12,9,Facing.RIGHT],'4':[15,15,Facing.DOWN],'5':[15,4,Facing.LEFT],'6':[1,10,Facing.UP]}

rd = returnPath(pos_dict_full)
# print(type(rd))
# for i in rd:
#     print(type(i))

# # Serializing json
# json_object = json.dumps(rd)
 
# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
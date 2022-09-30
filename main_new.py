from path_getter import returnPath
from mdp_python_algo.robot_pathfinder.config.constants import Facing
import json

pos_dict_full = {'ROBOT':[1,1,Facing.UP],'1': [18,6,Facing.LEFT], '2':[14,1,Facing.UP], '3':[5,13,Facing.DOWN],'4':[17,19,Facing.DOWN],'5':[8,17,Facing.RIGHT]}

rd = returnPath(pos_dict_full)
print(type(rd))
for i in rd:
    print(type(i))

# Serializing json
json_object = json.dumps(rd)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
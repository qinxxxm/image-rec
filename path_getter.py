from mdp_python_algo.robot_pathfinder import main

def returnPath(pos_dict_full):
    args = main.parse_args()
    # commands_dict = main.run_simulator(args)
    commands_dict = main.run_simulator_return_commands_dict(args,pos_dict_full)

    print("returned commands_dict", commands_dict)
    return commands_dict

    # format of receiving obstacle pos and robot pos  
    # {1：[x, y, NSEW], ROBOT: []}

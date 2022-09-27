from mdp_python_algo.robot_pathfinder import main

def returnPath():
    args = main.parse_args()
    commands_dict = main.run_simulator(args)
    print("returned commands_dict", commands_dict)
    return commands_dict
"""
pathfinder should be isolated from simulator
"""
from ctypes import sizeof
from re import X
from mdp_python_algo.robot_pathfinder.models.arena import Arena
from mdp_python_algo.robot_pathfinder.models.board import Board
from mdp_python_algo.robot_pathfinder.models.command import Command
import itertools
import time
from mdp_python_algo.robot_pathfinder.models.robot import Robot
from mdp_python_algo.robot_pathfinder.utils.math_utils import dist_pos
from mdp_python_algo.robot_pathfinder.algorithm.simple_hybrid_astar import run_simple_hybrid_astar




def compute_simple_hamiltonian_path(arena: Arena, robot: Robot):
    # TODO: switch heuristic to simple hybrid astar
    # TODO: another option is to switch to variable distance
    permutations = tuple(itertools.permutations(arena.obstacles))
    
    def path_distance(path):
        nodes = [robot.cell_pos.cell_pos2d()] + [obstacle.cell_pos.cell_pos2d() for obstacle in path]
        dist = 0
        for i in range(len(nodes) - 1):
            dist += dist_pos(nodes[i], nodes[i + 1])
        return dist
    
    return min(permutations, key=path_distance)

def plan_paths(arena: Arena, robot: Robot):
    # start = time.time()
    print("raw obsticals\n", arena.obstacles)
    simple_hamiltonian_path = compute_simple_hamiltonian_path(arena, robot)
    print('Found hamiltonian path',simple_hamiltonian_path)
    order = list()
    for i in simple_hamiltonian_path:
        count = 1
        for j in arena.obstacles:
            if (i!=j):
                count+=1
            else:
                order.append(count)
            
        
    print("order=",order)

    last_cell = robot.cell_pos
    
    commands = list()
    # commands_dict returns a dictionary of movements
    commands_dict = {}
    commands_index = 1

    for obstacle in simple_hamiltonian_path:
        board = Board.from_arena(arena)
        next_cell = obstacle.get_target_position()
        board.start = board.nodes[last_cell.cell_y][last_cell.cell_x][last_cell.facing]
        board.goal = board.nodes[next_cell.cell_y][next_cell.cell_x][next_cell.facing]
        run_simple_hybrid_astar(board)

        # convert Command Object to string and put in commands_dict
        commands_list = get_path(board)[:-1]
        commands_list_str = list()
        x=0
        for i in commands_list:
            # print(i)
            # if str(i) =="l180":
            #     commands_list_str.append("l090")
            #     commands_list_str.append("l090")
            # elif str(i) =="r180":
            #     commands_list_str.append("r090")
            #     commands_list_str.append("r090")
            # elif str(i) =="m180":
            #     commands_list_str.append("m090")
            #     commands_list_str.append("m090")
            # elif str(i) =="o180":
            #     commands_list_str.append("o090")
            #     commands_list_str.append("o090")
            # else:
            #     commands_list_str.append(str(i))
            commands_list_str.append(str(i))
        commands_list_str
        commands_dict[order[commands_index-1]] = commands_list_str
        commands_index += 1
        commands.extend(get_path(board))
        last_cell = next_cell
    
    # end = time.time()
    print('Done path planning')
    # print(f'Total time consumed: {(end - start):.2f} seconds')
    print(commands)
    # print(commands_dict)
    return commands, commands_dict
def get_path(board):
    if not board.goal.close:
        return
    node = board.goal
    commands = list()
    command = None
    while node.predecessor is not None:
        if command is None or command.move != node.move:
            command = Command(node.move)
            commands.append(command)
        else:
            command.inc_repeat()
        node = node.predecessor
    
    # Add take pic char
    commands.reverse()
    commands.append('snap')
    # print(commands)
    return commands

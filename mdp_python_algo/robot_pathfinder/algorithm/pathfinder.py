"""
pathfinder should be isolated from simulator
"""
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
    simple_hamiltonian_path = compute_simple_hamiltonian_path(arena, robot)
    print('Found hamiltonian path')
    print(simple_hamiltonian_path)
    
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
        _,commands_dict[commands_index] = get_path(board)
        commands_index += 1
        commands.extend(get_path(board))
        last_cell = next_cell
    
    # end = time.time()
    print('Done path planning')
    # print(f'Total time consumed: {(end - start):.2f} seconds')
    print(commands)
    print(commands_dict)
    return commands, commands_dict

def get_path(board):
    if not board.goal.close:
        return
    node = board.goal
    commands = list()
    command = None
    commands_str = list()
    while node.predecessor is not None:
        if command is None or command.move != node.move:
            command = Command(node.move)
            commands.append(command)
            command_str = str(command)
            commands_str.append(command_str)
        else:
            command.inc_repeat()
        node = node.predecessor
    
    # Add take pic char
    commands.reverse()
    commands_str.reverse()
    print(command_str)
    commands.append('snap')
    print(commands)
    return commands, commands_str

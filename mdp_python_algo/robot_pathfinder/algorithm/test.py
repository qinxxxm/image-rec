from models.arena import Arena
from models.board import Board
from models.command import Command
import itertools
import time
from models.robot import Robot
from utils.math_utils import dist_pos
from algorithm.simple_hybrid_astar import run_simple_hybrid_astar


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

simple_hamiltonian_path = compute_simple_hamiltonian_path(arena, robot)

last_cell = robot.cell_pos

commands_dict = {}
commands_index = 0
for obstacle in simple_hamiltonian_path:
    board = Board.from_arena(arena)
    next_cell = obstacle.get_target_position()
    board.start = board.nodes[last_cell.cell_y][last_cell.cell_x][last_cell.facing]
    board.goal = board.nodes[next_cell.cell_y][next_cell.cell_x][next_cell.facing]
    run_simple_hybrid_astar(board)
    commands_dict[commands_index] = get_path(board)
    commands_index += 1
    last_cell = next_cell

print(commands_dict)
import pygame

from mdp_python_algo.robot_pathfinder.algorithm.pathfinder import plan_paths
from mdp_python_algo.robot_pathfinder.config.constants import SimulatorConst


def handle_events_display_default_map(simulator, events):
    # for event in events:
    #     if event.type == pygame.MOUSEBUTTONDOWN:
            print('Start path planning')
            simulator.mode = SimulatorConst.MODE_FIND_PATH
            simulator.commands, commands_dict = plan_paths(simulator.arena, simulator.robot)
            # TODO: run path planning in a separate thread
            return commands_dict



def draw_display_default_map(simulator):
    pass

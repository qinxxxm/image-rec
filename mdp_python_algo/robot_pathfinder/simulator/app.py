
import pygame
import sys
from mdp_python_algo.robot_pathfinder.utils.log_utils import print_warning, print_error
from mdp_python_algo.robot_pathfinder.utils.position_utils import cellx_winx, celly_winy
from mdp_python_algo.robot_pathfinder.config.set_arena import set_arena
from mdp_python_algo.robot_pathfinder.config.set_robot import set_robot
from mdp_python_algo.robot_pathfinder.config.constants import Facing
from mdp_python_algo.robot_pathfinder.config.constants import Color, RobotConst
from mdp_python_algo.robot_pathfinder.config.constants import SimulatorConst
from mdp_python_algo.robot_pathfinder.simulator.manage.show_default_map import draw_display_default_map, handle_events_display_default_map
from mdp_python_algo.robot_pathfinder.simulator.manage.show_result import handle_events_display_result
from mdp_python_algo.robot_pathfinder.simulator.manage.find_path import handle_events_find_path
from mdp_python_algo.robot_pathfinder.simulator.manage.customize_map import draw_customize_map, handle_events_customize_map
from mdp_python_algo.robot_pathfinder.simulator.manage.show_animation import handle_events_display_animation
from mdp_python_algo.robot_pathfinder.simulator.view.arena_view import draw_arena
from mdp_python_algo.robot_pathfinder.simulator.view.robot_view import draw_robot, RobotView, RobotViewCommand
from mdp_python_algo.robot_pathfinder.models.command import Command
from mdp_python_algo.robot_pathfinder.models.robot import Robot
from mdp_python_algo.robot_pathfinder.models.arena import Arena
from mdp_python_algo.robot_pathfinder.models.cell_position import CellPosition



class Simulator:
    
    def __init__(self):
        print('Initializing simulator')
        
        # UI attributes
        self.running = False
        self.surface = None
        self.clock = None
        self.mode = SimulatorConst.MODE_NULL
        
        # algorithm attributes
        self.arena = None
        self.robot = None
        self.command = None
        self.commands = None
        self.robot_view = None
        
    def init_map(self, map_index, pos_dict_full):
        print('Loading map to pygame')
        print(f'User choice is {map_index}')
        #here ger the arena value from pos_dict_full
        ARENAS = set_arena(pos_dict_full)
        if map_index == -1:
            print('Default map is not loaded, waiting for user input')
            self.mode = SimulatorConst.MODE_CUSTOMIZE_MAP
        elif map_index < 0 or len(ARENAS) <= map_index:
            print_warning('Invalid default map, switching to customize mode')
            self.mode = SimulatorConst.MODE_CUSTOMIZE_MAP
        else:
            self.arena = ARENAS[map_index]
            self.mode = SimulatorConst.MODE_DISPLAY_DEFAULT_MAP
    def draw(self):
        if not self.running or self.mode == SimulatorConst.MODE_NULL:
            # this line shouldn't be reached
            print_error('ERROR: drawing while pygame is not running')
            sys.exit(1)
        
        self.surface.fill(Color.WHITE)
        draw_arena(self)
        
        if self.mode == SimulatorConst.MODE_DISPLAY_DEFAULT_MAP:
            draw_display_default_map(self)
        elif self.mode == SimulatorConst.MODE_CUSTOMIZE_MAP:
            draw_customize_map(self)
        elif self.mode == SimulatorConst.MODE_FIND_PATH:
            pass
        elif self.mode == SimulatorConst.MODE_DISPLAY_ANIMATION:
            pass
        elif self.mode == SimulatorConst.MODE_DISPLAY_RESULT:
            pass
        else:
            # this line shouldn't be reached
            print_error('ERROR: invalid simulator mode')
            sys.exit(1)
        
        draw_robot(self)
        
        pygame.display.flip()        
    def init_display(self, pos_dict_full):
        print('Initializing pygame')
        
        # UI
        pygame.init()
        self.running = True
        self.surface = pygame.display.set_mode(SimulatorConst.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        
        # algorithm
        self.arena = Arena()
        # here get the robot pos from pos_dict_robot
        pos_dict_robot = set_robot(pos_dict_full)
        robot_start_x = pos_dict_robot[0][0]
        robot_start_y = pos_dict_robot[0][1]
        robot_start_facing = pos_dict_robot[0][2]
        if robot_start_facing == Facing.UP:
            robot_start_theta = 90
        elif robot_start_facing == Facing.RIGHT:
            robot_start_theta = 0
        elif robot_start_facing == Facing.LEFT:
            robot_start_theta = 180
        elif robot_start_facing ==Facing.DOWN:
            robot_start_theta = 270
        self.robot = Robot(CellPosition(robot_start_x, robot_start_y, robot_start_facing))
        self.command = None
        self.commands = list()
        self.robot_view = \
            RobotView(cellx_winx(robot_start_x), celly_winy(robot_start_y), robot_start_theta)
    def tick(self):
        if not self.running or self.mode == SimulatorConst.MODE_NULL or self.clock is None:
            # this line shouldn't be reached
            print_error('ERROR: clock ticking while pygame is not running')
            sys.exit(1)
        
        self.clock.tick(SimulatorConst.FRAMES_PER_SECOND)
        
        assert SimulatorConst.FRAMES_PER_SECOND / SimulatorConst.ROBOT_SPEED
        
        if self.command is None and self.commands is not None and 0 < len(self.commands):
            command = self.commands.pop(0)
            if not isinstance(command, Command):
                [self.clock.tick(SimulatorConst.FRAMES_PER_SECOND) for _ in range(SimulatorConst.FRAMES_PER_SECOND)]
                return
                
            self.command = RobotViewCommand(command, self.robot_view)
        
        if self.command is not None:
            self.command = self.command.forward()    
    def handle_events(self):
        if not self.running or self.mode == SimulatorConst.MODE_NULL:
            # this line shouldn't be reached
            print_error('ERROR: handling events while pygame is not running')
            sys.exit(1)
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                self.mode = SimulatorConst.MODE_NULL
                pygame.quit()
                print('QUIT button is clicked')
                print('Quitting pygame')
                return
        
        if self.mode == SimulatorConst.MODE_DISPLAY_DEFAULT_MAP:
            # handle_events_display_default_map(self, events)
            commands_dict = handle_events_display_default_map(self, events)
            return commands_dict
        elif self.mode == SimulatorConst.MODE_CUSTOMIZE_MAP:
            handle_events_customize_map(self, events)
        elif self.mode == SimulatorConst.MODE_FIND_PATH:
            handle_events_find_path(self, events)
        elif self.mode == SimulatorConst.MODE_DISPLAY_ANIMATION:
            handle_events_display_animation(self, events)
        elif self.mode == SimulatorConst.MODE_DISPLAY_RESULT:
            handle_events_display_result(self, events)
        else:
            # this line shouldn't be reached
            print_error('ERROR: invalid simulator mode')
            sys.exit(1)

    



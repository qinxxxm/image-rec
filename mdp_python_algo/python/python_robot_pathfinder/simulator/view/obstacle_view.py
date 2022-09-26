import os
import sys
import pygame
from utils.log_utils import print_warning
from config.constants import SimulatorConst, Facing
from models.obstacle import Obstacle
from tkinter import S

def draw_obstacle(simulator, obstacle: Obstacle):
    win_x, win_y = obstacle.cell_pos.win_pos()

    # draw the image
    image = pygame.image.load(os.path.join('assets', f'{obstacle.image.name}.png'))
    image = pygame.transform.scale(image, (SimulatorConst.WINDOW_CELL_WIDTH, SimulatorConst.WINDOW_CELL_HEIGHT))
    image_rect = image.get_rect()
    image_rect.center = win_x, win_y
    simulator.surface.blit(image, image_rect)

    # # draw red dot to represent obstacle facing (works, but not used) (replaced by bar)
    # dot_x, dot_y = win_x, win_y
    # if obstacle.cell_pos.facing == Facing.RIGHT:
    #     dot_x += SimulatorConst.OBSTACLE_CIRCLE_OFFSET_X
    # elif obstacle.cell_pos.facing == Facing.UP:
    #     dot_y -= SimulatorConst.OBSTACLE_CIRCLE_OFFSET_Y
    # elif obstacle.cell_pos.facing == Facing.LEFT:
    #     dot_x -= SimulatorConst.OBSTACLE_CIRCLE_OFFSET_X
    # elif obstacle.cell_pos.facing == Facing.DOWN:
    #     dot_y += SimulatorConst.OBSTACLE_CIRCLE_OFFSET_Y
    # else:
    #     # this line shouldn't be reached
    #     print_warning('ERROR: attempting to draw obstacle with no facing')
    #     sys.exit(1)
    
    # pygame.draw.circle(simulator.surface, SimulatorConst.OBSTACLE_CIRCLE_COLOR, (dot_x, dot_y), SimulatorConst.OBSTACLE_CIRCLE_RADIUS)

    # draw bar to represent obstacle facing
    topleft_x = win_x- SimulatorConst.WINDOW_CELL_WIDTH_RADIUS
    topleft_y = win_y - SimulatorConst.WINDOW_CELL_HEIGHT_RADIUS
    cell_w = SimulatorConst.WINDOW_CELL_WIDTH
    cell_h = SimulatorConst.WINDOW_CELL_HEIGHT
   
    rect_x, rect_y = win_x, win_y

    if obstacle.cell_pos.facing == Facing.UP:
        rect_x = topleft_x
        rect_y = topleft_y
        obstacle_bar_rect = pygame.Rect((rect_x, rect_y), (cell_w, SimulatorConst.OBSTACLE_BAR_THICKNESS))        
    elif obstacle.cell_pos.facing == Facing.DOWN:
        rect_x = topleft_x
        rect_y += SimulatorConst.WINDOW_CELL_HEIGHT_RADIUS - SimulatorConst.OBSTACLE_BAR_THICKNESS
        obstacle_bar_rect = pygame.Rect((rect_x, rect_y), (cell_w, SimulatorConst.OBSTACLE_BAR_THICKNESS))    
    elif obstacle.cell_pos.facing == Facing.LEFT:
        rect_x = topleft_x
        rect_y = topleft_y
        obstacle_bar_rect = pygame.Rect((rect_x, rect_y), (SimulatorConst.OBSTACLE_BAR_THICKNESS, cell_h))
    elif obstacle.cell_pos.facing == Facing.RIGHT:
        rect_x += SimulatorConst.WINDOW_CELL_WIDTH_RADIUS - SimulatorConst.OBSTACLE_BAR_THICKNESS
        rect_y -= SimulatorConst.WINDOW_CELL_HEIGHT_RADIUS
        obstacle_bar_rect = pygame.Rect((rect_x, rect_y), (SimulatorConst.OBSTACLE_BAR_THICKNESS, cell_h))
    else:
        # this line shouldn't be reached
        print_warning('ERROR: attempting to draw obstacle with no facing')
        sys.exit(1)

    pygame.draw.rect(simulator.surface, SimulatorConst.OBSTACLE_BAR_COLOR, obstacle_bar_rect)


def draw_obstacles(simulator):
    for obstacle in simulator.arena.obstacles:
        draw_obstacle(simulator, obstacle)

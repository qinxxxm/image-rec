import pygame

from config.constants import ArenaConst, SimulatorConst
from simulator.view.obstacle_view import draw_obstacles


def draw_arena(simulator):
    start_zone_rect = pygame.Rect(0,480,SimulatorConst.WINDOW_CELL_WIDTH*4,120)
    pygame.draw.rect(simulator.surface, SimulatorConst.START_COLOR, start_zone_rect)
    for i in range(ArenaConst.NUM_COLS):
        pygame.draw.line(
            simulator.surface,
            SimulatorConst.CELL_BORDER_LINE_COLOR,
            (i * SimulatorConst.WINDOW_CELL_WIDTH, 0),
            (i * SimulatorConst.WINDOW_CELL_WIDTH, SimulatorConst.WINDOW_HEIGHT),
            SimulatorConst.CELL_BORDER_LINE_WIDTH
        )
    for i in range(ArenaConst.NUM_ROWS):
        pygame.draw.line(
            simulator.surface,
            SimulatorConst.CELL_BORDER_LINE_COLOR,
            (0, i * SimulatorConst.WINDOW_CELL_HEIGHT),
            (SimulatorConst.WINDOW_WIDTH, i * SimulatorConst.WINDOW_CELL_HEIGHT),
            SimulatorConst.CELL_BORDER_LINE_WIDTH
        )
        # num_rect = pygame.Rect(0,i,SimulatorConst.WINDOW_CELL_WIDTH,SimulatorConst.WINDOW_CELL_HEIGHT)
        # pygame.draw.rect(simulator.surface, SimulatorConst.START_COLOR, num_rect)

        # # green border for the arena
        # pygame.draw.rect(
        # 	simulator.surface,
        # 	SimulatorConst.ARENA_BORDER_LINE_COLOR,
        # 	pygame.Rect(0, 0, SimulatorConst.WINDOW_WIDTH, SimulatorConst.WINDOW_WIDTH),
        # 	SimulatorConst.ARENA_BORDER_LINE_WIDTH
        # )

    # draw x and y axes with numbers
    font = pygame.font.Font('FreeSans.ttf', 10)
    
    for i in range(ArenaConst.NUM_COLS):
        text = font.render(str(19-i), True, SimulatorConst.AXES_COLOR)
        textRect = text.get_rect()
        textRect.center = (SimulatorConst.WINDOW_CELL_WIDTH_RADIUS / 2, i*SimulatorConst.WINDOW_CELL_HEIGHT + SimulatorConst.WINDOW_CELL_HEIGHT_RADIUS)
        simulator.surface.blit(text, textRect)
   
    for i in range(ArenaConst.NUM_ROWS):
        text = font.render(str(i), True, SimulatorConst.AXES_COLOR)
        textRect = text.get_rect()
        textRect.center = (i*SimulatorConst.WINDOW_CELL_WIDTH + SimulatorConst.WINDOW_CELL_WIDTH_RADIUS, SimulatorConst.WINDOW_HEIGHT - SimulatorConst.WINDOW_CELL_HEIGHT_RADIUS / 2)
        simulator.surface.blit(text, textRect)

    draw_obstacles(simulator)

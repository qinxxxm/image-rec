from enum import Enum, IntEnum
import math

class LineDirection(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1

class Color:

    RED = (127, 0, 0)
    ORANGE = (255,128,0)
    YELLOW = (255,255,0)
    GREEN = (0, 127, 0)
    BLUE = (90, 150, 220)
    BLUE_LIGHT = (170, 200, 240)
    MAGENTA = (255,0,255)
    WHITE = (255, 255, 255)
    GREY = (127, 127, 127)
    BLACK = (0, 0, 0)

class Facing(IntEnum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

class Moves(IntEnum):
    l = 0
    f = 1
    r = 2
    m = 3
    b = 4
    o = 5

class ArenaConst: #in cm
    ARENA_WIDTH = 200
    ARENA_HEIGHT = 200 
    CELL_WIDTH = 10 
    CELL_HEIGHT = 10
    NUM_ROWS = 20
    NUM_COLS = 20
    
    VIRTUAL_OBSTACLE_RADIUS = 1
    DETECT_CELL_DISTANCE = 3

class ObstacleImage(Enum):
    ONE = 11
    TWO = 12
    THREE = 13
    FOUR = 14
    FIVE = 15
    SIX = 16
    SEVEN = 17
    EIGHT = 18
    NINE = 19
    A = 20
    B = 21
    C = 22
    D = 23
    E = 24
    F = 25
    G = 26
    H = 27
    S = 28
    T = 29 
    U = 30
    V = 31
    W = 32
    X = 33
    Y = 34
    Z = 35
    UP = 36
    DOWN = 37
    RIGHT = 38
    LEFT = 39
    STOP = 40

class RobotConst:    
    WIDTH = 25
    HEIGHT = 20
# robot x, y ,facing, theta are obsolete. replaced by value in pos_dict_robot
    # START_X = 1
    # START_Y = 1
    # START_FACING = Facing.UP
    # START_THETA = 90

    MOVES_PENALTY = [
        3.5,  # l
        1.0,  # f
        3.5,  # r
        6.0,  # m
        2.0,  # b
        6.0,  # o
    ]
    
    CHANGE_MOVES_PENALTY = 1.5
    
    MOVES_FUNC_DXY = [
        [
            (lambda r, s, t: r * math.sin(s * t), lambda r, s, t: r * math.cos(s * t) - r),
            (lambda r, s, t: r * math.cos(s * t) - r, lambda r, s, t: -r * math.sin(s * t)),
            (lambda r, s, t: -r * math.sin(s * t), lambda r, s, t: r - r * math.cos(s * t)),
            (lambda r, s, t: r - r * math.cos(s * t), lambda r, s, t: r * math.sin(s * t)),
        ],
        [
            (lambda r, s, t: s * t, lambda r, s, t: 0),
            (lambda r, s, t: 0, lambda r, s, t: -s * t),
            (lambda r, s, t: -s * t, lambda r, s, t: 0),
            (lambda r, s, t: 0, lambda r, s, t: s * t),
        ],
        [
            (lambda r, s, t: r * math.sin(s * t), lambda r, s, t: r - r * math.cos(s * t)),
            (lambda r, s, t: r - r * math.cos(s * t), lambda r, s, t: -r * math.sin(s * t)),
            (lambda r, s, t: -r * math.sin(s * t), lambda r, s, t: r * math.cos(s * t) - r),
            (lambda r, s, t: r * math.cos(s * t) - r, lambda r, s, t: r * math.sin(s * t)),
        ],
        [
            (lambda r, s, t: -r * math.sin(s * t), lambda r, s, t: r * math.cos(s * t) - r),
            (lambda r, s, t: r * math.cos(s * t) - r, lambda r, s, t: r * math.sin(s * t)),
            (lambda r, s, t: r * math.sin(s * t), lambda r, s, t: r - r * math.cos(s * t)),
            (lambda r, s, t: r - r * math.cos(s * t), lambda r, s, t: -r * math.sin(s * t)),
        ],
        [
            (lambda r, s, t: -s * t, lambda r, s, t: 0),
            (lambda r, s, t: 0, lambda r, s, t: s * t),
            (lambda r, s, t: s * t, lambda r, s, t: 0),
            (lambda r, s, t: 0, lambda r, s, t: -s * t),
        ],
        [
            (lambda r, s, t: -r * math.sin(s * t), lambda r, s, t: r - r * math.cos(s * t)),
            (lambda r, s, t: r - r * math.cos(s * t), lambda r, s, t: r * math.sin(s * t)),
            (lambda r, s, t: r * math.sin(s * t), lambda r, s, t: r * math.cos(s * t) - r),
            (lambda r, s, t: r * math.cos(s * t) - r, lambda r, s, t: -r * math.sin(s * t)),
        ],
    ]
    
    MOVES_SIGN_T = [1, 0, -1, -1, 0, 1]
    
    # MOVES_DXY[moves][facing]
    MOVES_DXY = [
        [(2, 2), (-2, 2), (-2, -2), (2, -2)],
        [(1, 0), (0, 1), (-1, 0), (0, -1)],
        [(2, -2), (2, 2), (-2, 2), (-2, -2)],
        [(-2, 2), (-2, -2), (2, -2), (2, 2)],
        [(-1, 0), (0, -1), (1, 0), (0, 1)],
        [(-2, -2), (2, -2), (2, 2), (-2, 2)]
    ]
    
    MOVES_VALID_CHECK_DXY = [
        [[(1, 0), (2, 0), (2, 1), (2, 2)],
         [(0, 1), (0, 2), (-1, 2), (-2, 2)],
         [(-1, 0), (-2, 0), (-2, -1), (-2, -2)],
         [(0, -1), (0, -2), (1, -2), (2, -2)]],
        [[(1, 0)],
         [(0, 1)],
         [(-1, 0)],
         [(0, -1)]],
        [[(1, 0), (2, 0), (2, -1), (2, -2)],
         [(0, 1), (0, 2), (1, 2), (2, 2)],
         [(-1, 0), (-2, 0), (-2, 1), (-2, 2)],
         [(0, -1), (0, -2), (-1, -2), (-2, -2)]],
        [[(-1, 0), (-2, 0), (-2, 1), (-2, 2)],
         [(0, -1), (0, -2), (-1, -2), (-2, -2)],
         [(1, 0), (2, 0), (2, -1), (2, -2)],
         [(0, 1), (0, 2), (1, 2), (2, 2)]],
        [[(-1, 0)],
         [(0, -1)],
         [(1, 0)],
         [(0, 1)]],
        [[(-1, 0), (-2, 0), (-2, -1), (-2, -2)],
         [(0, -1), (0, -2), (1, -2), (2, -2)],
         [(1, 0), (2, 0), (2, 1), (2, 2)],
         [(0, 1), (0, 2), (-1, 2), (-2, 2)]],
    ]
    
    MOVES_NEXT_FACING = [
        [Facing.UP, Facing.LEFT, Facing.DOWN, Facing.RIGHT],
        [Facing.RIGHT, Facing.UP, Facing.LEFT, Facing.DOWN],
        [Facing.DOWN, Facing.RIGHT, Facing.UP, Facing.LEFT],
        [Facing.DOWN, Facing.RIGHT, Facing.UP, Facing.LEFT],
        [Facing.RIGHT, Facing.UP, Facing.LEFT, Facing.DOWN],
        [Facing.UP, Facing.LEFT, Facing.DOWN, Facing.RIGHT],
    ]


class SimulatorConst:
    # UI constants
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    WINDOW_CELL_WIDTH = WINDOW_WIDTH / ArenaConst.NUM_COLS
    WINDOW_CELL_HEIGHT = WINDOW_HEIGHT / ArenaConst.NUM_ROWS
    WINDOW_CELL_SIZE = (WINDOW_CELL_WIDTH, WINDOW_CELL_HEIGHT)
    WINDOW_CELL_WIDTH_RADIUS = WINDOW_CELL_WIDTH / 2
    WINDOW_CELL_HEIGHT_RADIUS = WINDOW_CELL_HEIGHT / 2
    WINDOW_IMAGE_WIDTH = WINDOW_CELL_WIDTH / 2
    WINDOW_IMAGE_HEIGHT = WINDOW_CELL_HEIGHT / 2
    WINDOW_IMAGE_SIZE = (WINDOW_IMAGE_WIDTH, WINDOW_IMAGE_HEIGHT)
    WINDOW_IMAGE_WIDTH_RADIUS = WINDOW_IMAGE_WIDTH / 2
    WINDOW_IMAGE_HEIGHT_RADIUS = WINDOW_IMAGE_HEIGHT / 2
    WINDOW_SCALE_X = WINDOW_WIDTH / ArenaConst.ARENA_WIDTH
    WINDOW_SCALE_Y = WINDOW_HEIGHT / ArenaConst.ARENA_HEIGHT
    # WINDOW_ROBOT_OBSTACLE_CENTER_SAFE_DISTANCE = ArenaConst.ROBOT_OBSTACLE_CENTER_SAFE_DISTANCE * WINDOW_SCALE_X
    
    ROBOT_WIDTH = RobotConst.WIDTH * WINDOW_SCALE_X
    ROBOT_HEIGHT = RobotConst.HEIGHT * WINDOW_SCALE_Y
    
    ROBOT_SPEED = WINDOW_CELL_WIDTH * 5  # pixels per second
    ROBOT_TURN_RADIUS = 2 * WINDOW_CELL_WIDTH
    
    FRAMES_PER_SECOND = 10
    
    ARENA_BORDER_LINE_WIDTH = 4
    ARENA_BORDER_LINE_COLOR = Color.GREEN
    
    CELL_BORDER_LINE_WIDTH = 2
    CELL_BORDER_LINE_COLOR = Color.BLUE_LIGHT
    
    # dot to represent obstacle faing
    OBSTACLE_CIRCLE_COLOR = Color.MAGENTA
    OBSTACLE_CIRCLE_RADIUS = 3
    OBSTACLE_CIRCLE_OFFSET_X = WINDOW_CELL_WIDTH_RADIUS - OBSTACLE_CIRCLE_RADIUS - CELL_BORDER_LINE_WIDTH
    OBSTACLE_CIRCLE_OFFSET_Y = WINDOW_CELL_HEIGHT_RADIUS - OBSTACLE_CIRCLE_RADIUS - CELL_BORDER_LINE_WIDTH
    
    # bar to represent obstacle facing
    OBSTACLE_BAR_COLOR = Color.MAGENTA
    OBSTACLE_BAR_THICKNESS = 5

    AXES_COLOR = Color.BLACK

    OBSTACLE_BORDER_LINE_WIDTH = 4
    OBSTACLE_BORDER_LINE_COLOR = Color.RED

    START_COLOR = Color.BLUE
    
    # logic constants
    MODE_NULL = -1
    MODE_DISPLAY_DEFAULT_MAP = 0
    MODE_CUSTOMIZE_MAP = 1
    MODE_FIND_PATH = 2
    MODE_DISPLAY_ANIMATION = 3
    MODE_DISPLAY_RESULT = 4

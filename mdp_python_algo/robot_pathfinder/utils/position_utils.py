"""
Conversion among pos, win_pos, cell_pos
pos is a float representing the position of a point on the actual arena with origin at bottom-left
win_pos is a float representing the position of a point on the simulator with origin at top-left
cell_pos is an int representing the position of a cell on the arena board with origin at bottom-left
"""
from mdp_python_algo.robot_pathfinder.config.constants import ArenaConst, SimulatorConst, Facing
from typing import Tuple

def x_winx(x: float) -> float:
    return x * SimulatorConst.WINDOW_SCALE_X

def y_winy(y: float) -> float:
    return SimulatorConst.WINDOW_HEIGHT - (y * SimulatorConst.WINDOW_SCALE_Y)

def winx_x(win_x: float) -> float:
    return win_x / SimulatorConst.WINDOW_SCALE_X

def winy_y(win_y: float) -> float:
    return (SimulatorConst.WINDOW_HEIGHT - win_y) / SimulatorConst.WINDOW_SCALE_Y

def pos_winpos(pos: Tuple[float, float]) -> Tuple[float, float]:
    return x_winx(pos[0]), y_winy(pos[1])

def winpos_pos(win_pos: Tuple[float, float]) -> Tuple[float, float]:
    return winx_x(win_pos[0]), winy_y(win_pos[1])

def x_cellx(x: float) -> int:
    return x // ArenaConst.CELL_WIDTH

def cellx_x(cell_x: int) -> float:
    """returns the center of the cell"""
    return cell_x * ArenaConst.CELL_WIDTH + ArenaConst.CELL_WIDTH / 2

def winx_cellx(win_x: float) -> int:
    return x_cellx(winx_x(win_x))

def cellx_winx(cell_x: int) -> float:
    return x_winx(cellx_x(cell_x))

def y_celly(y: float) -> int:
    return y // ArenaConst.CELL_HEIGHT

def celly_y(cell_y: int) -> float:
    """returns the center of the cell"""
    return cell_y * ArenaConst.CELL_HEIGHT + ArenaConst.CELL_HEIGHT / 2

def pos_cellpos(pos: Tuple[float, float]) -> Tuple[int, int]:
    return x_cellx(pos[0]), y_celly(pos[1])

def wint_celly(win_y: float) -> int:
    return y_celly(winy_y(win_y))

def celly_winy(cell_y: int) -> float:
    return y_winy(celly_y(cell_y))

def cellpos_pos(cell_pos: Tuple[int, int]) -> Tuple[float, float]:
    """returns the center of the cell"""
    return cellx_x(cell_pos[0]), celly_y(cell_pos[1])

def winpos_cellpos(win_pos: Tuple[float, float]) -> Tuple[int, int]:
    return pos_cellpos(winpos_pos(win_pos))

def cellpos_winpos(cell_pos: Tuple[int, int]) -> Tuple[float, float]:
    return cellx_winx(cell_pos[0]), celly_winy(cell_pos[1])

def theta_to_facing(theta: float) -> Facing:
    if 45 < theta <= 135:
        return Facing.UP
    elif -45 < theta <= 45:
        return Facing.RIGHT
    elif -135 < theta <= -45:
        return Facing.DOWN
    return Facing.LEFT

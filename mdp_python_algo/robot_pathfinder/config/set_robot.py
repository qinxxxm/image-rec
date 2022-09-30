def set_robot(pos_dict_full):
    pos_dict_robot = {}
    pos_dict_robot[0] = pos_dict_full.get('ROBOT')

    # error handling for x, y value that falls on the boarder
    if pos_dict_robot[0][0] == 0:
        pos_dict_robot[0][0] = 1
    if pos_dict_robot[0][1] == 0:
        pos_dict_robot[0][1] = 1
        
    # print('pos_dict_robot: ',pos_dict_robot)
    return pos_dict_robot

def set_robot(pos_dict_full):
    pos_dict_robot = {}
    pos_dict_robot[0] = pos_dict_full.get('ROBOT')
    print('pos_dict_robot: ',pos_dict_robot)
    return pos_dict_robot

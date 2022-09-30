from mdp_python_algo.robot_pathfinder.config.constants import Moves

"""
l = 0
f = 1
r = 2
m = 3
b = 4
o = 5
"""
# Take picture symbol
TAKE_PICTURE = 'snap'


def compress_instructions(instruction_list: list):
    print("Compressing Instructions!")
    str = ""
    count = 1
    pre = instruction_list[0]
    for i in range(1, len(instruction_list)):
        if pre == instruction_list[i]:
            count += 1
        
        else:
            str = (str + f"{pre}/") if pre == TAKE_PICTURE else (str + f"{pre},{count}/")
            count = 1
            pre = instruction_list[i]
    
    # Append no more instructions
    str += "!"
    
    return str

def find_object_face():
    # Scan, Move back 3x, Turn right, Forward, TL * 2
    iList = ["snap"] + [Moves.b] * 3 + [Moves.r] + [Moves.f] + [Moves.l] * 2
    return compress_instructions(iList * 4)

def commands_to_message(commands: list):
    index = 0
    str = ""
    while (index < len(commands)):
        str = str + f"{commands[index].move},{commands[index].repeat}/" if commands[index] != TAKE_PICTURE else str + f"{TAKE_PICTURE}/"
        index += 1
    
    str += '!'
    print("Message: ", str)
    
    return str

if __name__ == "__main__":
    iList = [Moves.b] * 15 + ["snap", Moves.f, Moves.l, Moves.l, Moves.l, Moves.o, Moves.r]
    print(compress_instructions(iList))
    
    # print(find_object_face())

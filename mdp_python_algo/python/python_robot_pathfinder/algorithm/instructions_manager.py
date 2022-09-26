from config.constants import Moves

"""
LEFT_FORWARD = 0
FORWARD_FORWARD = 1
RIGHT_FORWARD = 2
LEFT_BACKWARD = 3
BACKWARD_BACKWARD = 4
RIGHT_BACKWARD = 5
"""
# Take picture symbol
TAKE_PICTURE = 'take picture'


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
    iList = ["take picture"] + [Moves.BACKWARD_BACKWARD] * 3 + [Moves.RIGHT_FORWARD] + [Moves.FORWARD_FORWARD] + [Moves.LEFT_FORWARD] * 2
    return compress_instructions(iList * 4)

def commands_to_message(commands: list):
    index = 0
    str = ""
    while (index < len(commands)):
        str = str + f"{commands[index].move},{commands[index].repeat}/" if commands[
                                                                                           index] != TAKE_PICTURE else str + f"{TAKE_PICTURE}/"
        index += 1
    
    str += '!'
    print("Message: ", str)
    
    return str

if __name__ == "__main__":
    iList = [Moves.BACKWARD_BACKWARD] * 15 + ["take picture", Moves.FORWARD_FORWARD, Moves.LEFT_FORWARD, Moves.LEFT_FORWARD, Moves.LEFT_FORWARD, Moves.RIGHT_BACKWARD, Moves.RIGHT_FORWARD]
    print(compress_instructions(iList))
    
    # print(find_object_face())

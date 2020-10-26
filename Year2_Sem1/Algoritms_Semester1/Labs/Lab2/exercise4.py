import random
stack =[]
block_index = 0
game_len = int(input("How many blocks do you want in this game >>>>"))
while (game_len)-1  >= 0:       #continue game until no more blocks to  show
    for x in range(1):
        block = random.randint(0,2)     #generates a radnom num between 0 and 2
    if block == 0:
        color = 'Red'
    elif block == 1:
        color = 'Green'
    elif block == 2:
        color = 'Blue'
    #ask user to accept/ reject
    user = input("Do you accept this block: %s [Y/N]?." % (color))
    if user == 'y' or user == 'Y':
        stack.append(color)
        game_len -= 1
    #elif user == 'n' or user == 'N':
        #generate new color and ask to accept/reject#
    else:
        print("Error input incorrect.")
print(stack)








'''import random

def show_color():
    num_of_pairs = 0
    block_count = 0
    stack = []
    loop = False
    while loop == False:
        for x in range(1):
            block = random.randint(0, 2)
        block_count += 1
        if block == 0:
            color = 'Red'

        elif block == 1:
            color = 'Green'

        elif block == 2:
            color = 'Blue'
        user = input("Do you want this block color: %s [Y/N]>>> " % (color))
        if user == 'y' or user == 'Y':
            stack.append(color)
        elif user == 'n' or user == 'N':
            print(stack)
            break






show_color()
'''
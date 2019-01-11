import random

def pick_lotto():
    num_list = [str(i) for i in random.sample(range(1, 46), 6)]
    num = ' '.join(num_list)
    return num

print(pick_lotto())
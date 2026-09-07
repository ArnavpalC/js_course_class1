import random as ran

red_balls = 1
blue_balls = 1
green_balls = 1

bc = ['Blue', "Red", 'Green']
def pbe():
    reult = ran.choice(bc)
    p = bc.count('Red')/len(bc)

    print('Probability of Picking Red Ball is',p)

    if reult == 'Red':
        return 'Red Ball was Picked'

    else:
        return 'Not it'

r = pbe()
print(r)
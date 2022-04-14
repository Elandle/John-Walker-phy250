
# Cellular automata code without functions and classes


import random
import matplotlib.pyplot
import numpy

length = 20 # Row length of the cellular automata
rule = 69 # Rule number of cellular automata
time = 20 # Steps to evaluate cellular automata

# Makes the initial cellular automata state, with length entries, each entry randomly 0, 1, or 2
initial = [random.randint(0,2) for _ in range(length)]

# List of all possible neighbourhoods (each neighbourhood is a tuple)
neighbourhoods = [(0,0), (0,1), (0,2), (1,0), (2,0), (1,1), (1,2), (2,1), (2,2)] 

# Converts the rule to base 3 with a padding of size 9
rule= numpy.base_repr(rule, base= 3, padding= 0)
while(len(rule)<9): 
    rule = "0"+ rule

# Turn the rule of the cellular automata into a transformation table for each type of neighbourhood
table = {}
for i in range(len(neighbourhoods)):
    key = neighbourhoods[i]
    val = rule[i]
    table.update({key:val})

# Initializing the cellular automata
spacetime = [initial]
current = initial.copy()

# Evolving the cellular automata
for t in range(time):
    new = []
    for i in range(len(current)):
        neighbourhood = (current[(i-1)%length], current[i])
        new.append(int(table[neighbourhood]))
    current = new
    spacetime.append(new)

# Graphing the cellular automata results
matplotlib.pyplot.imshow(spacetime)
matplotlib.pyplot.show()

# Cellular automata code with functions and classes

import random
import matplotlib.pyplot
import numpy

# Function that takes a number and converts it to base 3 with an input padding
def ternarypadconversion(number, pad):
    ternary= numpy.base_repr(number, base= 3, padding= 0)
    while(len(ternary)<pad): 
        ternary= "0"+ ternary
    return ternary

# Function that makes a table for evolving each neighbourhood given an input rule number (not in base 3)
def maketable(rule):
    neighbourhoods= [(0,0), (0,1), (0,2), (1,0), (2,0), (1,1), (1,2), (2,1), (2,2)]
    ternaryrule= ternarypadconversion(rule, len(neighbourhoods))
    return dict(zip(neighbourhoods, map(int, reversed(ternaryrule))))

# Class for the cellular automata
class ECA(object):
    # Initializes cellular automatas
    def __init__(self, rule, initial):
        self.lookuptable= maketable(rule)
        self.initial= initial
        self.spacetime= [initial]
        self.current= initial.copy()
        self._length= len(initial)
        
    # Evolves cellular automatas
    def evolve(self, time):
        for _ in range(time):
            new= []
            for i in range(self._length):
                neighbourhood= (self.current[(i-1)], self.current[i])
                new.append(self.lookuptable[neighbourhood])
            self.current= new
            self.spacetime.append(new)
            
size= 20 # Row size of the cellular automata            
initial= [random.randint(0,2) for _ in range(size)] # Initializes a random starting row




# Making a cellular automata object. 
# Takes two inputs: rule number, starting row
ca= ECA(69, initial) 

ca.evolve(30) # Iterate the cellular automata input times

# Graph the cellular automata
matplotlib.pyplot.imshow(ca.spacetime)
matplotlib.pyplot.show()
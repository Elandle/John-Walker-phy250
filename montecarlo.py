import numpy
import matplotlib.pyplot

# Integrating P(x|a) gives N(a)=(a/(2*pi))^1/2
# Bayes theorem gives us P(a|{x1,...,xn})=P({x1,...,xn}|a)*P({x1,...,xn})/P(a)
# We are assuming the same variance a throughout, so it has a probability of 100% to occur, meaning P(a)=1
# So P(a|{x1,...,xn})=P({x1,...,xn}|a)*P({x1,...,xn})
# Expanding this out: P(a|{x1,...,xn})=(P(x1|a)*...*P(xn|a))*(P(x1)*...*P(xn))
# P(xi|a)= exp(-x^2/(2a))
# P(xi)= 1/(2*pi*a) * exp(-x^2/(2a^2))


N= 100 # number of samples
a= 2 # variance
x= numpy.random.rand(1,N)[0] # taking our input samples to be random

# Calculating P(a|{x1,...,xn}) and graphing it
P= numpy.array([])
for i in range(0,N):
    dummy= 1
    for j in range(0,i):
        dummy= dummy*numpy.exp(-x[j]*x[j]/(2*a))*numpy.exp(-x[j]*x[j]/(2*a*a))/(2*numpy.pi*a)
    P= numpy.append(P, [dummy])
matplotlib.pyplot.plot(P)


# Doing the monte carlo
x= numpy.array([])
x0= 1 # setting an initial state
timemax= 1000 # setting a maximum amount of time

for t in range(0,timemax):
    proposed= numpy.random.standard_normal(1)
    probability= 1
    test= (numpy.exp((-proposed*proposed)/(2*a*a))/(numpy.exp((-x0*x0)/(2*a*a))))*numpy.exp(-(x0-proposed)*(x0-proposed)/(2*a*a))
    if (test<=probability):
        probability= test
    u= numpy.random.uniform(0,1)
    if (u<=probability):
        x0= proposed
        x= numpy.append(x, [x0])
    else:
        x= numpy.append(x, [x0])
        
# Graph of trace plot
matplotlib.pyplot.plot(x)

# Histogram of chain
matplotlib.pyplot.hist(x)

# Not really sure how to interpret these graphs
# I tried to follow the instructions in the slides and assignment, but did not really understand the instructions
    
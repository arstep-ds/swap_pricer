import numpy as np
import numpy.random as rnd

def simulatePathCIR(r0, numSteps, alpha, b, sigma, timeDelta=1/12):
    d = 4 * b * alpha / (sigma**2)
    simPath = np.zeros(numSteps, dtype="float64")
    simPath[0] = r0
    if d > 1:
        for i in range(numSteps-1):
            c = (sigma**2) * (1 - np.exp(-alpha * timeDelta)) / (4 * alpha)
            lbda = simPath[i] * np.exp(-alpha * timeDelta) / c
            # Generate a random variable Z ~ Normal(0, 1)
            Z  = rnd.normal()
            # Generate a random variable X ~ chi-square(d - 1) 
            X = rnd.chisquare(d - 1)
            # calculate next value of the path
            simPath[i+1] = c * ((Z + np.sqrt(lbda))**2 + X) 
    else:
        for i in range(numSteps-1):
            c = (sigma**2) * (1 - np.exp(-alpha * timeDelta)) / (4 * alpha)
            lbda = simPath[i] * np.exp(-alpha * timeDelta) / c
            # Generate a random variable N ~ Poisson(lambda/2)
            N = rnd.poisson(lam=lbda/2)
            # Generate a random variable X ~ chi-square(d+2N)
            X = rnd.chisquare(d + 2*N)
            simPath[i+1] = c * X
    return simPath
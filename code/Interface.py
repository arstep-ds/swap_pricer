import InterestRate as ir
import CompoundingFrequency as cfr
import DiscountFactor as df
import PresentValue as pv
import pandas as pd
import numpy as np
import Interpolation as interp
import CIR
import matplotlib.pyplot as plt

ir.comp_to_cont(0.08, cfr.semiannual())

years = [0.5,1,1.5,2]
cash_flows = [80, 120, 160, 1200]
disc_factors = []
for year in years:
    disc_factors.append(df.disc_factor(r=0.08,m=cfr.semiannual(), t=year))

present_values = []
for i in range(len(cash_flows)):
    present_values.append(pv.present_value(cash_flows[i],disc_factors[i]))

# interpolation test
x_data = np.array([73/365, 165/365, 348/365])
y_data = np.array([0.0135, 0.0223, 0.0285])
x_interp = np.array([73/365, 272/365, 348/365])

cubic_spline = interp.cubic_spline(interp_values=x_interp, x_coord=x_data, y_coord=y_data)
linear = interp.piecwise_linear(interp_values=x_interp, x_coord=x_data, y_coord=y_data)

numSimulations = 1000
numSteps = 360
startVal = 0.01 # assuming initial interest rate to be 1% (yearly)
timeDelta = 1/12
alpha = 0.75
b = 0.02
sigma = 0.5
# each row is one scenario
simulationPaths = np.zeros((numSimulations, numSteps), dtype='float64')
for s in range(numSimulations):
    simulationPaths[s,:] = CIR.simulatePathCIR(startVal, numSteps,alpha=alpha, b=b, sigma=sigma, timeDelta=timeDelta)

for i in range(len(simulationPaths)-996):
    plt.plot(simulationPaths[i,:])
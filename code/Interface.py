#imports
import numpy as np
import ImpliedForward as ifwd
#simple testing
# data
years = np.array([0.49589, 1, 1.49589, 2])
rates = np.array([0.0089, 0.0123, 0.0141, 0.0163])
#calculate implied forwards for swap valuation
implied_fwds = ifwd.impl_fwd_swap(rates=rates, years=years)
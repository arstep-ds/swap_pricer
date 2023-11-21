import numpy as np
from scipy.interpolate import CubicSpline

def piecwise_linear(interp_values, x_coord, y_coord):
    return np.interp(x=interp_values, xp=x_coord, fp=y_coord)

def cubic_spline(interp_values, x_coord, y_coord):
    cs = CubicSpline(x_coord,y_coord)
    return cs(interp_values)

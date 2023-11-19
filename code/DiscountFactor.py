import math

def disc_factor(r, m, t):
    """Calculate discount factor, given rate r, freq m and time t"""
    return 1 / ((1+(r/m))**(m*t))

def disc_factor_simple_rate(r_s, t):
    """Calculate discount factor, given simple rate r_s and time t"""
    return 1 / (1+r_s*t)

def disc_factor_cont_rate(r_c, t):
    return math.exp(-r_c*t)
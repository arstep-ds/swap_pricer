import math

def cont_to_comp(r_c, m):
    """Takes continous rate and compunding frequency and returns the annual rate"""
    return m * (math.exp(r_c/m) - 1)

def comp_to_cont(r, m):
    """Takes annual rate and compunding frequency and returns the continuous rate"""
    return m * math.log(1+(r/m))

def simple_to_comp(r_s, m, t):
    """Takes simple rate, compunding frequency and time t
    and returns the continuous rate"""
    return m * (((1+(t*r_s))**(1/m*t)) - 1)

def comp_to_simple(r, m, t):
    """Takes compounding annual rate, compunding frequency and time t
    and returns the simple rate"""
    return (1/t) * (((1+r/m)**(m*t)) -1)

def cont_to_simple(r_c, t):
    """Convert a continuous compounding rate r_c to simple interest rate"""
    return (1/t)*(math.exp(r_c*t) -1)

def simple_to_cont(r_s, t):
    """Convert a simple interest rate r_s to continuous compounding rate"""
    return (1/t) * math.log(1+(t*r_s))
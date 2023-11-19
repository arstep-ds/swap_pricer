def disc_factor(r, m, t):
    """Calculate discount factor, given rate r, freq m and time t"""
    return 1 / ((1+(r/m))**(m*t))
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def iterate(start, stop, step):
    """ Iterates over the equation z = z**2 + c given the input parameters
    
    Parameters:
    start -------- float value that is the initial value used to calculate c which is then input into the above equation
    stop --------- float value that is the final value used to calculate c which is then input into the above equation
    step --------- float value which is by how much both x and y will increase by when used to calculate c
    
    Returns:
    conv --------- a list of points in the real/complex plane that when input into the above equation converge
    div ---------- a list of points in the real/complex plane that when input into the above equation converge
    loops -------- a list of the amount of iterations over the above equation required to diverge the specific point. List is
                   in parallel with the div list
    """
    conv = []
    div = []
    loops = []
    for x in np.arange(start, stop, step):
        for y in np.arange(start, stop, step):
            c = x + 1j * y
            z = 0
            loop = 0
        
            for _ in range(10):
                z = z ** 2 + c
                loop += 1
            
                if abs(z) > 2:
                    div.append(c)
                    loops.append(loop)
                    break
            else:
                conv.append(c)
    return conv, div, loops


import numpy as np
import matplotlib.pyplot as plt

def histvalues(filename):
    
    count, amp = np.loadtxt(filename, usecols=(0,1), unpack=True)
    counts, bin_edges = np.histogram(amp, bins=256)
    
    binsy = bin_edges[:len(bin_edges)-1]
    
    return counts, binsy
    
    
def histvalues2(filename):
    
    count, amp = np.loadtxt(filename, usecols=(0,1), unpack=True)
    counts, bin_edges = np.histogram(amp, bins=64)
    
    binsy = bin_edges[:len(bin_edges)-1]
    
    return counts, binsy
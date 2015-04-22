#!/usr/bin/env python

from statlib import stats

# zero crossing and negative sum
def zero_negative(package):
    negative = 0
    zero_crossed = 0
    for sample in range(len(package)):
        if package[sample] > 0:
            if sample != len(package) - 1:
                if package[sample + 1] < 0:
                    zero_crossed += 1
        else:
            negative += package[sample]
            if sample != len(package) - 1:
                if package[sample + 1] > 0:
                    zero_crossed += 1
    return stats.stdev(package), negative, zero_crossed 

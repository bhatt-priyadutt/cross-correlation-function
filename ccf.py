import numpy as np
import sys
import pandas as pd
from scipy import signal

def calc_ccf(x,y):
    xo = x - x.mean()
    yo = y - y.mean()
    correlation = signal.correlate(xo, yo, mode="full")
    corr_scores = ((correlation[:len(x)] / len(x)) /
                   (np.std(x) * np.std(y)))
    return corr_scores


if __name__=="__main__":
    df = pd.read_csv(sys.argv[1])
    x = df['x']
    y = df['y']
    corr_scores = calc_ccf(x,y)
    print(list(reversed(corr_scores)))

import sys
import random
import pandas as pd


def derive_y_var(xs, noise):
    y = []
    diff = 0
    for i in range(len(xs)):
        if i != 0:
            diff = xs[i] - xs[i - 1]
        y_i = xs[i] + noise + diff
        y.append(y_i)
    return y


def fill_y_holes(y, k):
    min_y = min(y)
    max_y = max(y)
    for i in range(k):
        y.insert(0, random.randint(min_y, max_y))
    return y


def alternative_algo(xs, noise_random_list):
    y = []
    for i in range(len(xs)):
        y_i = xs[i] + noise_random_list[i]
        y.append(y_i)
    return y

if __name__ == "__main__":
    use_alternative=True
    k = int(sys.argv[1])
    x = random.sample(range(1, 200), 30)
    xs = x[:-k]
    if use_alternative:
        # Using alternative algorithm
        noise_random_list = random.sample(range(1, 1000), 28)
        y = alternative_algo(xs, noise_random_list)
    else:
        noise = random.randint(0, 100)
        y = derive_y_var(xs, noise)
    y = fill_y_holes(y, k)
    df = pd.DataFrame(x, columns=['x'])
    df['y'] = y
    print(df)
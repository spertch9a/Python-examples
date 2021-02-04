import numpy as np

np.random.seed(123)

coin = np.random.randint(0, 2)  # This randomly generates 0 or 1

if coin == 0:
    print("heads")
else:
    print("tails")

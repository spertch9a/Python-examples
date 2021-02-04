import numpy as np

# seed(): sets the random seed, so that your results are reproducible between simulations.
np.random.seed(123)

# As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.

coin = np.random.randint(0, 2)  # This randomly generates 0 or 1
# rand(): if you don't specify any arguments, it generates a random float between zero and one.


if coin == 0:
    print("heads")
else:
    print("tails")

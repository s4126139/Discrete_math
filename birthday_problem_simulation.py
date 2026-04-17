from itertools import accumulate
import matplotlib.pyplot as plt
from operator import mul

num_days = 365

factors = [1 - i / num_days for i in range(num_days)]
prob_no_collision = list(accumulate(factors, mul))
prob_collision = [1 - p for p in prob_no_collision]

plt.plot(prob_collision)
plt.savefig('birthdays.png')

for n in (22, 23, 35, 100):
    print(f'The probability for {n} people '
          f'is {prob_collision[n - 1]}')
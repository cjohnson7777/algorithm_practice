from collections import Counter
import random

#[MEDIUM] Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

# Write a function to simulate an unbiased coin toss.



def toss_biased():
    return 1 if random.random() < 0.7 else 0


def toss_fair():
    while True:
        first_toss = toss_biased()
        second_toss = toss_biased()


        if first_toss != second_toss:
            return first_toss

print('Biased tosses')
biased_results = [toss_biased() for _ in range(1000)]
count_bias = Counter(biased_results)
print(count_bias)

print('\nFair tosses')
results = [toss_fair() for _ in range(1000)]
count = Counter(results)
print(count)
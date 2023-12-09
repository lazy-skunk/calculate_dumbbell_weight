from itertools import combinations

from tabulate import tabulate

PLATE_WEIGHTS = [1.25, 2.0, 2.5, 3.5]
TWO_PLATES_FOR_PAIR = 2
all_combinations = []

for i in range(1, len(PLATE_WEIGHTS) + 1):
    for subset in combinations(PLATE_WEIGHTS, i):
        total_weight = sum(subset) * TWO_PLATES_FOR_PAIR
        all_combinations.append([total_weight, ", ".join(map(str, subset))])

all_combinations.sort(key=lambda x: x[0])

headers = ["dumbbell", "plates"]
print(tabulate(all_combinations, headers=headers, tablefmt="fancy_grid"))

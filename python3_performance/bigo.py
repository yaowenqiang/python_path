import random
import time

def double_first_amount(amounts):
    return amounts[0] * 2

def sum_odd_amounts(amounts):
    sum = 0
    for a in amounts:
        if a % 2:
            sum += a
    return sum

random_amounts = [random.randint(1, 100) for _ in range(1000)]

start_time = time.time()
double_first_amount(random_amounts)
double_duration = time.time() - start_time

start_time = time.time()
sum_odd_amounts(random_amounts)
sum_duration = time.time() - start_time

print(f'duration double: {double_duration}')
print(f'duration sum: {sum_duration}')
print(f'Ratio of duration: {sum_duration/double_duration:2f}')



#amounts = [3, 11, 25]

#
#sum = 0
#
#for amount in amounts:
#    sum += amount

# your task is to clean this script in 
# a way that uses the code as a single function 
# that takes a path and returns the total_price variable
# that meets pep8 standards and receives a 10 score using pylint

import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
    
gift_costs = np.array(gift_costs).astype(int)  # convert string to int

start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))

start = time.time()

total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))


# (mlops) snehalbhagat@Mac coding_standards % pylint pylint_practice.py 
# ************* Module pylint_practice
# pylint_practice.py:1:38: C0303: Trailing whitespace (trailing-whitespace)
# pylint_practice.py:2:47: C0303: Trailing whitespace (trailing-whitespace)
# pylint_practice.py:7:22: C0303: Trailing whitespace (trailing-whitespace)
# pylint_practice.py:15:0: C0303: Trailing whitespace (trailing-whitespace)
# pylint_practice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# pylint_practice.py:11:0: E0401: Unable to import 'numpy' (import-error)
# pylint_practice.py:13:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
# pylint_practice.py:20:0: C0103: Constant name "total_price" doesn't conform to UPPER_CASE naming style (invalid-name)
# pylint_practice.py:26:6: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
# pylint_practice.py:33:6: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)

# -----------------------------------
# Your code has been rated at 1.25/10

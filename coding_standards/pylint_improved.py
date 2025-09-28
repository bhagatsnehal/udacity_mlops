"""
Calculate cost of gifts incurred for prime day

Author: Snehal
Date: 26 September 2025
"""

import numpy as np


def get_total_gift_cost(gift_costs_pth):
    """
    Returns the total cost of gifts incurred by gifting all gifts less than $25
    """
    with open(gift_costs_pth, 'r', encoding="utf-8") as file_path:
        gift_costs = file_path.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int

    total_cost = gift_costs[gift_costs < 25].sum() * 1.08 # add cost after tax
    return total_cost

if __name__ == '__main__':
    TOTAL_COST = get_total_gift_cost('gift_costs.txt')
    print(TOTAL_COST)

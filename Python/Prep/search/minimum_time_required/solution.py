#!/bin/python3

import math
import os
import random
import re
import sys

def minTime(machines, goal):
    machines = sorted(machines)
    n_machines = len(machines)

    best_case = int(goal / n_machines * machines[0])
    worst_case = int(goal / (n_machines - 1) * machines[-1])
    avg_case = 0

    # Binary Search Format
    while best_case < worst_case:
        sum_d = 0
        avg_case = (best_case + worst_case) // 2
        for m in machines:
            # calculate how many rubber ducks have been made after avg_case
            sum_d += (avg_case // m)
        # Have we made enough rubber ducks to meet our goal?
        if sum_d >= goal:
            # YES, we need less days to meet our goal
            worst_case = avg_case
        else:
            # NO, we need more days to meet our goal
            best_case = avg_case + 1
    return int(best_case)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()


import factors_of_number as factor
from typing import List

'''
simple leetcode challenge to learn some python
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Fred's follow up.  Skip the n2 bubble sort comparison logic and just go for a real solution.
'''

def get_input() -> List[int]:
    print( "Ok now for the main list stuff." )
    raw_input_str = input( 'Enter numbers separated by spaces or commas: ' )
    raw_input_str.strip()

    if not raw_input_str:
        print( 'well the input looks to be empty!' )
        return []

    numbers = [int(x) for x in raw_input_str.replace(',', ' ').split() if x.strip()]
    return numbers


def two_sum( nums: List[int], target: int) -> List[int]:
    return [1, 2]

if __name__ == '__main__':
    print( "Ok, starting now in main.  Here we go!" )
    target = int(input( "Input the target number: " ))
    print( f'You entered: {target}' )
    #
    # not necessary, find factors for fun
    #
    factors = factor.factors_of_number(int(target))
    print( f'Okey-Dokey then, here are the factors: {factors}' )

    numbers = get_input()
    print(f'here is the list of numbers you entered: {numbers}')

    #---------------------------------------------------------------
    # option # 1 -
    # save the original to search and get original indices from
    # use a sorted list copy and search high and low values to
    # reduce search time.
    #---------------------------------------------------------------
    original_list = numbers.copy()
    numbers.sort()
    print(f'sorted: {numbers}')

    low_index = 0
    high_index = len(numbers) - 1
    print(f'high index: {high_index}')
    
    for idx, low in enumerate(numbers):
        low = int(low)
        high = int(numbers[high_index])
        print( f'pos: {idx}: num: {low}, check: {numbers[idx]}' )

        if low + high == target:
            print(f'found our target, low: {low}, high: {high}!')
            break
        elif low + high > target:
            high_index -= 1
        elif low + high < target:
            continue
        else:
            print("how did we get here!?")


    print(f'{high} + {low} == {target}, and that is all now!')
    #
    # find the list indices corresponding to high and low values
    #
    if high == low:
        indices = [i for i, e in enumerate(original_list) if e == high]
        print( f'high and low are the same value, indices at {indices}')
    else:
        index1 = original_list.index(low)
        print( f'low value {low} at index {index1}')
        index2 = original_list.index(high)
        print( f'high value {high} at index {index2}')


'''
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Fred's notes.   

These are NOT python lists, but from a class ListNode.
On the leetcode page we are given this:
# 
# Definition for singly-linked list
#
# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

Using the ListNode class, populate two linked lists with numbers, stored in reverse order
as specified in the problem statement.

Then store the answer the same way, reverse order.  Print it all out for fun.

More Freds notes.  
    This ListNode class is logically just a contrived linked-list-stack data struct.
    Given the class ListNode, add some functions:
        - print, to dump list values 
        - pop, to remove and return list element
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):    # __str__ also
        ptr = self
        while ptr:
            print(ptr.val, end=" -> ")
            ptr = ptr.next
        print( "None" )

    def pop(self):
        if self is None:
            return None, None
        number = self.val
        self = self.next
        return number, self

#
# traverse the ListNode links and get all the values into a list of ints
#
def get_list_of_values( head: Optional[ListNode] ) -> list[int]:
    ptr = head
    rval = []
    while ptr:
        rval.append(ptr.val)
        ptr = ptr.next

    return rval

#
# join the list of ints into one int value 
#
# wondering what the cost is to convert int to str values
# and then convert the joined string back to an int rval
# 
# as opposed to C++ std::accumulate() 
#
def get_int_value_from_list( temp: list[int] ) -> int:
    if not temp:
        return 0

    joined_list = ''.join(str(num) for num in temp)
    return int(joined_list)


#
# input the first number.   
# - separate the individual numbers in the input
# - add the numbers to a linked list (this should be called a linked stack!)
#
first_input = input('Enter the first addend: ')
first_list = [int(char) for char in first_input]
first_linked_stack = None
for val in first_list:
    first_linked_stack = ListNode(val, first_linked_stack)

print('The first input number stored in reverse order in the list-stack:')
first_linked_stack.print()

#
# input the second number
#
second_input = input('Enter the second addend: ')
second_list = [int(char) for char in second_input]
second_linked_stack = None
for val in second_list:
    second_linked_stack = ListNode(val, second_linked_stack)

print('The second input number stored in reverse order in the list-stack:')
second_linked_stack.print()

temp1 = get_list_of_values(first_linked_stack)
temp1.reverse()
print(f'the list is {temp1}')
number1 = get_int_value_from_list(temp1)
print(f'the number is {number1}')


temp2 = get_list_of_values(second_linked_stack)
temp2.reverse()
print(f'the list is {temp2}')
number2 = get_int_value_from_list(temp2)
print(f'the number is {number2}')

answer = number1 + number2
print(f'{number1} + {number2} = {answer}')
#
# quite the series of dance moves in this comprehension
#
answer_int_list = [int(char) for char in list(str(answer))]
answer_linked_stack = None
for val in answer_int_list:
    answer_linked_stack = ListNode(val, answer_linked_stack)

print('the answer stored as a NodeList linked stack thing: ')
answer_linked_stack.print()





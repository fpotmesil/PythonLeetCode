'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''

my_string = input('Enter the string to find the longest substring with no repeating characters: ')

my_set = set()
my_dict = {}
start_idx = 0
sub_string = ""

for x, c in enumerate(my_string):
    print(f'char {c} as pos {x}')

    #
    # check to see if character is already in set
    #
    # if char is already in set, save in a dict:
    #   - whatever substring we have
    #   - start and end positions
    # else: 
    #   - keep growing the substring
    #   - insert char in set
    #
    if c in my_set:
        my_set.clear()
        print(f'char {c} already in set.  saving {sub_string}, indices {start_idx}:{x}')
        my_dict[sub_string] = [start_idx, x]
        start_idx = x
        sub_string = c 
        my_set.add(c)
    else:
        sub_string += c
        my_set.add(c)

    print(f'current substring is {sub_string}')
#
# dont forget to add the current substring we are populating 
# when we hit the end of the input
#
if len(sub_string) > 0: # always true i think.
    my_dict[sub_string] = [start_idx, x]

#
# can also skip the reverse sort and use a list[-1] for the longest substring.
#
sorted_strings = sorted(my_dict.keys(), key=len, reverse=True)
print( f'The sorted strings by len are: {sorted_strings}')
print( f'Largest substring is: \'{sorted_strings[0]}\', length: {len(sorted_strings[0])}')

#
# the original substring indices are still it the map for future reference.
# 
# this solution only finds the first longest substrings if there are multiples.
# 
    






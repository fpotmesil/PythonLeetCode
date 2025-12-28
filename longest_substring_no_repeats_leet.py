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

if len(s) == 0:
    return 0

my_set = set()
my_list= []
sub_string = ""

for c in s:
    if c in my_set:
        if len(sub_string) > 1:
            my_list.append(sub_string)
            cut_idx = sub_string.index(c) + 1
            sub_string = sub_string[cut_idx:]
            my_set.clear()
            for char in sub_string:
                my_set.add(char)
            sub_string += c
            my_set.add(c)
        else:
            my_set.clear()
            my_list.append(sub_string)
            sub_string = c
            my_set.add(c)
    else:
        sub_string += c
        my_set.add(c)

my_list.append(sub_string)

return len(max(my_list, key=len))




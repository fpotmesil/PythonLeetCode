"""
https://open.kattis.com/problems/repeatedsubsequence

Repeated Subsequence

You are given a string s.
Find the longest string t such that appears as a subsequence of s
at least twice.

A string t is a subsequence of s if you can highlight some characters of s such that,
when read in order from left to right, they form the string t. 
For example, 'aca' is a substring of 'abeacbad', 
because we can highlight indices 4, 5, and 7, as shown below.

Freds note - image does not translate to gvim.  :(
\includegraphics[scale=0.75]{onesubseq.png}

We say a string t appears as a subsequence at least twice if 
there are two different sets of indices of s that can be highlighted to form t.

Two sets are considered different if there is at least one position that is 
included in one set but not the other. 

For example, appears as a subsequence of 'aca' appears as a subsequence of 'abeacbad'
at least twice because we can highlight either of the below sets of indices 
(note that it is not the longest such subsequence):

Another image that does not show up  :(
\includegraphics[scale=0.75]{twosubseq.png}

Input

The first line of the input contains a single integer t (1 <= t <= 10^4)
—the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 <= n <= 2*10^5)
—the size of the string s

The second line of each test case contains n lowercase letters 
— the string s

It is guaranteed that the sum of n over all test cases does not exceed 2*10^5

Output

For each test case, if no subsequence of s
appears multiple times, print -1

Otherwise, output the longest string t
that appears as a subsequence of s multiple times.

If there are multiple solutions, print any.

Sample Input 1 
7
1
h
3
aab
3
xyz
7
ababbab
9
abceyzvpa
8
repeated
11
subsequence

	
Sample Output 1
-1
ab
-1
ababab
a
reated
subseque

Fred's notes - for standalone, we will do one string at a time, and just input the string.
The string input length can easily be determined in O(n) we wont consider this cost at all.
**Although I need to learn about how TJ did the command line arg glomming and then pop()d args.
"""



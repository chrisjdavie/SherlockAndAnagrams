'''
Solving the Sherlock and Anagrams puzzle on hackerrank.

---------------------

Problem Statement

Given a string S, find the number of "unordered anagrammatic pairs" of substrings.

Input Format

First line contains T, the number of testcases. Each testcase consists of string S in one line.

Constraints 
1<=T<=10 
2<=length(S)<=100 
String S contains only the lowercase letters of the English alphabet.

Output Format

For each testcase, print the required answer in one line.

---------------------

This problem is horribly ambiguous. I'll have a go at the most likely solution.

(Looks like I was right) One of these days I'll learn lambda functions

Created on 1 Jan 2016

@author: chris
'''
from itertools import combinations_with_replacement
from collections import Counter

def genSortedSubstrings(inputString):
    for i, j in combinations_with_replacement( range(len(inputString)), 2):
        yield ''.join(sorted(inputString[i:j+1]))

def numCombs(N):
    return N*(N-1)/2

for _ in range(input()):
    inputString = raw_input().strip()
    substringsCounted = Counter(genSortedSubstrings(inputString))
    
    print sum(map(numCombs, substringsCounted.values()))
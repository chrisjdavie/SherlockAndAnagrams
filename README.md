# SherlockAndAnagrams

Solving the hackerrank Sherlock And Anagrams puzzle

https://www.hackerrank.com/challenges/sherlock-and-anagrams

It's finding all the substrings, and then seeing how many are anagrams of each other

## Execution

$ cd solution/

$ python src/FirstGo.py < data/Input00.txt

## Complexity

This algorithm isn't great - finding all the substrings is O(N^2) (well O(N(N-1)/2)...) and the sorting the substrings is worst 
case O(NlogN) (maybe closer to N -> N/2 as the average string is half the length). This is the worst bit, and is O(N^3logN).

I think Counter, in the way I've used it, runs dynamically, so shouldn't be harming the execution time.

The substrings don't strictly need to be sorted - a frequency analysis can be done to find a unique, order independent
key to hash. It can be done dynamically, but for each key the hash needs to be generated, so reduces that bit from O(NlogN)
to O(26).

So there is an version of this algorithm that isn't too hard to implement that's O(N^2*13), which is much better than mine.
Mine is good enough and easier to understand if you can read Python

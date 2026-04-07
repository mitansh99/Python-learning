# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

#  EX - 1

# Input: s = "racecar", t = "carrace"
# Output: true

# EX - 2
# Input: s = "jar", t = "jam"
# Output: false


# Solution 1 - Sorting ---------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) ==sorted(t)


# Solution 2 - set and count -------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for c in set(s):
            if t.count(c)==s.count(c):
                continue
            else:
                return False
        return True
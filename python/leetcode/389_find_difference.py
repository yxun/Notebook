#%%
"""
- Find the Difference
- https://leetcode.com/problems/find-the-difference/
- Easy

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""

#%%
##
class S1:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = sorted(s)
        n = sorted(t)
        for i in range(len(m)):
            if m[i] != n[i]:
                return n[i]

        return n[-1]

#%%
class S2:
    def findTheDifference(self, s, t):
        res = {}
        for i in s:
            res[i] = res.get(i,0) + 1
        for j in t:
            res[j] = res.get(j,0) - 1
        for key in res:
            if abs(res[key]) == 1:
                return key

#%%
class S3:
    def findTheDifference(self, s, t):
        from collections import Counter
        return list((Counter(t) - Counter(s)).keys()).pop()

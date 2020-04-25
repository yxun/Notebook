#%%
"""
- Length of Last Word
- https://leetcode.com/problems/length-of-last-word/
- Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

#%%
##
class S1:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        words = s.split(' ')
        for i in range(len(words)-1, -1, -1):
            if words[i]:
                return len(words[i])
        
        return 0

#%%
class S2:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])


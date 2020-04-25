#%%
"""
- Wildcard Matching
- https://leetcode.com/problems/wildcard-matching/
- Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

"""

#%%
class S:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = True
        for i in range(len(p)):
            dp[i+1][0] = dp[i][0] and p[i] == '*'
            for j in range(len(s)):
                dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] if p[i] == '*' else dp[i][j] and p[i] in ('?', s[j])
        return dp[len(p)][len(s)]


#%%

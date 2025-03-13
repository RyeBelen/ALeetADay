'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

# Dumbass solution, forgot there was split
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        word = ""
        lastWord = ""

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            if s[i] != " ":
                word += s[i]
            elif s[i] == " ":
                if len(word) != 0:
                    lastWord = word
                word = ""

        if word != "":
            lastWord = word

        return len(lastWord)
 
        # Actual solution if you knew shit

        words = s.split()

        return len(words[-1])

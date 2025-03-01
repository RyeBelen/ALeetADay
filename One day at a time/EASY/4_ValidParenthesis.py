'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = "({["
        stacks = []

        # check length if valid
        if len(s) <= 1:
            return False

        # iterate
        for i in range(len(s)):

            # manual checking
            # check if its the opening
            if s[i] in opening:
                stacks.append(s[i]) 
            elif len(stacks) == 0: # if the starting is a close, return false
                return False
            # we can determine if its valid whenever we encounter a closing
            # if the opening within the stack is not the corresponding, we return false
            elif s[i] == ')':  
                if stacks.pop() != '(':
                    return False
            elif s[i] == '}':
                if stacks.pop() != '{':
                    return False
            elif s[i] == ']':
                if stacks.pop() != '[':
                    return False  

        # if there are still some opening remaining, its false
        if len(stacks) > 0:
            return False
        return True     
      
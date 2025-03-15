'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # SOlution was to basically to start at 3, add the previous and current value
        # repeat until n
        if n <= 2:
            return n

        # defined the inital first and second value
        first = 1 
        second = 2

        # starting from 3
        for i in range(3, n):

            # assign third as the sum of first and second
            third = first + second

            # now the first value will be the previous second
            first = second
            # then the second value will become the third one
            second = third

        
        # repeat until n and return first + second
        return first + second
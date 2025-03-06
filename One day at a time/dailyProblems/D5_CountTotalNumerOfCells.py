'''
There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.


Min 1 = 1
Min 2 = 5
Min 3 = 13


Return the number of colored cells at the end of n minutes.

 

Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
 

Constraints:

1 <= n <= 10^5
'''

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """

        k = 1

        for i in range(n):
            k += 4 * i

        return k


        # MY ORIGINAL SOLUTION, BASICALLY FOR EVERY ITERATION, ADD 4 MULTIPLIED BY CURRENT ITERATION
        # MIN 1 = i = 0, 4 * i(0) = 0, k(1) + 0 = k(1)
        # MIN 2 = i = 1, 4 * i(1) = 4, k(1) + 4 = k(5)
        # MIN 3 = i = 2, 4 * i(2) = 8, k(5) + 8 = k(13)

        # scale = 4
        # blocks = 1
        
        # if n == 1:
        #     return n

        # while n-1: 
        #     blocks += scale
        #     scale += 4
        #     n -= 1


        # return blocks
            

        
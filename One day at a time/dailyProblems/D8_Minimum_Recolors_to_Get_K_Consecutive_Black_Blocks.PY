'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
'''

# OPTIMAL
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        #initialize a left point
        left = 0 
        recolor = 0
        result = k # worst case, everything needs to be recolored

        # iterate through the list 
        for right in range(len(blocks)):

            # if the block at the current index is a W, increment recolor
            if blocks[right] == "W":
                recolor += 1           
            
            # if the the current index - the left index + 1 == k
            # or the size of the current window is exactly k
            if right - left + 1 == k:

                # determine the result  by finding the lowest
                result = min(result, recolor)

                # if the block at the left point is a W, decrement recolor
                if blocks[left] == "W":
                    recolor -= 1       

                # increement left pointer     
                left +=1

                
        return result

# BRUTE FORCE
        n = len(blocks)
        minimum = k 

        for i in range(n - k + 1):  # Iterate through all possible substrings of length k
            count = 0
            for j in range(i, i + k):  # Check the k-length substring starting at index i
                if blocks[j] == "W":
                    count += 1
            minimum = min(minimum, count)

        return minimum
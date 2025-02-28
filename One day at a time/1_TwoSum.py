'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # using regular loops
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
        # using hashmaps
        
        num_map = {}  # Dictionary to store visited numbers and their indices

        for index, value in enumerate(nums):
            # complement is just the number needed to add to value in order to react target
            complement = target - value
            
            # check if that value is present within num_map
            if complement in num_map :
                return(num_map[complement], index)
            
            # if not just add the number along with its index to the hashmap
            num_map[value] = index

        #return empty list
        #return []
      
        # using list comprehension 
        # no benefits but cool to know
        ans = [[i,j] for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] + nums[j] == target]
        return ans[0] if ans else []     
    
        


        
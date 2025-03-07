'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
'''

# bobo ampota
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0

        if nums[-1] == target:
            return len(nums)-1
        if nums[0] > target:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == target:
                return i
            if nums[i+1] > target and nums[i] < target:
                return i+1

        
        return len(nums)

            
        
# too stupid to think of this
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            else:
                i += 1
        return i
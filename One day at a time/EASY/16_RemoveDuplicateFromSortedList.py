'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Travers through the linked list
        current = head

        # we need to check if there is a value in the currnet node and next node
        # in order to not go to a none node
        while current and current.next:
            
            # check if current value is the same as the next node
            if current.val == current.next.val:
                # if they're the same, the current node will point to the node after
                # its current .next
                # we can do this since we wil only move to the next node if there value
                # of the next node isn't the same
                current.next = current.next.next
            else:
                
                current = current.next
        return head



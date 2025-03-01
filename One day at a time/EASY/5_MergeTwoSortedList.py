'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # ll = linked list

        list3 = ListNode()  # create new ll
        numList = [] # create empty list to store value

        # append all the contents of the 1st ll to the numlist
        while(list1):
            numList.append(list1.val)
            list1 = list1.next
        
        # append all the contents of the 2nd ll to the numlist
        while(list2):
            numList.append(list2.val)
            list2 = list2.next
        
        # sort 
        numList.sort()

        # iterate through the entire numlist
        for i in numList:

            # put the each current value in numlist in a temporary node
            temp = ListNode(i)
            
            # if the list is empty set temp to list3
            if list3 is None:
                list3 = temp
                pass
            
            # iterate through the ll
            current_node = list3
            while current_node.next:
                current_node = current_node.next
            
            # add the temp node to the end of the list
            current_node.next = temp
        
        return list3.next

        

   
        
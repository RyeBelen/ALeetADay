'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


# THIS DEFINITELY NOT THE OPTIMAL SOLUTION TO DO THIS
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # declares variables to use
        list3 = ListNode(None)
        s1 = "" # to hold l1's value
        s2 = "" # to hold l2's value
        total = 0

        # iterate through l1 and add at beginning of the string
        while(l1):
            s1 = str(l1.val) + s1  
            l1 = l1.next
    
        # iterate through l2 and add at beginning of the string
        while(l2):
            s2 = str(l2.val) + s2 
            l2 = l2.next

        # get the total of both
        total = str(int(s1) + int(s2))
        
        # reverse that shit
        rev = total[::-1]

        # iterate through the entire answer
        for i in range(len(rev)):  

            # create temp node with the value being each digit of the answer
            temp = ListNode(int(rev[i]))

            # check if empty
            if list3.val is None:
                list3 = temp
                continue
                
            #iterate through the list
            current = list3
            while current.next:
                current = current.next

            # add
            current.next = temp
        
        return list3
            
# OPTIMAL SOLUTION BUT I DONT KNOW SHIT
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        result = root
        excess = 0
        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next
            
            result.next = ListNode(excess%10)
            result = result.next
            excess = excess//10
            
        return root.next  

        
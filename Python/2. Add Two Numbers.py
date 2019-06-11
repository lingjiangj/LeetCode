# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            result = ListNode(0)
            current = result 
            carry = 0
            while l1 != None or l2!=None or carry != 0:
                t1,t2 = 0,0
                if l1 != None:
                    t1 = l1.val
                    l1 = l1.next
                if l2 != None:
                    t2 = l2.val
                    l2 = l2.next
                tmpsum = t1+t2+carry
                carry = tmpsum//10
                current.next = ListNode(tmpsum % 10)
                current = current.next
                
            return result.next
        
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Method 1 - 对链表中每一个对位相加，若大于十进1.
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
    
# Solution 2
##两个公式分别计算，链表 -> 整数相加 -> 链表
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getNumber(l):
            num = ""
            while l != None:
                num += str(l.val)
                l = l.next
            return int(num[::-1])
        
        def buildListNode(num):
            num_reversed = str(num)[::-1]
            result = node = ListNode(0)
            for i in num_reversed:
                node.next = ListNode(int(i))
                node = node.next
            return result.next
        
        n = getNumber(l1) + getNumber(l2)
        return buildListNode(n)
        

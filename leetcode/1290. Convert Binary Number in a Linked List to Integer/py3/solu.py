# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# from typing import list
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        theList = []
        while(head != None):
            theList.append(head.val)
            head = head.next
        
        rever = theList
        rever.reverse()
        print('the list: ', theList, ', rever: ', rever)
        
        sum = 0
        for it in range(len(rever)):
            temp = pow(2, it) * rever[it]
            print('temp: ', temp)
            sum += temp
        return sum


head = ListNode(1, None)
head = ListNode(1, head)
head = ListNode(1, head)
head = ListNode(0, head)
head = ListNode(1, head)

sol = Solution()
print('ret: ', sol.getDecimalValue(head) )

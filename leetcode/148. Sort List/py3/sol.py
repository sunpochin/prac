# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Merge Sort

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (None == head):
            return head
        
        arr = []
        while(head != None):
            arr.append(head.val)
            head = head.next
            
        arr.sort()
#        print('arr: ', arr)
        lastNode = None
        for it in reversed(arr):
            curNode = ListNode(it, lastNode)
            lastNode = curNode
            
        return curNode
    
        
        
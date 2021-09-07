from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = curhead = ListNode(-1)
        print('dummy head next: ', dummyhead.next, '\n curhead next, ', curhead.next)
        
        while l1 and l2:
            if l1.val < l2.val:
                curhead.next = l1
                print('curhead.next: ', curhead.next.val)
                l1 = l1.next
            else:
                curhead.next = l2
                print('curhead.next: ', curhead.next.val)
                l2 = l2.next
            curhead = curhead.next
            print('dummy head next: ', dummyhead.next, '\n curhead next, ', curhead.next)
            print('l1: ', l1, '\n l2, ', l2, '\n')


        if l1:
            curhead.next = l1
        if l2:
            curhead.next = l2
        return dummyhead.next


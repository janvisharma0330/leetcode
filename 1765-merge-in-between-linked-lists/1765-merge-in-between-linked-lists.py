# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        t1=list1
        for i in range(a-1):
            t1=t1.next
        t2=t1.next
        for i in range(b-a + 1):
            t2=t2.next
        t1.next=list2
        while list2.next:
            list2=list2.next
        list2.next=t2
        return list1




        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        i=0
        j=len(arr)-1
        res=0
        while i<j:
            res=max(res,arr[i]+arr[j])
            i=i+1
            j=j-1
        return res        
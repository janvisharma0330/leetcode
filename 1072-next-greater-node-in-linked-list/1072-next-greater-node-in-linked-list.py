# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer=[]
        stack=[]
        index=0
        while head is not None:
            answer.append(0)
            curr=head.val
            while stack and stack[-1][0] < curr:
                last=stack.pop()
                answer[last[1]] = curr
            stack.append((curr, index))
            index+=1
            head=head.next
        return answer

        
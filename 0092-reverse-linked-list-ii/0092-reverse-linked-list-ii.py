class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(m-1): p = p.next
        tail = p.next

        for i in range(n-m):
            tmp = p.next                  
            p.next = tail.next            
            tail.next = tail.next.next    
            p.next.next = tmp             
        return dummy.next
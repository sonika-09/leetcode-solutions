# 206 - Reverse Linked List
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head 
        prev_node = None
        while temp:
            next_node = temp.next
            temp.next = prev_node

            prev_node = temp
            temp = next_node
        return prev_node
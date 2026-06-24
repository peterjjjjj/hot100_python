class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return head

        curt = head
        prev_node = None

        while curt:
            next_node = curt.next
            curt.next = prev_node
            prev_node = curt
            curt = next_node

        return prev_node

if __name__ == '__main__':
    test = ListNode(0)
    test.next = ListNode(1)
    test.next.next = ListNode(2)
    test.next.next.next = ListNode(3)
    test.next.next.next.next = ListNode(4)
    test.next.next.next.next.next = ListNode(5)

    trial = Solution()
    trial.reverseList(test)




        

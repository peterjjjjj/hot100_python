#LC 19

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head

        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

if __name__ == '__main__':
    test = Solution()
    case = ListNode(1)
    case.next = ListNode(2)
    case.next.next = ListNode(3)
    case.next.next.next = ListNode(4)
    case.next.next.next.next = ListNode(5)
    print(test.removeNthFromEnd(case, 2))
    pass
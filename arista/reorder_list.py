class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next
        if slow == fast:
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr

            curr = next_node

        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next


            first.next = second
            second.next = first_next

            second = second_next
            first = first_next


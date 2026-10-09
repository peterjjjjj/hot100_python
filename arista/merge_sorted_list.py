#LC 21

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode
                                   | None, list2: ListNode | None) -> ListNode | None:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
        else:
            head = list2

        while list1 and list2:
            if list1.val <= list2.val:
                while list1.next and list1.next.val <= list2.val:
                    list1 = list1.next
                next_node = list1.next
                list1.next = list2
                list1 = next_node
            else:
                while list2.next and list2.next.val <= list1.val:
                    list2 = list2.next
                next_node = list2.next
                list2.next = list1
                list2 = next_node

        return head
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1.next, list2)
            return list2


_list1 = ListNode(1, ListNode(2, ListNode(4, None)))
_list2 = ListNode(1, ListNode(3, ListNode(4, None)))

_result = Solution().mergeTwoLists(_list1, _list2)
a = 4

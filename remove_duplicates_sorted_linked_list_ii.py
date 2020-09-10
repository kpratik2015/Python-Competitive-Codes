# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next


class MySolution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        last_unique = ListNode(-99)
        dummy = last_unique
        fast_head = head.next
        last_rejected = ListNode(-99)
        if not head.next:
            return head
        while head:
            # print(f"{head.val} {last_rejected.val}")
            if fast_head and head.val != fast_head.val and head.val != last_rejected.val:
                last_unique.next = head
                last_unique = last_unique.next
            elif not fast_head and head.val != last_rejected.val:
                last_unique.next = head
                last_unique = last_unique.next
            else:
                last_rejected.val = head.val
                last_unique.next = None
            head = head.next
            if fast_head:
                fast_head = fast_head.next
        return dummy.next

h = Solution().deleteDuplicates(ListNode(1,ListNode(1,ListNode(1,ListNode(2,ListNode(3))))))

while h:
  mark = "->" if h.next else ""
  print(f"{h.val} {mark}", end=" ")
  h = h.next
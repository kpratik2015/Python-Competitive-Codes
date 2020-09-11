# Problem: https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        pre = ListNode(-99)
        post = ListNode(-99)
        post_temp = post
        pre_temp = pre
        temp = head
        while temp:
            if temp.val < x:
                pre.next = temp
                pre = pre.next
            else:
                post.next = temp
                post = post.next
            temp = temp.next
        post.next = None
        pre.next = post_temp.next
        return pre_temp.next

h = Solution().partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3)

while h:
  mark = "->" if h.next else ""
  print(f"{h.val} {mark}", end=" ")
  h = h.next
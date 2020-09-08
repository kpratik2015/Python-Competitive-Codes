# Problem: https://leetcode.com/problems/rotate-list/

'''
Rotations is calculated as k % total nodes.

Two node pointers created: SP and FP.
FP goes till k-1 element first. Then SP goes on until FP reaches end.
FP points to element whose next will be elements by SP.

save SP's next in temp.
SP'next is nulled as it is element at the end, which reflects in head
FP's next is head
head is reset to temp.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__ (self):
      return str(self.val)

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if head.next == None:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotateTimes = k%length

        if k == 0 or rotateTimes == 0:
            return head
        
        print(f"rotateTimes: {rotateTimes}")

        fastPointer = head
        slowPointer = head

        for _ in range (rotateTimes): # fastPointer reaches to element 
            fastPointer = fastPointer.next 
        print(f"fastPointer is at [{fastPointer.val}]")
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        print(f"slowPointer at [{slowPointer.val}] and fastPointer at [{fastPointer.val}]")
        # slowPointer is now at the elment which will be end
        temp = slowPointer.next # saving start position in temp
        print(f"temp at [{temp}] and slowPointer's next [{slowPointer.next}] will be nulled")
        slowPointer.next = None # with this head is also modified to cut off the starting elements
        print(f"fastPointer's next [{fastPointer.next}] will point to head [{head}]")
        fastPointer.next = head # fastPointer was at the end, now the end's next will point to head
        head = temp # giving back start position to head

        return head

node = Solution().rotateRight(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),4)
while node:
  print(f"[{node.val}]", end=" ")
  node = node.next
'''
# merge2Lists(l1, l2)
1. two dummy nodes: head, point
2. while node in l1 and l2:
  2.a. Two Routes:
    2.a.[i] l1.val is less or equal to l2.val, point.next assigned to l1 and l1 is advanced
    2.a.[ii] l2.val is less than l1.val, point.next assigned to l2, l2 assigned to l1 and l1 assigned point.next.next
  2.b. advance point.next
3. non-empty list is assigned to point.next
4. return head.next

Note: l2 always is list of nodes with higher values and l1 is left over nodes of point.
'''

from typing import List
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  def __repr__(self):
    return f'[{self.val}]-'

def merge2Lists(l1, l2):
  head = point = ListNode(0)
  while l1 and l2:
    if l1.val <= l2.val:
      point.next = l1 # point attaches to l1 nodes as its val is lower
      l1 = l1.next # l1 is advanced
    else:
      point.next = l2 # point attaches to l2 nodes as its val is lower
      l2 = l1 # l2 must have higher value nodes, so the switch
      l1 = point.next.next # l1 goes back to the left over nodes of point (which comes from previous l2)
    point = point.next
  if not l1:
    point.next=l2
  else:
    point.next=l1
  return head.next

def mergeKLists(lists: List[ListNode]) -> ListNode:
  if not lists:
    return ListNode("")
  amount = len(lists)
  interval = 1
  while interval < amount:
    for i in range(0, amount - interval, interval * 2): # two taken at a time, so advance by 2
      # print(f'm2L({i}, {i+interval}) with interval {interval}')
      lists[i] = merge2Lists(lists[i], lists[i + interval])
    interval *= 2
  return lists[0] if amount > 0 else lists

x = ListNode(1, ListNode(4, ListNode(5)))
y = ListNode(1, ListNode(3, ListNode(4)))
z = ListNode(2, ListNode(6))

res = mergeKLists([x, y, z])

while res:
  print(res, end='')
  res = res.next

# [1]-[1]-[2]-[3]-[4]-[4]-[5]-[6]-
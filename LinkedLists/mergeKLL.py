""" 
Merge K sorted LL by calling merge2LL on all LL
"""
from LinkedList import Node, Linkedlist
  
def printLL(head):
  temp = head
  while temp:
    print(temp.val, end=" ")
    temp = temp.next
  print()
    
      

def merge2LL(head1, head2):
  currHead = dummy = Node(-1)
  while head1 and head2:
    if head1.val <= head2.val:
      currHead.next = head1
      head1 = head1.next
    else:
      currHead.next = head2
      head2 = head2.next 
    currHead = currHead.next
  if head1 is None and head2 is not None:
    currHead.next = head2
  if head1 is not None and head2 is None:
    currHead.next = head1 
  return dummy.next


def mergeKLL(heads):
  currHead = heads[0]
  for i in range(1,len(heads)):
    currHead = merge2LL(currHead, heads[i])
  return currHead


if __name__ == "__main__":
  k = int(input("enter k: "))
  heads = []
  for _ in range(k):
    llNodes = list(map(int,input().strip().split()))
    ll = Linkedlist()
    for n in llNodes:
      ll.append(n)
    heads.append(ll.head)
    # print(ll)
    # printLL(ll.head)
  print("before", heads)
  newHead = mergeKLL(heads)
  print("after", heads)
  printLL(newHead)
""" 
Given two sorted linked lists consisting of N and M nodes respectively. 
The task is to merge both of the list (in-place) and return head of the merged list.
"""

from LinkedList import Node, Linkedlist
        
def printLL(node):
    while node:
        print(node.val, end=" ")
        node = node.next 
    print()
        
    
        
def mergeTwoLL(head1, head2):
    #currHead travels over the newly formed linked list, dummyNode is used to point to the head of merged LL
    currHead = dummyNode = Node(-1)
    while head1 and head2:
        if head1.val < head2.val:
            currHead.next = head1
            head1 = head1.next 
        else:
            currHead.next = head2 
            head2 = head2.next 
        currHead = currHead.next
    if head1 or head2:
        currHead.next = head1 if head1 else head2
    return dummyNode.next 


    
if __name__ == "__main__":
    n,m = map(int, input().strip().split())
    ll1 = Linkedlist()
    ll2 = Linkedlist()
    ll1Nodes = list(map(int,input().strip().split()))
    ll2Nodes = list(map(int,input().strip().split()))
    for x in ll1Nodes:
        ll1.append(x)
    for x in ll2Nodes:
        ll2.append(x)
    printLL(mergeTwoLL(ll1.head,ll2.head))


        
""" 
You are given the heads of two sorted linked lists list1 and list2. Merge the two
lists into one sorted list. The list should be made by splicing together the nodes 
of the first two lists. Return the head of the merged linked list.
uses extra Linked list
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    #creates a new node and appends node to ll
    def append(self, newVal):
        newNode = ListNode(newVal)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode
        
def printLL(node):
    while node:
        print(node.val, end=" ")
        node = node.next 
    print()
        
    
        
def mergeTwoLL(head1, head2):
    #currHead travels over the newly formed linked list, dummyNode is used to point to the head of merged LL
    currHead = dummyNode = ListNode(-1)
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
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1Nodes = list(map(int,input().strip().split()))
    ll2Nodes = list(map(int,input().strip().split()))
    for x in ll1Nodes:
        ll1.append(x)
    for x in ll2Nodes:
        ll2.append(x)
    printLL(mergeTwoLL(ll1.head,ll2.head))


        
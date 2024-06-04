""" 
Given two sorted lists, merge them so as to produce a combined sorted list
using Recursion.
Approach: The recursive solution can be formed, given the linked lists are sorted. 

Compare the head of both linked lists.
Find the smaller node among the two head nodes. The current element will be the smaller node among two head nodes.
The rest elements of both lists will appear after that.
Now run a recursive function with parameters, the next node of the smaller element, and the other head.
The recursive function will return the next smaller element linked with rest of the sorted element. Now point the next of current element to that, i.e curr_ele->next=recursivefunction()
Handle some corner cases. 
If both the heads are NULL return null.
If one head is null return the other.
"""



class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def merge(h1, h2):    
    if h1 is None and h2 is not None:
        return h2
    if h1 is not None and h2 is None:
        return h1

    if h1.data <= h2.data:
        h1.next = merge(h1.next, h2)
        return h1
    else:
        h2.next = merge(h1, h2.next)
        return h2


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(9)

head2 = Node(4)
head2.next = Node(6)
head2.next.next = Node(14)

# head2 = Node(0)
# head2.next = Node(2)
# head2.next.next = Node(14)


printList(head1)
print()
printList(head2)
print()
mergedhead = merge(head1, head2)
printList(head1)
print()
printList(head2)
print()
printList(mergedhead)
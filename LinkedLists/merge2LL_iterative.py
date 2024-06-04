class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def merge(head1, head2):    
    currHead = dummyNode = Node(-1)
    while head1 and head2:
        if head1.data <= head2.data:
            currHead.next = head1
            head1 = head1.next 
        else:
            currHead.next = head2 
            head2 = head2.next 
        currHead = currHead.next
    if head1 is None and head2 is not None:
        currHead.next = head2 
    if head2 is None and head1 is not None:
        currHead.next = head1
    return dummyNode.next


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next

head1 = Node(1)
head1.next = Node(3)


head2 = Node(4)
head2.next = Node(6)


# head2 = Node(0)
# head2.next = Node(2)
# head2.next.next = Node(14)


mergedhead = merge(head1, head2)
printList(mergedhead)
class Node:
  def __init__(self,val, next=None) -> None:
    self.val = val
    self.next = next
    
  def __repr__(self) -> str:
    return str(self.val)
    

# Definition for singly-linked list.
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    #creates a new node and appends node to ll
    def append(self, newVal):
        newNode = Node(newVal)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode
      
  
    def __repr__(self) -> str:
        return str(self.head.val)
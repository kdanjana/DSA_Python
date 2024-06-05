""" 
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
intution:
We can create a min heap pq to maintain the head nodes of all linked lists. Each time, we take out the node
with the smallest value from the min heap, add it to the end of the result linked list, and then add the
next node of this node to the heap. Repeat the above steps until the heap is empty.
The time complexity is o(nxlogk), and the space complexity is o(k). Here, n is the total number of all linked 
list nodes, and k is the number of linked lists given in the problem.
Here's the step-by-step intuition behind the solution:
First, we initialize a min-heap that will contain the current smallest node from each linked-list.
We go through the list of linked-lists, and if a linked-list is not empty, we insert its head into the min-heap. 
Since we are dealing with a linked-list, we only need a reference to the head node to access the entire list.
We create a new dummy node that serves as the precursor to the merged linked-list, which we'll build one node
at a time as we extract the smallest nodes from the min-heap.
While the min-heap is not empty, we perform the following steps:
Extract the smallest node from the min-heap (this is done efficiently for a min-heap since the smallest element 
is always the root).
If the extracted node has a next node, we insert the next node into the min-heap to replace the position of 
the extracted node.
Append the extracted node to the merged linked-list by setting the next reference of the current node to this 
extracted node.
Move the current node pointer forward to this extracted node, which is now the last node in the merged list.
Once we've exhausted all the nodes (when the min-heap is empty), we've built the complete merged linked-list
which starts from the dummy node's next node.
The use of the min-heap ensures that we're always processing nodes in ascending order since the heap is always
sorted after each insertion and removal.
IMPORTANT:
 A __lt__ method is added to the ListNode class, which allows the comparison between two ListNode instances 
 based on their val attribute. This is required for the heap to maintain the correct order based on node 
 values
 
Time Complexity: O(N * K * log K)
Auxiliary Space: O(K)
"""
import sys, os 

# Get the absolute path to the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)


from LinkedLists.LinkedList import Node, Linkedlist
import heapq 



def printLL(head):
  temp = head
  while temp:
    print(temp.val, end=" ")
    temp = temp.next
  print()
  
  
  
  
def mergeKLists(lists):
  #setattr(Node, "__lt__", lambda a, b: a.val < b.val)
  #using min heap
  pq = []
  # Adding the first node of each LL to pq
  for head in lists:
    if head:  # Check if the head node is not None
      #heapq.heappush(pq, (head))
      heapq.heappush(pq, (head.val, head))
  # Creating a dummy node which will help in easily returning the head of the merged list
  dummy = Node(-1)
  current = dummy
  while pq:
    #node = heapq.heappop(pq)
    node = heapq.heappop(pq)[1]
    current.next = node
    current = current.next
    if node.next:  # Check if the next node exists
      #heapq.heappush(pq, node.next)
      heapq.heappush(pq, (node.next.val, node.next))
  return dummy.next



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
  newHead = mergeKLists(heads)
  print("after", heads)
  printLL(newHead)


""" 

ChatGPT
The comparison of val in the Node class is handled by the __lt__ method that is defined in the Node class. 
In the provided code snippet, setattr(Node, "__lt__", lambda a, b: a.val < b.val) sets the __lt__ attribute 
of the Node class to a lambda function. This lambda function takes two arguments a and b, which represent 
instances of the Node class, and compares their val attributes to determine if a is less than b.

Here's the relevant part of the code again for reference:
setattr(Node, "__lt__", lambda a, b: a.val < b.val)

So, when you compare two instances of the Node class using the less-than (<) operator, Python internally 
calls this lambda function to determine the result of the comparison based on the val attribute of the 
nodes
"""
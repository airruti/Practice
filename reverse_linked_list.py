from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Initialize three pointers prev as NULL, curr as head and next as NULL.
        Iterate through the linked list. In loop, do following. 
        // Before changing next of current, 
        // store next node 
        next = curr->next
        // Now change next of current 
        // This is where actual reversing happens 
        curr->next = prev 
        // Move prev and curr one step forward 
        prev = curr 
        curr = next
        
        """
        prevNode = None
        currNode = head
        nextNode = None
        
        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode

print(reverseList([1234]))

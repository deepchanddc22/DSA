class ListNode:
    def __init__(self,value = 0,next=None):
        self.value = value
        self.next = next
        
        
def detect_cycle(head):
    
    if not head and not head.next:
        return False
    
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False


# Create nodes of the linked list
node1 = ListNode(1)  # First node with value 1
node2 = ListNode(2)  # Second node with value 2
node3 = ListNode(3)  # Third node with value 3
node4 = ListNode(4)  # Fourth node with value 4

# Link the nodes to form a cycle
node1.next = node2  # node1 points to node2
node2.next = node3  # node2 points to node3
node3.next = node4  # node3 points to node4
node4.next = node2  # node4 points back to node2, forming a cycle

# Test the function on the cyclic list
print(detect_cycle(node1))  # Output: True because there is a cycle

# Create a new list without a cycle
node1 = ListNode(1)  # First node
node2 = ListNode(2)  # Second node
node1.next = node2   # node1 points to node2

# Test the function on the non-cyclic list
print(detect_cycle(node1))  # Output: False because there is no cycle

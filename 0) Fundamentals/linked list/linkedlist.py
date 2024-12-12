class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            
            
    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point its next to the current head
        self.head = new_node  # Update the head to this new node
        
        
        
    def insert_at_position(self, data, position):
        """Insert a node with the given data at the specified position."""
        new_node = Node(data)
        
        # Case 1: Inserting at the head (position 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Case 2: Inserting at any other position
        current = self.head
        current_position = 0

        # Traverse the list to find the node just before the target position
        while current and current_position < position - 1:
            current = current.next
            current_position += 1
        
        # If current is None, the position is out of bounds
        if current is None:
            print("Position out of bounds!")
            return
        
        # Insert the new node
        new_node.next = current.next
        current.next = new_node


            
        
    def delete(self, data):
        if self.head is None:  # List is empty
            print("List is empty")
            return

        if self.head.data == data:  # If the head node needs to be deleted
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:  # Traverse the list
            current = current.next

        if current.next is None:  # Node with the target data not found
            print(f"Node with data {data} not found")
        else:  # Remove the node
            current.next = current.next.next

        
    def reverse_iterative(self):
        prev = None  # This will be the new tail of the reversed list (initially empty)
        current = self.head  # Start with the current head of the list

        while current:  # Traverse the list until we reach the end (current becomes None)
            next_node = current.next  # Save the next node (to keep track of the rest of the list)
            current.next = prev  # Reverse the current node's pointer to point to the previous node
            prev = current  # Move the `prev` pointer one step forward (to the current node)
            current = next_node  # Move the `current` pointer one step forward (to the next node)

        self.head = prev  # Update the head of the list to the new first node (prev)

    
    def reverse_recursive(self):
        def _reverse_recursive(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse_recursive(next_node, current)

        self.head = _reverse_recursive(self.head, None)
        
        
    def display(self):
        """Print all the nodes in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
        
        
        
        
# Create a linked list
ll = LinkedList()

# Append nodes
ll.append(10)
ll.append(20)
ll.append(30)

# Display the linked list
print("Linked list after appending nodes:")
ll.display()

# Prepend a node
ll.prepend(5)
print("Linked list after prepending a node:")
ll.display()

# Delete a node
ll.delete(20)
print("Linked list after deleting a node:")
ll.display()

# Try deleting a node not in the list
ll.delete(100)

# Check if the list is empty
# print("Is the list empty?", ll.is_empty())

ll.insert_at_position(5, 0)  # Insert at head
ll.insert_at_position(15, 2)  # Insert in the middle
ll.insert_at_position(35, 5)  # Insert at the end

# Display updated list
print("Updated list:")
ll.display()

            
            
ll.reverse_iterative()
print("Reversed list (iterative):")
ll.display()
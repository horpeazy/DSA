class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    # Define a function outside of the class
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def append(self, value):
        """ Append a value to the end of the list. """    
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def search(self, value):
        """ Search the linked list for a node with the 
            requested value and return the node. 
        """
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return node

    def remove(self, value):
        """ Remove first occurrence of value. """
        node = self.head
        prev = None
        while node:
            if node.value == value:
                if node == self.head:
                    self.head = node.next
                    return
                else:
                    prev.next = node.next
                    return
            prev = node
            node = node.next

        return

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        value = self.head.value
        self.head = self.head.next
        return value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return
        
        node = self.head
        i = 0
        while node.next and i < pos - 1:
            node = node.next
            i += 1
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        return
    
    def size(self):
        """ Return the size or length of the linked list. """
        len_ = 0
        node = self.head
        while node:
            node = node.next
            len_ += 1

        return len_
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])


def print_linked_list(head):
    temp_node = head
    
    while temp_node is not None:
        print(temp_node.value)
        temp_node = temp_node.next

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = Node(input_list[0])
    for i in range(1, len(input_list)):
        temp_head = head
        while temp_head is not None:
            temp_head = temp_head.next
        temp_head.next = Node(input_list[i])
        
    return head

def create_linked_list_better(input_list):
    head = None
    tail = None
    
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
            
    return head

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
        
        
def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    rllist = LinkedList()
#     node = linked_list.head   
#     while node:
#         if rllist.head is None:
#             rllist.append(node.value)
#             node = node.next
#             continue
#         new_node = Node(node.value)  ## Prepend to the linked list
#         new_node.next = rllist.head
#         rllist.head = new_node
#         node = node.next

    for value in reversed(list(linked_list)):
        rllist.append(value)

    return rllist

def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    if linked_list.head is None:
        return False
    
    slow = linked_list.head
    fast = linked_list.head
    
    while fast and fast.next:
        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two nodes
        fast = fast.next.next

        if slow == fast:
            return True
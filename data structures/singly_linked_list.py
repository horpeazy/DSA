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


# ------------------------------------------------ #
#    Nested Linked List                            #
# ------------------------------------------------ #

''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order
        return self._flatten(self.head)
    
    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        
        return merge(node.value, self._flatten(node.next))

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    llist = LinkedList(None)
    list1_ = list1.to_list()
    list2_ = list2.to_list()
    
    for value in sorted(list1_ + list2_):
        llist.append(value)
        
    return llist

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        if self.head is None:
            self.head = Node(value)
            return

        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        return None

def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sorted_array = []
    
    linked_list = SortedLinkedList()
    for value in array:
        linked_list.append(value)
    
    # Convert sorted linked list to a normal list/array
    node = linked_list.head
    while node:
        sorted_array.append(node.value)
        node = node.next
    
    return sorted_array

import math

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    number = 0
    new_arr = []
    
    for num in arr:
        number = (number * 10) + num
    number += 1
    
    while number:
        new_arr = [number % 10] + new_arr
        number = math.floor(number / 10)
        
    return new_arr
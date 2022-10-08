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


# ------------------------------------------------------------------------------ #
# Given a linked list wth integer data,arrange the elements in such a manner that#
# all nodes with even numbers are placed after odd numbers. Do not create any new#
# nodes and avoid using any other data structure. The relative order of even and #
# odd elements must not change.                                                  #
# -------------------------------------------------------------------------------#

"""
parameter: - head of the given linked list
return: - head of the updated list with all even elements placed after odd elements
"""
#--------------------------------------------------#
'''
The Idea: Traverse the given LinkedList, and build two sub-lists: EVEN and ODD. 
For this purpose, we will use four helper references, that denotes starting and 
current ending of EVEN and ODD sub-list respectively. 

1. For each Node in the LinkedList, check if its data is even/odd. 
Change the "next" reference (pointer) of each Node, based on the following rules:
 - First even valued Node will be referenced by head of EVEN sub-list
 - Subsequent even valued Node will be appended to the tail of EVEN sub-list

 - First odd valued Node will be referenced by head of ODD sub-list
 - Subsequent odd valued Node will be appended to the tail of ODD sub-list
 
2. After the loop, append the EVEN sub-list to the tail of ODD sub-list.
'''
#--------------------------------------------------#
def even_after_odd(head):
    
    if head is None:
        return head
    
    # Helper references
    ''' `even_head` and `even_tail` represents the starting and current ending of the "EVEN" sub-list '''
    even_head = None                    
    even_tail = None
    
    ''' `odd_head` and `odd_tail` represents the starting and current ending of the "ODD" sub-list '''
    odd_head = None
    odd_tail = None
    
    current = head                  # <-- "current" represents the current Node. 
    
    # Loop untill there are Nodes available in the LinkedList
    while current:                  # <-- "current" will be updated at the end of each iteration
        
        next_node = current.next    # <-- "next_node" represents the next Node w.r.t. the current Node
        
        if current.data % 2 == 0:   # <-- current Node is even
            
            # Below 
            if even_head is None:   # <-- Make the current Node as the starting Node of EVEN sub-list
                even_head = current     # `even_head` will now point where `current` is already pointing
                even_tail = even_head     
            else:                   # <-- Append the current even node to the tail of EVEN sub-list 
                even_tail.next = current
                even_tail = even_tail.next
        else:
            if odd_head is None:    # <-- Make the current Node as the starting Node of ODD sub-list
                odd_head = current
                odd_tail = odd_head
            else:                   # <-- Append the current odd node to the tail of ODD sub-list 
                odd_tail.next = current
                odd_tail = odd_tail.next
        current.next = None
        current = next_node         # <-- Update "head" Node, for next iteration
    
    if odd_head is None:            # <-- Special case, when there are no odd Nodes 
        return even_head

    odd_tail.next = even_head       # <-- Append the EVEN sub-list to the tail of ODD sub-list
    
    return odd_head

# ------------------------------------------------------------------------------ #
# You are given the head of a linked list and two integers, i and j. You have to #
# retain the first i nodes and then delete the next j nodes. Continue doing so   #
# until the end of the linked list.                                              #
# -------------------------------------------------------------------------------#

# Solution
"""
:param: head - head of linked list
:param: i - first `i` nodes that are to be skipped
:param: j - next `j` nodes that are to be deleted
return - return the updated head of the linked list
"""
'''
The Idea: 
Traverse the Linkedist. Make use of two references - `current` and `previous`.
 - Skip `i-1` nodes. Keep incrementing the `current`. Mark the `i-1`^th node as `previous`. 
 - Delete next `j` nodes. Keep incrementing the `current`.
 - Connect the `previous.next` to the `current`
'''
def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None
    
    # Edge case - Delete 0 nodes
    if j == 0:
        return head
    
    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # Helper references
    current = head
    previous = None
    
    # Traverse - Loop untill there are Nodes available in the LinkedList
    while current:
        
        '''skip (i - 1) nodes'''
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next
        
        '''delete next j nodes'''
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        
        '''Connect the `previous.next` to the `current`''' 
        previous.next = current
    
    # Loop ends
    
    return head

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

# ------------------------------------------------ #
#   Max Sub Array                                  #
# ------------------------------------------------ #

# Solution
'''
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let `current_sum` denotes the sum of a subarray, and `max_sum` denotes the maximum value of `current_sum`.
3. LOOP STARTS: For each element of the array, update the `current_sum` with the MAXIMUM of either:
 - The element added to the `current_sum` (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
4. Return `max_sum`
'''

def max_sum_subarray(arr):
    
    current_sum = arr[0] # `current_sum` denotes the sum of a subarray
    max_sum = arr[0]     # `max_sum` denotes the maximum value of `current_sum` ever
    
    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        
        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        current_sum = max(current_sum + element, element)
        
        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)   
    
    return max_sum

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    sums = []
    
    for i in range(len(arr)):
        sum = arr[i]
        for j in range(i + 1, len(arr)):
            sum += arr[j]
            sums.append(sum)
    return max(sums)


# ------------------------------------------------ #
#   Pascals Triangle                               #
# ------------------------------------------------ #

# Solution

'''
Points to note:
1. We have to return a list.
2. The elements of n^th row are made up of elements of (n-1)^th row. This comes up till the 1^st row. We will follow a top-down approach. 
3. Except for the first and last element, any other element at position `j` in the current row is the sum of elements at position `j` and `j-1` in the previous row. 
4. Be careful about the edge cases, example, an index should never be a NEGATIVE at any point of time. 
'''

def nth_row_pascal(n):
    
    if n == 0:
        return [1]
    
    current_row = [1] # First row
    
    ''' Loop from 1 to n; `i` denotes the row number'''
    for i in range(1, n + 1):
        # Set the `current_row` from previous iteration as the `previous_row`
        previous_row = current_row
        
        # Let's build the fresh current_row gradually
        current_row = [1] # add the default first element at the 0^th index of the `i^th` row
        
        '''Loop from 1 to (i-1); `j` denotes the index of an element with in the `i^th` row'''
        # Example, for 5th row we have considered n=4, 
        # we will iterate index from 1 to 3, because 
        # the default element at the 0^th index has already been added
        for j in range(1, i):
            
            # An element at position `j` in the current row is the 
            # sum of elements at position `j` and `j-1` in the previous row.
            next_number = previous_row[j] + previous_row[j - 1]
            
            # Append the new element to the current_row
            current_row.append(next_number)
            
        current_row.append(1) # append the default last element
    return current_row
def power_of_2(n):
    if n == 0:
        return 1
    
    return 2 * power_of_2(n - 1)

def sum_array_iter(array):
    result = 0
    
    for x in array:
        result += x
    
    return result

def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n == 0:
        return 1  # by definition of 0!
    return n * factorial(n-1)

# Solution
"""
RECURSIVE FUNCTION
Args: input(str): string to be reversed
Returns: a string that us reversed of input
"""
def reverse_string(input):
    
    # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""

    else:
        first_char = input[0]
        
        '''
        The `slice()` function can accept upto the following three arguments.
        - start: [OPTIONAL] starting index. Default value is 0.
        - stop: ending index (exclusive)
        - step_size: [OPTIONAL] the increment size. Default value is 1.
        
        The return type of `slice()` function is an object of class 'slice'. 
        '''
        the_rest = slice(1, None)     # `the_rest` is an object of type 'slice' class
        sub_string = input[the_rest]  # convert the `slice` object into a list
        
        # Recursive call
        reversed_substring = reverse_string(sub_string)
        
        return reversed_substring + first_char
#-------------------------------------------------#
'''
**Time and Space Complexity Analysis**
Each recursive call to the `reverse_string()` function will create 
a new set of local variables - first_char, the_rest, sub_string, and reversed_substring. 
Therefore, the space complexity of a recursive function would always be proportional to the 
maximum depth of recursion stack.  
The time complexity for this function will be  O(k*n), where k is a constant and n is the 
number of characters in the string (depth of recursion stack). 
'''

def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    
    # Termination / Base condition
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        # recursive call, if first and last char are identical, else return False
        return (first_char == last_char) and is_palindrome(sub_input)

# Recursive Solution
def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    # Base case 
    if arr == [9]:
        return [1, 0]
    
    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the last digit is 9.
    else:
        '''Recursive call'''
        # We have used arr[:-1], that means all elements of the list except the last one.
        # Example, for original input arr=[1,2,9], we will pass [1,2] in next call.
        arr = add_one(arr[:-1]) + [0]
        
    return arr


# Recursive Solution 
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
import copy                                # We will use `deepcopy()` function from the `copy` module

def permute(inputList):
    
    # a compound list
    finalCompoundList = []                  # compoundList to be returned 
    
    # Set a base condition to terminate recursion function when the `inputList`
    # cannot be divided further and return the `finalCompoundList`
    
    if len(inputList) == 0:
        finalCompoundList.append([])
        
    else:
        # We are going to split the input into two lists as follows:
        # `first_list` consisting of the first element on the `inputList`
        # `rest_list` consisting the remaining `inputList`
        
        first_element = inputList[0]        # Pick one element to be permuted
        after_first = slice(1, None)        # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list
        
        # Call the recursive function to split the `rest_list` further until it meets the base condition
        # and store the last `finalCompoundList` output into `sub_compoundList` variable
        
        sub_compoundList = permute(rest_list)
        
        # Once the recursion function meets the base condition, we can build the permutation by
        # iterating through all lists of the `compoundList` returned from previous recursive call
        
        for aList in sub_compoundList:
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1): 
                
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)  
                
                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)
                
                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)
                
    return finalCompoundList

# Recursive Solution
"""
Param - input string
Return - compound object: list of all permutations of the input string
"""

def permutations(string):
    return return_permutations(string, 0)
    
def return_permutations(string, index):
    # output to be returned 
    output = list()
    
    # Terminaiton / Base condition
    if index >= len(string):
        return [""]
    
    # Recursive function call
    small_output = return_permutations(string, index + 1)
    
    # Pick a character
    current_char = string[index] 
    
    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:
        
        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):
            
            # Make use of the sub-string of previous output, to create a new sub-string. 
            new_subString = subString[0: index] + current_char + subString[index:]
            output.append(new_subString)

    return output


# Recursive Solution
def keypad(num):
    
    # Base case
    if num <= 1:
        return [""]

    # If `num` is single digit, get the LIST having one element - the associated string
    elif 1 < num <= 9:
        return list(get_characters(num))

    # Otherwise `num` >= 10. Find the unit's (last) digits of `num` 
    last_digit = num % 10
    
    '''Step 1'''
    # Recursive call to the same function with “floor” of the `num//10`
    small_output = keypad(num//10)               # returns a LIST of strings
    
    '''Step 2'''
    # Get the associated string for the `last_digit`
    keypad_string = get_characters(last_digit)   # returns a string
    
    '''Permute the characters of result obtained from Step 1 and Step 2'''
    output = list()

    '''
    The Idea:
    Each character of keypad_string must be appended to the 
    end of each string available in the small_output
    '''
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    
    return output                                # returns a LIST of strings

# Recursive Solution

def deep_reverse(arr):
    
    # Terminaiton / Base condition
    if len(arr) < 1:
        return arr

    reversed_items = []  # final list to be returned
    
    '''Traverse the given list (array) in the reverse direction using extended slice.'''
    # For a given list, sample syntax are - myList[1:10:2], myList[:-1:1], myList[::-1]
    # The first argument is the starting index of the slice (inclusive),
    # second argument is the ending index of the slice (exclusive),
    # third argument is the increment/decrement step size.
    # If we do not specify an argument, it means to consider all elements from that end of the list. 
    for item in arr[::-1]:
        
        # If this item is a list itself, invoke deep_reverse to reverse the items recursively.
        if type(item) is list:
            item = deep_reverse(item)
        
        # append the item to the final list
        reversed_items.append(item)

    return reversed_items

def print_integers(n):
    if n <= 0:
        return
    print(n)
    print_integers(n - 1)

def binary_search(arr, target):
    return binary_search_func(arr, 0, len(arr) - 1, target)

def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    
    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return binary_search_func(arr, start_index, mid_index - 1, target)
    else:
        return binary_search_func(arr, mid_index + 1, end_index, target)

# Recursive Solution
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    # Base condition
    if num_disks == 0:
        return

    # Termination condition
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    

    '''Just think of one iteration, rest the Recursion will take care!'''
    
    # Step 1: Move `num_disks - 1` from source to auxiliary
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    
    # Step 2: Now you are left with the only largest disk at source. 
    # Move the only leftover disk from source to destination
    print("{} {}".format(source, destination))
    
    # Step 3: Move `num_disks - 1` from auxiliary to destination
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')

# Solution

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember: 
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

def all_codes(number):
    if number == 0:
        return [""]
    
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    if remainder <= 26 and number > 9 :
        
        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)
        
        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet
    
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
    
    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)
    
    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    
    return output

# Solution
def subsets(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output

# Solution
## Read input as specified in the question.
## Print output as specified in the question.


def staircase(n):
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

# Solution
def last_index(arr, target):
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    if index < 0:
        return -1
    
    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)

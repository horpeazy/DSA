# Task 1 - Solution
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

# Task 2 - Solution
# Part 1 - A list of all cities in the USA in alphabetic order.
print (1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print (city)

# Part 2 - All cities in Asia, in alphabetic order
print (2)
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append('{} - {}'.format(city, country))
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)

class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    
    def __init__(self, initial_size = 15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient
        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)         # we can use our put() method to rehash
                head = head.next

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

    
    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
                    
        return output

def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)

def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output =  staircase_faster(n - 1, num_dict)
        
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)
            
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output;
    return output

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    '''Input a string that has to be stored in the table.'''
    def store(self, string):
        hv = self.calculate_hash_value(string)   # generate the hash value
        
        if hv != -1:                             # if the string is a new one
            if self.table[hv] != None:           # if the bucket is non-empty 
                self.table[hv].append(string)    # append the string in the list at that bucket
            else:
                self.table[hv] = [string]        # store the string in a new list at that bucket
                
                
    '''Return the hash value if the string is already in the table. Return -1 otherwise.'''
    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        
        # Check collision, and confirm the availability of the given string
        # There might be a case when two strings can generate same hash value.
        # However, one string is present, and other one is not.
        if self.table[hv] != None:
            if string in self.table[hv]:
                return hv
        
        return -1                                # otherwise

    '''Helper function to calulate a hash value from a string.'''
    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value

def pair_sum_to_target(input_list, target):
    
    # Create a dictionary.
    # Each element of the input_list would become a "key", and
    # the corresponding index in the input_list would become the "value"
    index_dict = dict()
    
    # Traverse through the input_list
    for index, element in enumerate(input_list):
        
        # `in` is the way to test for the existence of a "key" in a dictionary
        if (target - element) in index_dict:
            
            # Return the TWO indices that sum to the target
            return [index_dict[target - element], index]

        index_dict[element] = index

    return [-1,-1]              # If the target is not achieved


def longest_consecutive_subsequence(input_list):
    
    # Create a dictionary.
    # Each element of the input_list would become a "key", and
    # the corresponding index in the input_list would become the "value"
    element_dict = dict()

    # Traverse through the input_list, and populate the dictionary
    # Time complexity = O(n) 
    for index, element in enumerate(input_list):
        element_dict[element] = index

    # Represents the length of longest subsequence
    max_length = -1
    
    # Represents the index of smallest element in the longest subsequence
    starts_at = -1  

    # Traverse again - Time complexity = O(n) 
    for index, element in enumerate(input_list):

        current_starts = index
        element_dict[element] = -1         # Mark as visited

        current_count = 1                  # length of the current subsequence

        '''CHECK ONE ELEMENT FORWARD'''
        current = element + 1              # `current` is the expected number

        # check if the expected number is available (as a key) in the dictionary,
        # and it has not been visited yet (i.e., value > 0)
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        while current in element_dict and element_dict[current] > 0:
            current_count += 1             # increment the length of subsequence 
            element_dict[current] = -1     # Mark as visited
            current = current + 1          

            
        '''CHECK ONE ELEMENT BACKWARD'''
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        current = element - 1             # `current` is the expected number

        while current in element_dict and element_dict[current] > 0:    
            current_starts = element_dict[current]         # index of smallest element in the current subsequence
            current_count += 1                             # increment the length of subsequence 
            element_dict[current] = -1
            current = current - 1

        '''If length of current subsequence >= max length of previously visited subsequence'''
        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts            # index of smallest element in the current (longest so far) subsequence
            max_length = current_count            # store the length of current (longest so far) subsequence


    start_element = input_list[starts_at]          # smallest element in the longest subsequence

    # return a NEW list starting from `start_element` to `(start_element + max_length)` 
    return [element for element in range(start_element, start_element + max_length)]



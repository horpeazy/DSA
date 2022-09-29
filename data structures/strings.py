
def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    new_string = ""
    for c in our_string:
        new_string = c + new_string
    
    return new_string

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    str1_ = []
    str2_ = []
    
    for c in str1:
        if c != " ":
            str1_.append(c.lower())
    for c in str2:
        if c != " ":
            str2_.append(c.lower())
            
    if sorted(str1_) == sorted(str2_):
        return True
    return False

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    my_string = ""
    word_array = our_string.split()
    len_ = len(word_array)
    for i in range(len_):
        new_word = ""
        for c in word_array[i]:
            new_word = c + new_word
        my_string += new_word
        if i != (len_ - 1):
            my_string += " "
    
    return my_string

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    if len(str1) != len(str2):
        return None
    
    dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dist += 1
    
    return dist

# Plan
# Func finds two items in weights_list whose sum equals the limit
    # returns a tuple of integers --> the  2 integers are the index of 2 weights in the weights list 
    # The higher valued index should be placed in the zeroth index and the smaller index should be placed in the first index
    #requires sort, and reverse=True 
# One of tests has duplicate numb, need another dict to store duplicate list elements, if the remainder weight we search for is the same as the element we minused from the limit, then we search the dup. dict 

# Weights list index ->  0   1   2   3   4
    # e.g --> weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    # weights_dict --> {"4": 0, "6": 1, "10": 2, "15": 3, "16": 4}
     # output: [3, 1] --> these two integers are the indices of weights 15 and 6 (sum is 21)


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
     # Store the weight list elements as keys in this dict, and their index positions as the value to the keys (as we need to return these index pos if we find two elements that make the limit)
    weights_dict = {}

    # Duplicate key dict, if there are two of the same elements in the weights list, we need to store the second element in here as own key, as dict doesnt allow duplicate keys 
    duplicate_key_dict = {}

    # Go over weights list 
    for i in range(length):
        # If the item in the list is not a key in the weights_dict: make the item a key and its index in the list as its value 
        if weights[i] not in weights_dict:
            weights_dict[weights[i]] = i
            # print(weights_dict)
        # If the item in the list is already a key
        else:
        # Add the duplicate item as a key to duplicate dict
        # As we still need to store the duplicate element to check if it can make the limit
            duplicate_key_dict[weights[i]] = i
            # print(duplicate_key_dict)

    # Loop over length of weights list again
    for i in range(length):
    # For each item in the list, subtract the limit from it so we get a remainder, which for all the items, we can use these remainder weights to check if it is stored in either dict, if it is, then we know we have made the limit
        remainder_weight = limit - weights[i]
        # Store the value of the current item's weight we are on 
        first_weight_element = weights[i]
        # print(first_weight_element)
    

        # If any of the remainder_weights is a key in our weights_dict (each loop for each item in list checks this  condition)
        if remainder_weight in weights_dict:
           # Check for duplicates, if these two are equal =  duplicate elements in weights list, then we go to else 
            if remainder_weight != first_weight_element:
            # If not, we have found two items in the list whose weights sum together to equal the limit 
            # need to access that remainder_weight key's value to get its index to return and access the index of the current element (element we subtracted from the limit
            # Make them into a tuple 
                elements_to_add = (weights_dict[remainder_weight], weights_dict[first_weight_element])
        # Convert to a list to sort
                elements_to_sort = list(elements_to_add)
        # We need to sort them, by reverse, so larger index is at 0th index
                elements_to_sort.sort(reverse=True)
        # Convert sorted list back into tuple
                make_tuple = tuple(elements_to_sort)
            # print(make_tuple)
                return make_tuple
            
            # If remainder and current element are the same, means these are duplicate values in the list, so our remainder element will be in the duplicates_dict instead
            # Access that remainder's key value in dup_dict which tells us its position in the weights list, alongside the current element we are on which is in the weights_dict 
            else:
                if remainder_weight in duplicate_key_dict:
                    e_to_add = (duplicate_key_dict[remainder_weight], weights_dict[first_weight_element])
                    e_to_sort = list(e_to_add)
                    e_to_sort.sort(reverse=True)
                    m_tuple = tuple(e_to_sort)
                    return m_tuple

    # If there is no remainder_weight stored in either the weights_dict or duplicates_dict, it means the limit cannot be reached          
    else:
        return None
   


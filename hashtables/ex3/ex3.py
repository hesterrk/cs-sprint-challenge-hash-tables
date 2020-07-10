# PLAN 
# Have a dict, all elements in nested arrays, one to hold elements we have encountered in all nested arrays, keep count of each element we encounter as value
# The count will let us know how many elements have appeared the same number times as the length of the big array, which means they are all presented in each of the big array's nested arrays 
# List to append common elements found in all arrays 



def intersection(arrays):
    """
    YOUR CODE HERE
    """
    
    #Stores all the elements in all of the nested arrays, with their count 
    #Key is item, value is count
    unique_el_dict = {}
    # List returns the elements present in all nested arrays
    common_el_list = []

    # Getting each nested array out of the big array
    for nested_array in arrays:
        # Getting each element out of each nested array
        for item in nested_array:
            # print(item)
            # Check if the item isnt already a key in the dict
            if item not in unique_el_dict:
                # Set count to 1 as we've just seen it
                unique_el_dict[item] = 1
            # Increment as we've seen it again
            else:
                unique_el_dict[item] += 1

    
    # Go through our dict, check if the count for each key(element) is equal to the length of the nested lists in the big array
    # which means the element is present in all nested lists

    # for item in unique_el_dict:
    #     if unique_el_dict[item] == len(arrays):
    #     # Append each key that is present in all nested arrays to our array
    #         common_el_list.append(item)
    #         print(common_el_list)
    # return common_el_list


    # Same as above, for each key in our unique_el_dict, if its count (value) is same as nested array length then we return the key (element) in this list
    intersec_result = [item for item in unique_el_dict if unique_el_dict[item] == len(arrays)]
    return intersec_result
    









if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

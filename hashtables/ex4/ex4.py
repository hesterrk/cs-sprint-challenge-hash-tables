# Plan:
# Return the positive integers that have equivalent negative integers
# We can do a count, if count is 2 for any key in our dict, then we know theres a matching pos and neg pair
# to check pos and neg, make the neg a positive using: abs() on the key 


def has_negatives(a):
    """
    YOUR CODE HERE
    """

    # Stores our list items as key and their count as value
    num_count = {}
    # List that contains the numbers that have both pos and neg
    pos_neg = []

    # For each item in our list
    for item in a:
        # convert any minus elements in list to positive for the count 
        item = abs(item)
        # If element in list is not a key in num_count dict
        if item not in num_count:
            # Make it a key and assign count to 1
            num_count[item] = 1
        else:
            # Increment count
            num_count[item] +=1

    # For each key in num_count dict
    for item in num_count:
        # If any key has the value (count) of '2' then it must have both a positive and negative integer in the input list
        if num_count[item] == 2:
            # add these keys to pos_neg list
            pos_neg.append(item)
    return pos_neg







if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

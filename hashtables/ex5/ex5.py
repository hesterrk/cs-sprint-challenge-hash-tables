# Plan
# We want to store each string element in files list as key in dict, but the last bit of the element as that contaisn the file pathname
    # we want to store the full string element as the value 
    # if the filepath key already exists (if there are string elements in files list that have different paths but have the same filename as the last section), we can simply append the full filepath to the existing value it already olds, which means we get a list of string elements from files list that all have the same filename
    # as we want to return the value (full string element full paths) as our result if the filepathname matches the queries in queries list 
# We can use our dict as a lookup for when we go through each item in queries list and check if there is a key for each item in queries list in the dict, if there is that means we can return the full paths that match that filename 
# To get the keys for our dict, we need to split each element in files list on the '/' and return last element [-1]



# Files: list of full paths to files
# Queries: list of filenames to query
def finder(files, queries):
    """
    YOUR CODE HERE
    """

    # Dict where the keys will be the filenames (end of each path string) in the files list
        # values will be the corresponding string element (full path) in files list
    file_name_to_path = {}
    
    # List to add the value from dict(which stores the full paths from files list) based on matching the query strings in query list to the keys in the dict which have identical filenames
    match_list = []


    # For each element (string) in the files list we want to access the last section of the string which is the filename
        # Split each element in this array, split it on the '/': file.split('/')
        # Get the last section 
    for file in files:
        # print(file, 'file')
        # Now we have reference to each filename of every element in files array --> use as the key in our file_name_to_path dict
        split_last_string = file.split('/')[-1]

        # Need to consider duplicate filename keys here, as elements in files array have the same filename at the end
            # If there is not yet a filename key in the dict we add the filename as the key
            # For its value we create a list, incase of duplicate keys (filename) as we will still want to get the value of the duplicate key to store
            # Assign the value of the current file string from files list we are on in the loop
        if split_last_string not in file_name_to_path:
            file_name_to_path[split_last_string] = [file]

        # For duplicate keys (filename) is already there, we append their value to the exisiting key we have in the dict
         # the value being the current element in the files list we are on
        else:
            file_name_to_path[split_last_string].append(file)

        

    # Use our dict keys to match the elements in queries list
    # The matching ones, return those key's value from the dict which are the filepath from files list
    for query in queries:
        # For every query element, we check if we have a key in the dict named the same  
        if query in file_name_to_path:
            #  if yes, it matches, return that key's value(s)
            # Add each of the matching key's values as we go through loop through query list to match_list
            # The bigger inputs have nested lists, want to add all content from nested lists into match_list, use extend()
            match_list.extend(file_name_to_path[query])
            # print(match_list)

    return match_list



 









if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

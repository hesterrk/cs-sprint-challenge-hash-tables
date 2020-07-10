
# PLAN 
# Source: start airport -> string
# Destination is next airport -> string
# The ticket for your first flight has a destination with a source of NONE, and the ticket for your final flight has a source with a destination of NONE, we need to keep last dest. as NONE but not include NONE at start 
# Return: an array of strings
# The ticket is an object which contains a source and destination 
# Dict --> source is the key and destination is value
# When putting current destination in route list, use the element before it as the key to find the next destination in the dict



#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

# Create route_list array: will be our final list output with the all destinations for the entire trip 
# The list is initialised with the length of the tickets array (len of trip) 
    route_list = [None] * length

    # Ticket dictionary containing source(start location) as key, and destination its value
    ticket_dict = {}

    # For each ticket object in the tickets array(input)
    for ticket in tickets:
        # We want to assign the first ticket's destination to the first element in route_list
            # If the ticket object's source is "NONE", we know its the first ticket
        # We dont add this to the ticket_dict because the following ticket to this one will already have this ticket's destination as its source + we dont want None as the first element in our ticket_list 
        if ticket.source == "NONE":
            route_list[0] = ticket.destination

        # If the ticket object's source is not none 
        # Add the ticket's source as the key in the ticket_dict and the ticket's destination as the value
        ticket_dict[ticket.source] = ticket.destination
        
    # Start loop at first index in the length of ticket_list as we already have the first item at 0th index
    for i in range(1, length):
        # We want to fill out route_list at each index (starting from index 1) with destinations
        # We use the previous element in the route_list as the key to access our ticket_dict's value for that key, as this will give us the next destination 
        # First time round: i = 1, so i-1 in route_list is our first destination, so we use that as the key to get the next destination
        # We get the last destination we just added to list as the key to access its next destinaton (value) in the dict 
        route_list[i] = ticket_dict[route_list[i-1]]

    # Return full destination array
    return route_list


  


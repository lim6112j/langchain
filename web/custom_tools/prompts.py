OSRM_GET_ROUTES = """
This tool is a wrapper around CielApp's fetching API, useful when you need to find optimized routes between two locations on the map.
The input to this tool is a dictionary specifying the start and destination location, and will be passed into CielApp's `get_routes` function.
For example, to create a CielApp's input dictionary with the start location longitude 127.444, latitude 37.11 and the destination location longitude 127.22, latitude 37.22, You would pass in the following string:
{{"locations": "127.444,37.11;127.22,37.22"}}
"""
SEND_RESPONSE_CIELAPP = """
This tool is a wrapper around CielApp's write API, useful when you need to create or post a message.
The input to this tool is a dictionary specifying the fields of the Ciel api message, and will be passed into CielApp's `send_response` function.
For Example, to create a CielApp message with the text "hello world", you would pass in the following string:
{{"message": "hello world"}}
"""

OSRM_GET_ROUTES = """
This tool is a wrapper around OSRM's fetching routes api, useful when you need to find optimized routes between two locations on the map.
start and destination location is needed for this tool and will call into OSRM's `get_routes` function.
"""
SEND_RESPONSE_EXTERNAPP = """
This tool is a wrapper around ExternApp's write API, useful when you need to create or post a extern message.
The input to this tool is a dictionary specifying the fields of the ExterApp message, and will be passed into ExternApp's `send_response` function.
For Example, to create a ExternApp message with the text "hello world", you would pass in the following string:
{{"message": "hello world"}}
"""

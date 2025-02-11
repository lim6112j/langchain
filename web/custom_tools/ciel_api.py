import os
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Extra, root_validator
from prompts import (
    OSRM_GET_ROUTES,
    SEND_RESPONSE_CIELAPP
)
from langchain.utils import get_from_dict_or_env
import http.client
from dotenv import load_dotenv
load_dotenv()
class CielApiWrapper(BaseModel):
    """ Wrapper for Ciel API. """

    # Define the fields that will be part of the request or response
    # Assuming you might fetch this from environment variables
    # cielapi: Any
    # List of operations that this tool can perform
    operations: List[Dict] = [
        {
            "mode": "get_routes",
            "name": "get the routes",
            "description": OSRM_GET_ROUTES,
        },
        {
            "mode": "send_response",
            "name": "send a message to the ciel api",
            "description": SEND_RESPONSE_CIELAPP,
        }
    ]
    # Example endpoint, adjust accordingly
    endpoint: str = "http://localhost:5001/route/v1/driving/"

    class Config:
        """ Configuration for this pydantic object. """
        extra = Extra.forbid

    def list(self) -> List[Dict]:
        return self.operations

    @root_validator(skip_on_failure=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """ Validate that api key and python package exists in environmewnt. """
        # bot_token = get_from_dict_or_env(values, "bot_token", "SLACK_BOT_TOKEN")
        # try:
        #     from slack_sdk import WebClient
        # except ImportError
        return values

    def run(self, mode: str, text: Optional[str]) -> str:
        """ Based on the mode from the caller, run the appropriate function. """
        if mode == "get_routes":
            return self.get_routes(text)
        elif mode == "send_response":
            assert text is not None, "Text must be provided."
            return self.send_response(text)
        else:
            raise ValueError("Invalid mode passed. {mode}")

    def get_routes(self, text: str) -> str:
        """ Get route information from the API. """
        import json
        params = json.loads(text)
        fields = dict(params)
        OSRM_API = os.getenv("OSRM_API")
        # http://localhost:5001/route/v1/driving/127.919323,36.809656;128.080629,36.699223?steps=true
        conn = http.client.HTTPConnection(OSRM_API, 5001)
        routes = conn.request("GET", "/route/v1/driving/" + fields["locations"] + "?steps=true")
        if not routes:
            return "No routes found."
        # response = "\n".join([f"{route['id']}: {route['title']}" for route in routes])
        return f"Available routes:\n{routes}"
    def send_response(self, text: str) -> str:
        """ Send a response back to the caller. """
        # Here you can implement logic to handle and respond to the request.
        return f"send str successfully : {text}"

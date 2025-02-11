from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Extra, root_validator
from prompts import (
    OSRM_GET_ROUTES,
    SEND_RESPONSE_EXTERNAPP
)
from langchain.utils import get_from_dict_or_env


class ExternAppWrapper(BaseModel):
    """ Wrapper for ExternApp API. """

    # Define the fields that will be part of the request or response
    # Assuming you might fetch this from environment variables
    externapp: Any
    # List of operations that this tool can perform
    operations: List(Dict) = [
        {
            "mode": "get_routes",
            "name": "get the routes",
            "description": OSRM_GET_ROUTES,
        },
        {
            "mode": "send_response",
            "name": "send a message to the external app",
            "description": SEND_RESPONSE_EXTERNAPP,
        }
    ]
    # Example endpoint, adjust accordingly
    endpoint: str = "http://localhost:3001/posts"

    class Config:
        """ Configuration for this pydantic object. """
        extra = Extra.forbid

    def list(self) -> List[Dict]:
        return self.operations

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """ Validate that api key and python package exists in environmewnt. """
        # bot_token = get_from_dict_or_env(values, "bot_token", "SLACK_BOT_TOKEN")
        # try:
        #     from slack_sdk import WebClient
        # except ImportError
        return values

    def run(self, mode: str, ; OSRM_GET_ROUTES)

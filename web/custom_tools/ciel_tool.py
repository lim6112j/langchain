from langchain.tools.base import BaseTool
from typing import Optional
from ciel_api import CielApiWrapper
from pydantic import Field
class CielTool(BaseTool):
    api_wrapper: CielApiWrapper = Field(default_factory=CielApiWrapper)
    mode: str
    name:str = ""
    description:str = ""
    def _run(self, instructions: Optional[str]) -> str:
        """ Use the Ciel Api to run an operation """
        return self.api_wrapper.run(self.mode, instructions)
    async def _arun(self, _: str) -> str:
        """Use the Ciel API to run an operation """
        raise NotImplementedError("CielTool does not support async")

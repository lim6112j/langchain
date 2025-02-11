from langchain.tools import BaseTool
from langchain_core.tools.base import BaseToolkit
from ciel_tool import CielTool
from ciel_api import CielApiWrapper
from typing import List
class CielToolKit(BaseToolkit):
    """Ciel Toolkit"""
    tools: List[BaseTool] = []
    @classmethod
    def from_ciel_api_wrapper(cls, ciel_api_wrapper: CielApiWrapper) -> "CielToolKit":
        operations = ciel_api_wrapper.list()
        tools = [
            CielTool(
                name=operation["name"],
                description=operation["description"],
                mode=operation["mode"],
                api_wrapper=ciel_api_wrapper,
            )
            for operation in operations
        ]
        return cls(tools=tools)
    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit"""
        return self.tools

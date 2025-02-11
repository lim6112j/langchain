from langchain.agents import AgentType
from langchain.agents import initialize_agent
from ciel_toolkit import CielToolKit
from langchain_openai import OpenAI
from ciel_api import CielApiWrapper

from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(temperature=0)
cielapiwrapper = CielApiWrapper()
toolkit = CielToolKit.from_ciel_api_wrapper(cielapiwrapper)
tools = toolkit.get_tools()

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
agent.run("get the routes of two locations in seoul")

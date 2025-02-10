import os
# import streamlit as st
# from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENWEATHERMAP_API_KEY"] = ""
# weather = OpenWeatherMapAPIWrapper()
# weatherData = weather.run("London,GB")
# print(weatherData)
llm = OpenAI(temperature=0)
tools = load_tools(["openweathermap-api"], llm)
agent_chain = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent_chain.run("What's the weather like in London?")

import os
# import streamlit as st
# from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import OpenAI
from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from dotenv import load_dotenv
load_dotenv()
# weather = OpenWeatherMapAPIWrapper()
# weatherData = weather.run("London,GB")
# print(weatherData)
llm = OpenAI(temperature=0)
tools = load_tools(["openweathermap-api"], llm)
agent_chain = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent_chain.run("What's the weather like in London?")
meteo_chain = APIChain.from_llm_and_api_docs(
    llm,
    open_meteo_docs.OPEN_METEO_DOCS,
    verbose=True,
    limit_to_domains=["https://api.open-meteo.com/"],
)
meteo_chain.run(
    "What is the weather like right now in Munich, Germany in degrees Fahrenheit?"
)

import os
from langchain_ollama import OllamaLLM
from langchain.agents import AgentType, initialize_agent, load_tools
from dotenv import load_dotenv
load_dotenv()
llm = OllamaLLM(model="llama2")
tools = load_tools(["openweathermap-api"])
agent_chain = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent_chain.invoke("What's the weather like in London?")

import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_anthropic import ChatAnthropic
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)
#llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
llm = OpenAI(temperature=0)
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()
from PIL import Image
try:
    d = graph.get_graph().draw_mermaid_png()
    open('output.png', 'wb').write(d)
    img = Image.open('output.png')
    img.show()
except Exception:
    # This requires some extra dependencies and is optional
    print(f"image exception:{Exception.with_traceback()}")
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1])
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("You:" + user_input)
        stream_graph_updates(user_input)
        break

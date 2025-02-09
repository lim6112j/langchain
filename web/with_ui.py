# with ui , https://www.youtube.com/watch?v=MlK6SIjcjE8
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.utilities import WikipediaAPIWrapper
# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """multiply two numbers"""
    return a * b


class SearchInput(BaseModel):
    query: str = Field(description="should be a search query")


@tool("search-tool", args_schema=SearchInput, return_direct=True)
def search(query: str) -> str:
    """Look up online"""
    return "langchain"


print(search.name)
print(search.description)
# print(search.args)
print(search.return_direct)

st.title("Ciel AI Agent")
prompt = st.text_input('plug in your prompt here')

title_template = PromptTemplate(
    input_variable=['destination'],
    template="""show me the route from current
 location to {destination} using google map"""
)
script_template = PromptTemplate(
    input_variable=['script', 'wikipedia_research'],
    template="""write me a youtube video script based on
     this destination DESTINATION: {script}
      while leveraging this wikipedia research:{wikipedia_research}"""
)
llm = OllamaLLM(model="llama2")
title_chain = LLMChain(llm=llm, prompt=title_template,
                       verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template,
                        verbose=True, output_key='script')
wiki = WikipediaAPIWrapper()
if prompt:
    title = title_chain.run(destination=prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(script=title,
                              wikipedia_research=wiki_research)
    st.write(title)
    # st.write(script)
    # st.write(wiki_research)

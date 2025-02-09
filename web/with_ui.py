# with ui , https://www.youtube.com/watch?v=MlK6SIjcjE8
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, APIChain
from langchain.utilities import WikipediaAPIWrapper
# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool
from langchain.chains import LLMChain, LLMRequestsChain
from langchain_core.prompts import PromptTemplate

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

web_request = """Between >>> and <<< are the raw response text from localhost.
Extract the title or say "not found" if the information is not contained.
Use the format
Extracted:<title or "not found">
>>> {requests_result} <<<
Extracted:"""
web_request_template = PromptTemplate(
    input_variable=["query", "requests_result"],
    template = web_request
)
llm = OllamaLLM(model="llama2")
title_chain = LLMChain(llm=llm, prompt=title_template,
                       verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template,
                        verbose=True, output_key='script')
wiki = WikipediaAPIWrapper()
web_request_chain = LLMRequestsChain(llm_chain=LLMChain(llm=llm, prompt=web_request_template))
if prompt:
    # title = title_chain.run(destination=prompt)
    # wiki_research = wiki.run(prompt)
    # script = script_chain.run(script=title,
    #                           wikipedia_research=wiki_research)
    question = "What are the Three (3) biggest countries, and their respective sizes?"
    inputs = {
        "query": prompt ,
        "url": "http://localhost:3001/posts/" + prompt.replace(" ", "+")
    }
    web_result = web_request_chain(inputs)
    # st.write(title)
    st.write(web_result)
    # st.write(script)
    # st.write(wiki_research)

    # import gmaps
    # gmaps.configure(api_key='AIzaSyAQkoRaEefK8pUcmb8D46DNfGZwREwcUZ0')
    # new_york = (40.75, -74.00)
    # map = gmaps.figure(center=new_york, zoom_level=12)
    # from ipywidgets import embed
    # snippet = embed.embed_snippet(views=map)
    # html = embed.html_template.format(title="", snippet=snippet)
    #
    # import streamlit.components.v1 as components
    # components.html(html, height=500,width=500)

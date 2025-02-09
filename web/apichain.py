from langchain_ollama import OllamaLLM
import streamlit as st
from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
llm = OllamaLLM(model="llama2")
chain = APIChain.from_llm_and_api_docs(
    llm,
    open_meteo_docs.OPEN_METEO_DOCS,
    verbose=True,
    limit_to_domains=["https://api.open-meteo.com/"]
)
print(open_meteo_docs.OPEN_METEO_DOCS[:500])
st.title("Ciel AI Agent")
prompt = st.text_input('plug in your prompt here')
if prompt:
    result = chain.run(
        "What is the weather like right now in Munich, Germany in degrees Fahrenheit?"
        )
    st.write(result)

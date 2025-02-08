from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
url = "https://namu.wiki/w/%EC%94%A8%EC%97%98%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0"
question = "씨엘모빌리티의 경쟁력에 대해 얘기해줘"
loader = WebBaseLoader(url)
docs = loader.load()
# print(docs)
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
embeddings = OllamaEmbeddings(model="llama2")
vector = FAISS.from_documents(documents, embeddings)
output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_template("""Answer the following question
 based only on the provided context:

<context>
{context}
</context>

Question: {input}""")
llm = OllamaLLM(model="llama2")
document_chain = create_stuff_documents_chain(llm, prompt)
document_chain.invoke({
    "input": question,
    "context": [Document(page_content="""langsmith can let
         you visualize test results""")]
})
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
response = retrieval_chain.invoke({"input": question})
print(response["answer"])

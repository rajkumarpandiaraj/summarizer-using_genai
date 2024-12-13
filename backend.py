
from langchain.chains.summarize import load_summarize_chain

from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_ollama import OllamaLLM

from langchain.docstore.document import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from PyPDF2 import PdfReader
import os


os.environ["GOOGLE_API_KEY"] = 'AIzaSyBf7YCm8dK5QkFcJbPJmDDe4PVdpXyfPeY'



def process_text(text) :
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.create_documents(text)
    return chunks

def summarizer(pdf) :
    print('going to summarize')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''

        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        
        print('process')
        # chunks = process_text(text)
        docs = [Document(page_content=text)]

        print('processed')
       
        # llm = OllamaLLM(model="llama3.2")
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            # other params...
        )

        chain = load_summarize_chain(
            llm,
            chain_type='stuff',
            verbose=False
        )
        print('chain')
        summary = chain.invoke(docs)

        return summary['output_text']

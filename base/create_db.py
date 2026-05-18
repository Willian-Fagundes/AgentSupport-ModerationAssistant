from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import time


load_dotenv(override=True)

BASE = "base"

def create_db():
    #load_docs
    docs = load_docs()
    print(docs)
    #chunk_data
    chunks = chunk_data(docs)
    #vetorize
    vetorize_chunks(chunks)

def load_docs():
    loader = PyPDFDirectoryLoader(BASE, glob = '*.pdf')
    docs = loader.load()
    return docs

def chunk_data(docs):
    separate = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 150,
        length_function = len,
        add_start_index = True,

    )
    chunks = separate.split_documents(docs)
    return chunks

def vetorize_chunks(chunks):
    embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    persist_directory = "DB"
    batch_size = 50  # menor batch

    first_batch = chunks[:batch_size]
    print(f"Initializing DB with the first {len(first_batch)} chunks...")
    db = Chroma.from_documents(
        documents=first_batch,
        embedding=embedding,
        persist_directory=persist_directory
    )
    print("Waiting 15 seconds...")
    time.sleep(15)  # espera após o primeiro batch também

    for i in range(batch_size, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        print(f"Processing chunks {i} to {i + len(batch)}...")
        db.add_documents(batch)
        print("Waiting 35 seconds to avoid rate limits...")
        time.sleep(35)  # sempre espera, não só quando tem próximo batch

    print("DB Criado")
    print(f"Total de chunks: {db._collection.count()}")

create_db()

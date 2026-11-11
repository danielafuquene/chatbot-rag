from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

# Cargar PDFs
docs = []

for pdf_file in Path("pdf").glob("*.pdf"):
    print(f"Cargando {pdf_file.name}")

    loader = PyPDFLoader(str(pdf_file))
    docs.extend(loader.load())

print(f"Paginas cargadas: {len(docs)}")

# Crear chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

print(f"Chunks creados: {len(chunks)}")

print(os.getenv("OPENAI_API_KEY"))

# Crear embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Guardar en Chroma
Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="features/knowledge/vector_db"
)

print("Base vectorial creada")
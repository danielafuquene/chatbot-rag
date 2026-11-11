from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="features/knowledge/vector_db",
    embedding_function=embeddings
)

def buscar_contexto(pregunta):
    resultados = db.similarity_search(
        pregunta,
        k=3
    )

    return "\n".join(
        [doc.page_content for doc in resultados]
    )
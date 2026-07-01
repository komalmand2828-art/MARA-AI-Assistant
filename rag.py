from pypdf import PdfReader
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from langchain_community.vectorstores import (
    FAISS
)
from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)
# ---------------------------
# READ SINGLE PDF
# ---------------------------
def read_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text
# ---------------------------
# READ MULTIPLE PDFs
# ---------------------------
def read_multiple_pdfs(pdf_files):
    all_text = ""
    for pdf in pdf_files:
        try:
            text = read_pdf(pdf)
            all_text += text
        except Exception:
            pass
    return all_text
# ---------------------------
# SPLIT INTO CHUNKS
# ---------------------------
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)
    return chunks
# ---------------------------
# EMBEDDINGS
# ---------------------------
def get_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return embeddings
# ---------------------------
# CREATE VECTOR DATABASE
# ---------------------------
def create_vector_db(text):
    chunks = split_text(text)
    embeddings = get_embeddings()
    vector_db = FAISS.from_texts(
        chunks,
        embedding=embeddings
    )
    return vector_db
# ---------------------------
# RETRIEVE CONTEXT
# ---------------------------
def retrieve_context(
    vector_db,
    query,
    k=3
):
    docs = vector_db.similarity_search(
        query,
        k=k
    )
    context = "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )
    return context
# ---------------------------
# RETURN SOURCE DOCUMENTS
# ---------------------------
def retrieve_docs(
    vector_db,
    query,
    k=3
):
    docs = vector_db.similarity_search(
        query,
        k=k
    )
    return docs
# ---------------------------
# KNOWLEDGE STATS
# ---------------------------
def count_chunks(text):
    chunks = split_text(text)
    return len(chunks)
# ---------------------------
# PDF INFORMATION
# ---------------------------
def get_pdf_stats(pdf_files):
    total_pages = 0
    total_pdfs = len(pdf_files)
    for pdf in pdf_files:
        try:
            reader = PdfReader(pdf)
            total_pages += len(
                reader.pages
            )
        except Exception:
            pass
    return {
        "pdfs": total_pdfs,
        "pages": total_pages
    }
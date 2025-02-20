from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS 

file_directory = "file/ProjectProposal.pdf"


def upload_file(file):
    with open(file_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_file(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

file = load_file(file_directory)
def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    texts = splitter.split_documents(documents)
    return texts

text_chunks = split_text(file)
print("total chunk:", len(text_chunks))
# print(len(text_chunks))

ollama_model = "deepseek-r1:1.5b"

def get_model(model = ollama_model):

    embedding = OllamaEmbeddings(model=ollama_model)
    return embedding

FAISS_DB_PATH = "database/faissdb"

faiss_db = FAISS.from_documents(text_chunks, get_model(ollama_model))
faiss_db.save_local(FAISS_DB_PATH)

# def create_faiss_index(texts, model):
#     embeddings = model.embed_documents(texts)
#     index = FAISS.from_embeddings(embeddings, dim=model.embedding_dim)
#     return index

# def save_faiss_index(index, db_path):
#     index.save(db_path)
#     print("faiss index saved successfully!")

# def load_faiss_index(db_path):
#     index = FAISS.load_from_checkpoint(db_path)
#     print("faiss index loaded successfully!")
#     return index

# model = get_model(ollama_model)

# if not os.path.exists(FAISS_DB_PATH):
#     index = create_faiss_index(text_chunks, model)
#     save_faiss_index(index, FAISS_DB_PATH)


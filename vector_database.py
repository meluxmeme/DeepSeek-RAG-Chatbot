from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS 

file_directory = "file/SENG637-03.pdf"


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

import sys
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

sys.stdout.reconfigure(encoding="utf-8")

loader = DirectoryLoader(
    path=r"D:\ML\GenAI\Dharm\Small Projects🛠️🛠️🔧\DocuRAG📃\Data",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
    show_progress=True
)

docs = loader.load()

print("Total Pages : ",len(docs))

for doc in docs:
    print(doc.page_content)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=20
)

chunks = splitter.split_documents(docs)

print("Total Chunks:", len(chunks))

for chunk in chunks:
    print(chunk.page_content)
    print(chunk.metadata)
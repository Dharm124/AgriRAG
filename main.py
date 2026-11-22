from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path=r"D:\ML\GenAI\Dharm\Small Projects🛠️🛠️🔧\AgriRAG📄🌾\Data", glob = "*.pdf",loader_cls=PyPDFLoader,show_progress = True
)

docs = loader.load()

print("Total Pages : ",len(docs))
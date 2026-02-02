# Tutorials from https://www.youtube.com/watch?v=LK-OyelN9MU&list=PLNIQLFWpQMRUMjxfe8o6g3uzJ6LH_VotY&index=3

# venv is virtual environment
# Multiple documents cannot be given to LLMs to remeber and retrieve the data - becuase most of them will have less memory.
# So RAG is used. 
# RAG ingestion pipeline:
# Multiple documents -> made into chunks -> Use Embedding model to converts chunks into vectors. Vectors have dimensions (semantic knowledge about the chunk). -> Store vectors in vector database.
# Retrieval pipeline:
# User query -> USE THE SAME EMBEDDING MODEL AND THE # OF DIMENSIONS USED FOR INGESTION MODEL FOR THE USER QUERY -> user query vector -> Retriever gets the vectors from teh vector database that are closer to user query vector and returns their respective chunks -> chunks are summarized as an answer. 
import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader # Used to read files from a directory.
from langchain_text_splitters import CharacterTextSplitter # Used for creating chunks
from langchain_openai import OpenAIEmbeddings # Embedding model 
from langchain_chroma import Chroma # Vector database. Chroma can be hosted locally.
from dotenv import load_dotenv # for environment variables

load_dotenv()

def load_documents(docs_path="docs"):

    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"The directory {docs_path} does not exist. Please create it and add your company files.")

    # Load all text files from docs directory
    loader = DirectoryLoader(
        path=docs_path,
        glob="**/*.txt", # only look for txt files.
        loader_cls=TextLoader # since we are using text files textloader class is used. Pdfs and other file types have other classes.
    )

    documents=loader.load() # Gives the langchain documents.

    if len(documents) == 0:
        raise FileNotFoundError(f"No txt files found in {docs_path}. Please add your company files.")
    
    for i, doc in enumerate(documents[:2]):  # Show first 2 documents
        print(f"\nDocument {i+1}:")
        print(f"  Source: {doc.metadata['source']}")
        print(f"  Content length: {len(doc.page_content)} characters")
        print(f"  Content preview: {doc.page_content[:100]}...")
        print(f"  metadata: {doc.metadata}")

    return documents


def main():
    print("Main Function")

    # load documents
    documents=load_documents(docs_path="docs")

if __name__ == "__main__":
    main()

# This what a langchian document would look like.
# documents = [
#    Document(
#        page_content="Google LLC is an American multinational corporation and technology company focusing on online advertising, search engine technology, cloud computing, computer software, quantum computing, e-commerce, consumer electronics, and artificial intelligence (AI).",
#        metadata={'source': 'docs/google.txt'}
#    ),
#    Document(
#        page_content="Microsoft Corporation is an American multinational corporation and technology conglomerate headquartered in Redmond, Washington.",
#        metadata={'source': 'docs/microsoft.txt'}
#    ),
#    Document(
#        page_content="Nvidia Corporation is an American technology company headquartered in Santa Clara, California.",
#        metadata={'source': 'docs/nvidia.txt'}
#    ),
#    Document(
#        page_content="Space Exploration Technologies Corp., commonly referred to as SpaceX, is an American space technology company headquartered at the Starbase development site in Starbase, Texas.",
#        metadata={'source': 'docs/spacex.txt'}
#    ),
#    Document(
#        page_content="Tesla, Inc. is an American multinational automotive and clean energy company headquartered in Austin, Texas.",
#        metadata={'source': 'docs/tesla.txt'}
#    )
# ]
# Tutorials from https://www.youtube.com/watch?v=LK-OyelN9MU&list=PLNIQLFWpQMRUMjxfe8o6g3uzJ6LH_VotY&index=3

 
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

def main():
    print("Main Function")

if __name__ == "__main__":
    main()
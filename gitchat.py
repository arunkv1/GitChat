

#!pip install --upgrade langchain 'deeplake[enterprise]' openai tiktoken
import logging
import openai
import json
from langchain.text_splitter import CharacterTextSplitter
import os
import getpass
import git
from git import Repo
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
import sys
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from os import devnull
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
logging.basicConfig(level=logging.ERROR)
os.environ["OPENAI_API_KEY"] = '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'
openai.api_key = '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'
activeloop_token = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTY5NDY0OTg3NCwiZXhwIjoxNzI2MjcyMjY1fQ.eyJpZCI6ImRldmFscHAifQ.6LcNchbvNWJpfXo9jwJtBfyUruYyXOYoXij7hQ9gjNBGcFyx5b8Jv5m68Qf8P2k6Mvs99RQsWefm6kFQJPh7wQ"
os.environ["ACTIVELOOP_TOKEN"] = activeloop_token
username = "devalpp"

embeddings = OpenAIEmbeddings(disallowed_special=())
db = DeepLake(
        dataset_path=f"hub://{username}/Training",
        read_only=True,
        embedding=embeddings,
    )
def newRepoFunctions(repoLink, targetDir):
    
    # Repo.clone_from(repoLinkn, '/Users/arunkrishnavajjala/Documents/chatcodebase/Training')
    root_dir = targetDir
    docs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            try:
                loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
                docs.extend(loader.load_and_split())
            except Exception as e:
                pass

    len(docs)

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(docs)

      # replace with your username from app.activeloop.ai
    # db = DeepLake(
    #     dataset_path=f"hub://{username}/Training",
    #     embedding=embeddings,
    # )

    #db.add_documents(texts)

    



def filter(x):
    # filter based on source code
    if "com.google" in x["text"].data()["value"]:
        return False

    # filter based on path e.g. extension
    metadata = x["metadata"].data()["value"]
    return "js" in metadata["source"] or "py" in metadata["source"]


def getResponse(questionin):
    sys.stdout = open(devnull, 'w')
    retriever = db.as_retriever()
    retriever.search_kwargs["distance_metric"] = "cos"
    retriever.search_kwargs["fetch_k"] = 100
    retriever.search_kwargs["maximal_marginal_relevance"] = True
    retriever.search_kwargs["k"] = 10
    retriever.search_kwargs['exec_option'] = "python"
    ### turn on below for custom filtering
    retriever.search_kwargs['filter'] = filter


    model = ChatOpenAI(model_name="gpt-3.5-turbo-16k")  # switch to 'gpt-4'
    qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

    questions = [questionin]
    chat_history = []

    for question in questions:
        result = qa({"question": question, "chat_history": chat_history})
        chat_history.append((question, result["answer"]))
        #print(f"-> **Question**: {question} \n")
        #print(f"**Answer**: {result['answer']} \n")
        sys.stdout = sys.__stdout__
        return result['answer']



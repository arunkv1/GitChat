import os
import json
from databaseOp import *
import openai
import json
import logging
import os
import getpass
import git
from git import Repo
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from os import devnull
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import sys
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

from gitchat import * 
logging.basicConfig(level=logging.WARNING)
gitLink = ""
active = True
print("========== Welcome to GitChat ==========")

result = check_repo_in_json()
gitLink = result
if result != False:
    choice = input("Use existing repo? (y/n) ")
    if choice == 'n':
        gitLink = input("Provide the link for the github repo: ")
        add_repo_to_json(gitLink)
    elif choice == 'y':
        show_repos()
        repoNum = input("Enter the Repo Number: ")
        repoNum = int(repoNum) - 1
        gitLink = get_repo(repoNum)
else:
    gitLink = input("Provide the link for the github repo: ")
    add_repo_to_json(gitLink)
    targetDir = '/Users/arunkrishnavajjala/Documents/chatcodebase/' + gitLink.split('/')[-1]
    Repo.clone_from(gitLink, targetDir)





while(active):
    user_input = input(">> Question: ")
    if user_input == 'exit':
        active = False
        break
    if user_input == 'help':
        print("1. Type \'exit\' to exit the chat interface\n2. Ask questions about your codebase\n")
    print(str(">> Answer: ")+getResponse(user_input))












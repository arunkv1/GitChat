import os
import json
from databaseOp import *


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



while(active):
    user_input = input(">> Question: ")
    if user_input == 'exit':
        active = False
        break
    if user_input == 'help':
        print("1. Type \'exit\' to exit the chat interface\n2. Ask questions about your codebase\n")
    print("call function and return")












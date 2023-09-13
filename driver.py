import os

active = True
print("========== Welcome to GitChat ==========")
while(active):
    user_input = input(">> Question: ")
    if user_input == 'exit':
        active = False
        break
    if user_input == 'help':
        print("1. Type \'exit\' to exit the chat interface\n2. Ask questions about your codebase\n")
    print("call function and return")



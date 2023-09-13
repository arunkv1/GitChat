import os
import json
def check_repo_in_json():
    try:
        # Open and load the JSON file
        with open('history.json', 'r') as file:
            data = json.load(file)
        
        # Check if the 'repo' key exists in the JSON data
        if 'repo' in data[0]:
            stored_repo_url = data[0]['repo']
            return stored_repo_url
        else:
            return False
    except FileNotFoundError:
        # Handle the case where the JSON file doesn't exist
        return False

def add_repo_to_json(new_repo_url):

    with open('history.json', 'r') as file:
        data = json.load(file)

    # Create a new dictionary representing the repository
    new_repo_dict = {"repo": new_repo_url}

    # Append the new repository dictionary to the existing array
    data.append(new_repo_dict)
    # Write the updated data back to the JSON file
    with open('history.json', 'w') as file:
        json.dump(data, file, indent=4)

def show_repos():
    data = []
    with open('history.json', 'r') as file:
        data = json.load(file)
    ctr = 1
    for i in data: 
        print(str(ctr) + ". " + i['repo'])
        ctr += 1

def get_repo(ind):
    data = []
    with open('history.json', 'r') as file:
        data = json.load(file)
    return(data[ind]['repo'])







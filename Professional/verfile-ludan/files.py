import os
from utils import dict_to_txt, folder_name_fix, file_name_fix

"""
Retrun a list of all the files and folders of a given root folder
"""
def list_files_and_folders(folder_path):
    try:
        # List all files and directories in the given folder
        items = [f for f in os.listdir(folder_path)]
        return items
    except FileNotFoundError:
        return f"The folder '{folder_path}' does not exist."
    except Exception as e:
        return str(e)
    

def remove_keys_ending_with(d, filters):
    # Use dictionary comprehension to filter out values ending with any of the strings in filters
    return {
        key: value 
        for key, value in d.items() 
        if not any(str(value).endswith(filter_str) for filter_str in filters)
    }

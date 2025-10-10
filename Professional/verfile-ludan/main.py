import os


from files import list_files_and_folders, remove_keys_ending_with
from utils import (
    create_gspread_client,
    dict_to_txt,
    file_name_fix,
    folder_name_fix,
    get_data,
)

# Root folder path
root_folder = "C:\programing\\verfile-ludan\\138294"

# Create a client for interactions with google sheets
client = create_gspread_client('credentials.json')

# Open the file using the sheet id (master document list) 
sheet_id = "1FuGrlW9UqJwLcjBBUgFMmH5vDahGkKFt6rA-OHLGLH0"
sheet = client.open_by_key(sheet_id)

values_list = sheet.sheet1.row_values(1)
print(values_list)

color = "#00ff00"

# Example Usage:
sheet = client.open_by_key(sheet_id).get_worksheet(0)

# Get all the values from the worksheet
all_values = sheet.get_all_values()

# Assuming headers are in the second row, pass header_row=1
key = 'Document number'
item_list = ['Binder', 'Revision']

data = get_data(key, item_list, sheet, header_row=1) 
print("Data has been loaded from Google sheets.")

# Count the number of items (keys) in 'data'
item_count = len(data)


folder_list = list_files_and_folders(root_folder)

all_files = {}
file_index = 0
filters = ['.bak' , '.log' , '.db']

# Create a dict with all the files in the sub fodlers of root folder
for folder in folder_list:
    sub_folder = os.path.join(root_folder, folder)
    sub_folder_file_list = list_files_and_folders(sub_folder)
    
    for file in sub_folder_file_list:
        # Exclude files with extensions in the filters list
        item = [file.lower().endswith(ext) for ext in filters]
       
        if not any(item):
            # Create a key-value pair with file and modified sub_folder name
            all_files[file_index] = f"{file_name_fix(file)}: Binder: {folder_name_fix(folder):}"
            file_index += 1

filtered_files = remove_keys_ending_with(all_files, filters)

# Write both dictinaries to a txt file 
dict_to_txt(filtered_files, 'all files')
dict_to_txt(data, filename='dict')
# Create a new dictionary to store the results
missing_or_mismatched = {}

# Extract the names of keys from filtered_files by considering only the first 14-16 characters
filtered_files_names = {
    key: value[:14].strip() for key, value in filtered_files.items()
}

# Extract the names of keys from filtered_files by considering only the first 14-16 characters
filtered_files_names = {
    key: value[:14].strip() for key, value in filtered_files.items()
}

# Create a new dictionary to store the results
missing = {}

# Extract the names of keys from filtered_files by considering only the first 14-16 characters
filtered_files_names = {
    key: value[:14].strip() for key, value in filtered_files.items()
}

# Create a new dictionary to store the results
missing = {}

# Iterate through each key in 'data'
for key, value in data.items():
    # Get the first 14-16 characters of the key (name)
    data_key_name = key[:14].strip()

    # Check if the name exists in the filtered_files_names
    if data_key_name not in filtered_files_names.values():
        # If the name is not found, add it with the status 'file is missing'
        missing[key] = value
        missing[key]['status'] = 'file is missing'

# Write the missing or mismatched entries to a text file
dict_to_txt(missing, 'missing.txt')

# Print the resulting dictionary with keys and their statuses
print("Keys that are missing or mismatched:")
for key, details in missing.items():
    print(f"{key}: {details}")

dict_to_txt(missing, filename='Test results')

print(len(data) , '\tdocs in google sheets')
print(len(filtered_files) , '\tfiles in fodler')
print(len(missing) , '\treports')

import gspread
from google.oauth2.service_account import Credentials
import re

def dict_to_txt(data_dict, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for key, values in data_dict.items():
            # Convert values (dictionary or list) to a tab-separated string
            if isinstance(values, dict):
                items = '\t'.join(f"{k}: {v}" for k, v in values.items())
            elif isinstance(values, list):
                items = '\t'.join(str(v) for v in values)
            else:
                items = str(values)

            # Write the formatted line to the file
            file.write(f"{key}:\t{items}\n")

    print(f"Dictionary data has been written to '{filename}'.")


def get_data(key, item_list, sheet, header_row=1, color=None):
    # Get all the values from the worksheet
    all_values = sheet.get_all_values()

    # Adjust for zero-indexing in Python
    header_row_index = header_row - 1

    # Extract headers from the specified row
    headers = all_values[header_row_index]

    # Find the index of the 'key' column based on the actual header name 
    key_index = headers.index(key)

    # Find the indices of the columns specified in 'item_list'
    item_indices = [headers.index(col) for col in item_list]

    # Create the dictionary to store the results
    result_dict = {}

    # Iterate over the rows (starting from the row after the header)
    for row in all_values[header_row_index + 1:]:
        # Use the key column to define the dictionary key
        row_key = row[key_index]

        # Collect the data from the specified item columns
        row_data = {headers[i]: row[i] for i in item_indices}

        # Add the key-value pair to the dictionary
        result_dict[row_key] = row_data

    return result_dict


def create_gspread_client(credentials_file):
    """
    Create and return a gspread client using the provided credentials file.
    """
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    cred = Credentials.from_service_account_file(credentials_file, scopes=scopes)
    return gspread.service_account(filename=credentials_file)


"""
Set the name of the file to fit the one in the master binder
"""
def file_name_fix(file_name):
    # Extract the main part of the file name before "_sheet" or "SHT" without a dash
    main_part_match = re.match(r"^([A-Za-z0-9-]+)", file_name)
    if not main_part_match:
        return file_name

    main_part = main_part_match.group(1)
    
    # Check for improperly formatted 'SHT' (e.g., directly attached)
    incorrect_sht_match = re.search(r"([A-Za-z0-9-]+)SHT(\d{1,3})", file_name, re.IGNORECASE)
    if incorrect_sht_match:
        main_part = incorrect_sht_match.group(1)
        number = incorrect_sht_match.group(2)
        formatted_number = number.zfill(3)
        return f"{main_part}-SHT{formatted_number}"
    
    # Look for "sheet" or "Sheet" followed by an underscore and a number
    sht_match = re.search(r"[Ss]heet[_\s]*(\d+)", file_name)
    if sht_match:
        # Get the number after 'sheet' or 'Sheet'
        number = sht_match.group(1)
        # Format the number to be 3 digits
        formatted_number = number.zfill(3)
        return f"{main_part}-SHT{formatted_number}"
    
    # If no conditions are met, return the main part unchanged
    return main_part


"""
Set the name of the folder to fit the one in the master binder
"""

def folder_name_fix(folder_name):
    # Replace any occurrence of "file" (case insensitive) with "MAP"
    folder_name = re.sub(r'file', 'MAP', folder_name, flags=re.IGNORECASE)

    # Use a regex to capture everything before the first dash and trim any trailing spaces
    match = re.match(r"^([^-\n]+)", folder_name)
    if match:
        # Return the matched part before the dash, stripped of any extra spaces
        return match.group(1).strip()

    # If no match is found (no dash present), return the original folder name stripped of spaces
    return folder_name.strip()

import re

def remove_after_fourth_boundary(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        contents = file.read()

    # Define the regex pattern to match the fourth multipart boundary
    pattern = r'^(.*?(?:\r?\n--.*?multipartboundary.*?){2})'

    # Use regex to find the match
    match = re.search(pattern, contents, re.DOTALL | re.IGNORECASE)

    # If a match is found, write the matched string back to the file; otherwise, write the original string
    if match:
        with open(file_path, 'w') as file:
            file.write(match.group(0))
    else:
        with open(file_path, 'w') as file:
            file.write(contents)

# Call the function with the file path
remove_after_fourth_boundary('hive_file_mhtml.mhtml')

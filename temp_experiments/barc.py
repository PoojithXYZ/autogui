import re

def process_file(file_path, pattern):
    with open(file_path, 'r') as file:
        content = file.read().replace('=', '').replace('\n', '')
    matches = re.findall(pattern, content)
    return matches

# Example usage:
file_path = 'hive_file_mhtml.mhtml'
pattern = r'3D\"(.*?)\">'    # Custom regex pattern (word with exactly 5 characters)

content, matches = process_file(file_path, pattern)

print("\nMatches:")
print(matches)


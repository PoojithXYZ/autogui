import re

def process_mhtml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        cleaned_content = re.sub(r'<.*?>', '', content, flags=re.DOTALL).replace('=', '')
        pattern = re.compile(r'(\d+)\s+View\s+launch', flags=re.DOTALL)
        integers = [int(match) for match in pattern.findall(cleaned_content)]
        print(integers)

# Replace 'path_to_your_mhtml_file.mhtml' with the actual path to your MHTML file
process_mhtml_file('hive_file_mhtml.mhtml')


r'''
import re

def remove_tags(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    cleaned_contents = re.sub(r'<.*?>', '', contents, flags=re.DOTALL).replace('=', '')
    print(cleaned_contents)

remove_tags('hive_file_mhtml.mhtml')
'''
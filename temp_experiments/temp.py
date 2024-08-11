import re

def get_links_and_scores(file_path) -> list:
    link_score_pairs = []
    def process_mhtml_file(file_path=file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            cleaned_content = re.sub(r'<.*?>', '', content, flags=re.DOTALL).replace('=', '')
            pattern = re.compile(r'(\d+)\s+View\s+launch', flags=re.DOTALL)
            integers = [int(match) for match in pattern.findall(cleaned_content)]
            return integers
    def extract_submission_urls(file_path=file_path):
        with open(file_path, 'r') as file:
            contents = file.read()
        pattern = r'https:\/\/hive\.smartinterviews\.in\/submission\/[a-zA-Z0-9=\r\n]*'
        urls = re.findall(pattern, contents)
        cleaned_urls = [url.replace('=', '').replace('\n', '') for url in urls]
        return cleaned_urls
    scores = process_mhtml_file()
    links = extract_submission_urls()
    for link, score in zip(links, scores):
        link_score_pairs.append((link, score))
    return link_score_pairs

# Call the function with the file path
print(get_links_and_scores('hive_file_mhtml.mhtml'))


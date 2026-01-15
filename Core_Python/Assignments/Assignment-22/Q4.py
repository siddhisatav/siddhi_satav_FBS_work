import re

def extract_urls(text):
    # Regex pattern to match URLs
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    
    # Find all URLs
    urls = re.findall(url_pattern, text)
    
    return urls

# Example usage
text = """
Check out these websites:
- https://www.google.com
- http://example.org
- www.openai.com
- Not a URL: test.com
"""

urls_found = extract_urls(text)
print("URLs found:", urls_found)

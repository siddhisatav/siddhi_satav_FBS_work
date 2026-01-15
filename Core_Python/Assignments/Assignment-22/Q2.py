import re

def extract_dates(text):
    # Regex patterns for different date formats
    patterns = [
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',                   # MM/DD/YYYY or M/D/YYYY
        r'\b\d{1,2}-\d{1,2}-\d{4}\b',                   # DD-MM-YYYY or D-M-YYYY
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b'  # Month DD, YYYY
    ]
    
    # Combine all patterns into one
    combined_pattern = '|'.join(patterns)
    
    # Find all matches
    dates = re.findall(combined_pattern, text, flags=re.IGNORECASE)
    
    return dates

# Example usage
text = """
We have the following events:
- Meeting on 12/25/2023
- Project deadline on 31-12-2023
- New Year Party on January 1, 2024
- Another event on Feb 2, 2024
"""

dates_found = extract_dates(text)
print("Dates found:", dates_found)

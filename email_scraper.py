import requests
from bs4 import BeautifulSoup
import re



# url = "https://httpbin.org/html"
url = "https://crawfishswimschool.com"


# Fetch page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all text
all_text = soup.get_text()

# Regex pattern for emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all emails
emails = re.findall(email_pattern, all_text)

# Remove duplicates
emails = list(set(emails))

# Print results
if emails:
    print("Emails found on the page:")
    for email in emails:
        print(email)
else:
    print("No emails found.")
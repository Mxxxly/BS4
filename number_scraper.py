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

phone_pattern = r"\+?\d[\d\s\-()]{8,15}\d"
numbers = re.findall(phone_pattern, all_text)

numbers = list(set(numbers))  # remove duplicates

for number in numbers:
    print(number)
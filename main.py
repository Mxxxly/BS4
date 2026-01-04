import requests 
from bs4 import BeautifulSoup
import re


# url = "https://example.com"
# response= requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# heading = soup.find('h1')
# print("Heading:", heading.text)


# url ="https://httpbin.org/html"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Search for text directly
# matches = soup.find_all(string="Example Domain")  # exact text match
# for match in matches:
#     print(match)



# USING SOUP.PRETTIFY()

# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())




# searching for a particular word

# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# matches = soup.find_all(string=re.compile("Example"))
# for match in matches:
#     print(match)


# searching by text inside tag 

# url = "https://httpbin.org/html"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# paragraphs = soup.find_all("p")
# for p in paragraphs:
#     if "Herman" in p.text:  # word from the page
#         print("Found:", p.text)


# This one is searching for all p tags in the page 

# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# paragraphs = soup.find_all("p")
# for p in paragraphs:
#     print("Found Melly request:", p.text)


# USING REGEX TO FIND EMAILS | IMPORTANT

# Step 1: Fetch the page
# url = "https://www.w3schools.com/html/html_examples.asp"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Step 2: Extract all text
# all_text = soup.get_text()

# # Step 3: Use regex to find emails
# email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# emails = re.findall(email_pattern, all_text)

# print("Found emails:")
# for email in emails:
#     print(email)



# This is removing duplicates emails 

# url = "https://www.w3schools.com/html/html_examples.asp"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Step 2: Extract all text
# all_text = soup.get_text()

# # Step 3: Use regex to find emails
# email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# emails = re.findall(email_pattern, all_text)

# # Remove duplicates by converting to set
# emails = list(set(emails))

# print("Found emails:")
# for email in emails:
#     print(email)



# This is to save the result to a txt file 


url = "https://www.w3schools.com/html/html_examples.asp"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract all text
all_text = soup.get_text()

# Step 3: Use regex to find emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, all_text)

# Remove duplicates
emails = list(set(emails))

# Print emails
print("Found emails:")
for email in emails:
    print(email)

# Step 4: Save emails to a text file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write("new email:"+ email + "\n")  # each email on a new line
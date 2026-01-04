import re 
import requests 
import csv
from bs4 import BeautifulSoup


file = open("books.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)

# Write header row
writer.writerow(["Title", "Price"])


page = 1

while True:
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    if not books:
        break

    for book in books:
        # Safe extraction with .get() and checks
        title_tag = book.find("h3").find("a")
        price_tag = book.find("p", class_="price_color")

        if title_tag and price_tag:
            title = title_tag.get("title", "No title").strip()
            price = price_tag.text.strip().replace("Â", "").replace("£", "")
            # Convert price to float (optional)
            try:
                price = float(price)
            except:
                price = 0.0

            # Write to CSV
            writer.writerow([title, price])

    page += 1

file.close()  # important to save file
print("Scraping complete! Data saved to books.csv")

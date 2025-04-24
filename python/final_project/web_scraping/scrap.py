from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the Python website
url = "https://www.python.org/"

r = requests.get(url)
data = r.text
print(f"HTTP  status code : {r.status_code}")

soup = BeautifulSoup(data, 'html.parser')

# Print prettified HTML to the console
# print(soup.prettify())

with open("file.html", mode="w", encoding="utf-8") as f:
    f.write(soup.prettify())


print(f"Title : {soup.title.text}")

# heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
heading_tags = ["h1", "h2"]

for heading in heading_tags:
    print(f"ALL {heading} HEADINGS")
    for text in soup.find_all(heading):
        print(text.text.strip())
    print()    
        

scraped_data = {
    'url': url,
    'status_code': r.status_code,
    'title': soup.title.string if soup.title else 'No title found',
}        

print(scraped_data)



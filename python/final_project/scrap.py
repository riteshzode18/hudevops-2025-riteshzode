# from bs4 import BeautifulSoup
# import requests


# r = requests.get("https://www.python.org/")

# data = r.text
# # with open("file.html", mode="w") as f:
# #     f.write(data)

# soup = BeautifulSoup(data, 'html.parser')


# print(soup.prettify())



# with open("file.html", mode="w") as f:
#     f.write(soup.prettify())

from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the Python website
r = requests.get("https://www.python.org/")
data = r.text

# Parse the HTML content
soup = BeautifulSoup(data, 'html.parser')

# Print the prettified HTML to the console
# print(soup.prettify())

# Save the prettified HTML to a file
# with open("file.html", mode="w", encoding="utf-8") as f:
#     f.write(soup.())prettify

print(soup.find(id="title"))
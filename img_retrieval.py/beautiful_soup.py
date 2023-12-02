# Get the HTML content from the response
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find an element by tag or class
# Example: Find an image tag
image_tag = soup.find('img')

# If you know the class or id of the element you can specify it
# Example: Find an element with a specific class
# specific_element = soup.find('div', class_='specific-class')

# Print the found element
print(image_tag)
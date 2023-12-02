import requests
from openai import OpenAI

client = OpenAI(api_key='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')


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)


image_url = 'https://udottraffic.utah.gov/1_devices/aux17227.jpeg'

# Send a GET request to the image URL
# response = requests.get(image_url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Open a file in binary write mode
#     with open('downloaded_image.jpeg', 'wb') as file:
#         # Write the content of the response to the file
#         file.write(response.content)
#     print("Image downloaded successfully.")
# else:
#     print(f"Failed to download the image. Status code: {response.status_code}")



# OpenAI API URL (replace with the specific endpoint you're using)



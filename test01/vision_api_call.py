# Import necessary modules
from pprint import pprint
from openai import OpenAI
import json
import os

var_value = os.environ.get('openaikey')
# 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

# Create an OpenAI client using your API key
client = OpenAI(api_key='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')

# Make a request to the OpenAI API using the chat model
# The request includes a series of messages, including text and image URLs
# The text message provides instructions for the model
# The image URLs are the images to be analyzed

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": """
        these are pictures from traffic cameras that are along a road
        that leads up to a ski resort. 
        Please analyze the traffic and weather conditions and respond as if writing a tweet. 
        the tweet doesnt have to be 140 characters, but needs to be concise.
        the format of the tweet should be as follows:
        Name of Camera: Traffic conditions; Road Conditions

        when you get to url: https://udottraffic.utah.gov/1_devices/aux17226.jpeg, describe it as a parking lot, not a road. describe how full it is.
        /SR-210 @ ''Alta/MP 12.16. This camera does not focus on a road, but a parking lot. 
        Describe how full the parking lot instead of describing the traffic conditions.

        Please remember, https://udottraffic.utah.gov/1_devices/aux16270.jpeg is NOT a parking lot. describe it as a road.
        """},
        # The following are image URLs for the model to analyze
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux14604.jpeg"}},
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16265.jpeg"}},
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16267.jpeg"}},
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16269.jpeg"}},
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16270.jpeg"}},
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17227.jpeg"}},
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17228.jpeg"}},
        {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17226.jpeg"}},
      ],
    }
  ],
  max_tokens=400,  # Limit the response to 500 tokens
)

# Save the response to a JSON file
with open('response.json', 'w') as f:
    json.dump(response.model_dump(), f)
'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'
from pprint import pprint
from openai import OpenAI
import json


client = OpenAI(api_key='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')

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": """
        these are pictures from traffic cams that are along the road
          that leads up to the ski resort. I want you to analyze traffic conditions.

        please create a gradient scale of hex colors in between green and red that represent the varying 
        levels of traffic and bad or good conditions. green is no traffic, red is a lot of traffic.

        Please list out each camera with a brief description of the traffic and road conditions.
         have the first word of your reponse for each camera be the hex code for the level of traffic. 
         I will use these hex codes to create a colored icon in my visual representation of your response in an app.

        """},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux14604.jpeg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux16265.jpeg",
          },
        },
                {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux16267.jpeg",
          },
        },
                {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux16269.jpeg",
          },
        },
                {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux16270.jpeg",
          },
        },
                {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux17227.jpeg",
          },
        },
                {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux17228.jpeg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://udottraffic.utah.gov/1_devices/aux17226.jpeg",
          },
        },
      ],
    }
  ],
  max_tokens=500,
)

with open('response.json', 'w') as f:
    json.dump(response.model_dump(), f)

pprint(response.choices[0].text)

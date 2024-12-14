from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Write a short description of a forest in spring in no more than three sentences"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "In spring, the forest comes alive with a vibrant tapestry of fresh green leaves and blooms, as the sun filters gently through the budding canopy. The air buzzes with renewed energy, filled with the songs of birds returning from their winter migrations and the soft rustle of wildlife awakening. Wildflowers carpet the forest floor in brilliant hues, transforming it into a lively mosaic that celebrates new beginnings."
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=0
)
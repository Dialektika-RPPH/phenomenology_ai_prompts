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
          "text": "In spring, the forest bursts into life with a vibrant canopy of fresh green leaves and colorful wildflowers carpeting the ground. The air is filled with birdsong and the gentle rustle of new foliage stirred by a soft breeze. Sunlight streams through the trees, casting playful patterns on the forest floor as nature awakens from its winter slumber."
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
  presence_penalty=1
)
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
          "text": "Write a short description of a forest in spring in no more than three sentences."
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "In spring, the forest bursts to life with a tapestry of vibrant greens as fresh leaves unfurl on every branch. The air is filled with the symphony of birdsong and the gentle rustle of new foliage. Splashes of wildflowers pepper the forest floor, providing colorful patches amid the lush sea of greenery."
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
  frequency_penalty=0,
  presence_penalty=0
)
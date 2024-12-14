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
          "text": "In spring, the forest awakens with a vibrant tapestry of emerging greens as leaves unfurl from budding trees. A symphony of birdsong fills the air, while wildflowers carpet the forest floor in splashes of color. The fresh scent of earth mixes with dappled sunlight, creating an atmosphere of renewal and vitality."
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
  presence_penalty=1
)
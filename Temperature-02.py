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
          "text": "In one sentence, what is the Moon?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "The Moon is Earth's only natural satellite, orbiting the planet and influencing tides, with a surface marked by craters and basins."
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  temperature=0.2,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
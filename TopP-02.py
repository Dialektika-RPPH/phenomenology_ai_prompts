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
          "text": "In no more than four sentences, describe a scene from a futuristic city."
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "In the heart of the futuristic city, towering skyscrapers with shimmering glass facades stretch into the sky, their surfaces alive with dynamic holographic advertisements. Autonomous drones zip through the air, delivering packages and providing real-time surveillance, while sleek, driverless vehicles glide silently along the multi-layered roadways. The streets are bustling with people, many of whom are accompanied by AI-driven robotic companions, engaging in lively conversations or assisting with daily tasks. Above, a network of elevated green spaces and solar panels provide a stark contrast to the urban sprawl, offering a glimpse of nature amidst the technological marvel."
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=0.2,
  frequency_penalty=0,
  presence_penalty=0
)
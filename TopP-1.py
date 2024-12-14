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
          "text": "Neon lights bathe the city in vibrant hues as autonomous vehicles glide silently along elevated roadways. Towering skyscrapers, adorned with vertical gardens, pierce the skyline, their glass surfaces reflecting the bustling metropolis below. People, accompanied by humanoid robots, stroll through holographic art displays in sprawling, solar-paneled plazas. Above, drones zip through the air, efficiently managing deliveries and surveillance while ensuring the city's seamless operation."
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
from openai import OpenAI

# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key="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",)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)

#that is paid client id
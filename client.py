from openai import OpenAI
#client = OpenAI()
# defaults to getting the key using os.environ.get("OΡΕΝΑΙ_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
api_key= "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",
)

completion =client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[

    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud"}, 
    {"role": "user", "content": "what is coding"}
  ]
)

print (completion.choices[0].message.content)
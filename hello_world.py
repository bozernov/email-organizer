import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello world"}
    ]
)

print("Response from OpenAI:")
print(response['choices'][0]['message']['content'])

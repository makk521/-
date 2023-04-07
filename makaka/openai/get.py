'''
https://github.com/openai/openai-python
'''
import openai
openai.api_key = "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"  # supply your API key however you choose

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "为什么天空是蓝色的!"}])
print(completion.choices[0].message.content)
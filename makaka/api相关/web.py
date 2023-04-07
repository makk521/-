from flask import Flask
import openai
openai.api_key = "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"  # supply your API key however you choose


app = Flask(__name__)

@app.route('/')
def hello_world():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "为什么天空是蓝色的!"}])
    return completion.choices[0].message.content

app.run(host='0.0.0.0')
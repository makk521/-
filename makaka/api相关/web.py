'''
简单的flask框架写的api,放在服务器上运行。
'''

from flask import Flask, request
import openai
openai.api_key = "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"  

app = Flask(__name__)

def ask_gpt(prompt):
    '''
    chatgpt的api调用。
    参数:问题
    返回:问题结果
    '''
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

@app.route('/', methods=['POST'])
def hello_world():
    # question = request.form['question']
    # print(question)
    # return ask_gpt(question)
    print(request.form)
    return 'hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
'''
简单的flask框架写的api,放在服务器上运行。
接受json格式的post请求,返回json格式
$ screen -S mysession
$ python app.py
'''

from flask import Flask, request
import openai
import json
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
    print(request.json['question'])    # dict
    question = request.json['question']
    answer = ask_gpt(question)
    data = json.dumps({'answer': answer}, sort_keys=True, indent=4, separators=(',', ': '))
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')



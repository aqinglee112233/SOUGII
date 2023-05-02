from flask import Flask, jsonify, request
import requests 
import os
import openai
app = Flask(__name__)
openai.api_key = os.environ.get("YOUR_API_KEY")
@app.route('/gpt', methods=['POST'])
def gpt():
    prompt = request.json.get('prompt')
    model = request.json.get('model', 'text-davinci-002')
    max_tokens = int(request.json.get('max_tokens', 16))
    temperature = float(request.json.get('temperature', 0.7))
    data = {
        'prompt': prompt,
        'engine': model,
        'max_tokens': max_tokens,
        'temperature': temperature
    }
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    #print(type(response))
    return response

if __name__ == '__main__':
      port = int(os.environ.get("PORT"))
      app.run(host="0.0.0.0", port=port)

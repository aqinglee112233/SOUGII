from flask import Flask, jsonify, request
import requests
import os
app = Flask(__name__)

@app.route('/gpt', methods=['POST'])
def call_openai_api():
    openai.api_key = os.environ.get("YOUR_API_KEY")
    prompt = request.form.get('prompt')
    model = request.form.get('model', 'text-davinci-002')
    max_tokens = int(request.form.get('maxTokens', 16))
    temperature = float(request.form.get('temperature', 0.7))

    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearerport  " + openai.api_key

    data = {
        "prompt": prompt,
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return jsonify({
            'success': True,
            'response': result['choices'][0]['text']
        })
    else:
        return jsonify({
            'success': False,
            'error': f'{response.status_code}: {response.reason}'
        })

if __name__ == '__main__':
      port = int(os.environ.get("PORT"))
      app.run(host="0.0.0.0", port=port)
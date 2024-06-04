from flask import Flask, request, render_template
import openai
import markdown2
import os
app = Flask(__name__)

# Ваш ключ OpenAI API
openai.api_key = 'sk-proj-SxFImaW9xwu94oCHyPpDT3BlbkFJrvWGHpxNZwruH79dy5Gk'

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        response_text = response.choices[0].text.strip()
        response_text = markdown2.markdown(response_text)
    return render_template('templates/index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(debug=True)

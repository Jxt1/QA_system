from flask import Flask, request, render_template, Markup
from QA_system import QA_entry


app = Flask(__name__, template_folder='./web')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def get_answer():
    question = request.form['question']
    answer = QA_entry(question)

    # answer = Markup(answer)
    print(answer)
    # answer = Markup(answer).striptags()
    return render_template('home.html', question=question, answer=answer)


if __name__ == '__main__':
    app.run()

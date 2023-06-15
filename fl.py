from flask import Flask, render_template, request
import ask

app = Flask(__name__)
responses = []


@app.route('/')
def index():
    return render_template("main.html")


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    text = request.args.get('user_input')

    if text is not None:
        res = ask.ask_help(text)
        responses.append(res)

    return render_template('chat.html', responses=responses)


app.debug = True
app.run(host='0.0.0.0', port=8080)

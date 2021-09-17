from flask import Flask, render_template, request
from ozekilibsrest import Configuration, Message, MessageApi

app = Flask(__name__)

configuration = Configuration(
    username="http_user",
    password="qwe123",
    api_url="http://127.0.0.1:9509/api"
)

api = MessageApi(configuration)

messages_to_send = []
logs = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit'] == 'SEND' and len(messages_to_send) > 0:
            log = api.send(messages_to_send)
            logs.append(log)
            messages_to_send.clear()
        elif request.form['submit'] == 'ADD':
            message = Message(
                to_address=request.form['to_address'],
                text=request.form['text']
            )
            messages_to_send.append(message)
    return render_template('SendMultipleSms.html', logs=logs, messages=messages_to_send)


if __name__ == '__main__':
    app.run()

# This is what happens when the repository gets updated.

from flask import Flask, render_template, request
from ozekilibsrest import Configuration, Message, MessageApi
app = Flask(__name__)

configuration = Configuration(
    username="http_user",
    password="qwe123",
    api_url="http://127.0.0.1:9509/api"
)

api = MessageApi(configuration)

logs = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = Message(
            to_address=request.form['to_address'],
            text=request.form['text']
        )
        log = api.send(message)
        logs.append(log)
    return render_template('SendSms.html', logs=logs)


if __name__ == '__main__':
    app.run()

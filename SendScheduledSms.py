from flask import Flask, render_template, request
from ozekilibsrest import Configuration, Message, MessageApi
from datetime import datetime
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
            text=request.form['text'],
            time_to_send=datetime.strptime(request.form.get('time_to_send'), "%Y-%m-%d %H:%M:%S")
        )
        log = api.send(message)
        logs.append(log)
    return render_template('SendScheduledSms.html', logs=logs)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request
from ozekilibsrest import Configuration, MessageApi
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
        messages = api.download_incoming()
        message_count_string  = messages.__str__()
        logs.append(message_count_string)
        for message in messages.messages:
            message_string = message.__str__()
            logs.append(message_string)
    return render_template('ReceiveSms.html', logs=logs)


if __name__ == '__main__':
    app.run()

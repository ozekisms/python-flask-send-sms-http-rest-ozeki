from flask import Flask, render_template, request
from ozekilibsrest import Configuration, Message, MessageApi, Folder
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
        message = Message(message_id=request.form['message_id'])

        if request.form['folder'] == 'inbox':
            log = api.delete(Folder.Inbox, message)
        elif request.form['folder'] == 'outbox':
            log = api.delete(Folder.Outbox, message)
        elif request.form['folder'] == 'sent':
            log = api.delete(Folder.Sent, message)
        elif request.form['folder'] == 'notsent':
            log = api.delete(Folder.NotSent, message)
        else:
            log = api.delete(Folder.Deleted, message)
        logs.append(log)
    return render_template('DeleteSms.html', logs=logs)


if __name__ == '__main__':
    app.run()

from flask import Flask, request
import json
from mySMTP import myMail

app = Flask(__name__)

response_data = {"success": None, "message": None}


@app.route('/test_smtp', methods=['GET', 'POST'])
def test_smtp():
    if request.method == 'POST':
        mail_data = json.loads(request.get_data())
        try:
            my = myMail(mail_data["host"], mail_data["port"], mail_data["username"], mail_data["password"],
                        mail_data["to_addr"], mail_data["subject"], mail_data["content"], mail_data["attach"])
            my.run()
            response_data['success'] = 'true'
            response_data['message'] = 'OK'
        except Exception as e:
            response_data['success'] = 'flase'
            response_data['message'] = str(e)
        return json.dumps(response_data)
    else:
        return "<h1>只接受POST请求！</h1>"

@app.route('/test_imap')
def test_imsp():
    return '进行中'

if __name__ == '__main__':
    app.run()

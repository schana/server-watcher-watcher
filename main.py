import flask
import requests

app = flask.Flask(__name__)
url = 'https://54.36.180.201/api/server-mod-reporting'
should_forward = True


@app.route('/api/server-mod-reporting', methods=['POST'])
def mock_response():
    print('Received request')
    if should_forward:
        forward(flask.request.data)
    return 'false'


def forward(data):
    try:
        print('Attempting to forward request')
        print(data)
        r = requests.post(url, data=data)
        if r.status_code == 200:
            print('Success')
        else:
            print('Failure', r.status_code)
    except requests.RequestException as e:
        print('Failure with exception', e)


if __name__ == '__main__':
    app.run(ssl_context='adhoc', port=443)

import flask

app = flask.Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if (flask.request.method == 'POST'):
        some_json = flask.request.get_json()
        return flask.jsonify({"you sent": some_json}), 201
    else:
        return flask.jsonify({"about": "Hello World!"})


@app.route('/multi/<int:num>/<int:num2>', methods=['GET'])
def get_multi(num, num2):
    return flask.jsonify({'result': num * num2})


@app.route('/add/<int:num>/<int:num2>', methods=['GET'])
def get_add(num, num2):
    return flask.jsonify({'result': num + num2})


@app.route('/sub/<int:num>/<int:num2>', methods=['GET'])
def get_sub(num, num2):
    return flask.jsonify({'result': num - num2})


@app.route('/div/<int:num>/<int:num2>', methods=['GET'])
def get_div(num, num2):
    return flask.jsonify({'result': num / num2})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=800)

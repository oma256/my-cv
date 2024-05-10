from flask import Flask, render_template
from reader import get_data


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data = get_data()

    return render_template('index.html', **data)


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)

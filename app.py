from flask import Flask, render_template
from reader import get_contact_info


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    fullname = 'Iman Turdukeev'
    get_contact_info()
    return render_template('index.html', fullname=fullname)


if __name__ == '__main__':
    app.run(debug=True)

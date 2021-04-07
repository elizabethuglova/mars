from flask import Flask, render_template

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return render_template('pei.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pynderbot', methods=['POST'])
def pynderbot():
	global userId, accessToken
	userId = request.form['userId']
	accessToken = request.form['accessToken']

	return render_template("pynderbot.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
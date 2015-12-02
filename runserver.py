from flask import Flask, request, jsonify, render_template
import pynder
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
	
	print(userId)
	print(accessToken)

	return render_template("pynderbot.html")

@app.route('/like')
def like():
	print(userId)
	print(accessToken)
	session = pynder.Session(str(userId), str(accessToken))
	users = session.nearby_users()
	liked = []
	for user in users[:5]:
		user.like()
		liked.append(user.name)

	return render_template("like.html", liked=liked)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
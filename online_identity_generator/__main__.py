from flask import Flask, render_template, jsonify, request
from online_identity_generator import User
from flask_login import login_manager, current_user, login_user
import os

# GLOBALS
USERS = []

app = Flask(__name__)
login_manager = login_manager.LoginManager(app)

@login_manager.user_loader
def load_user(id):
    for user in USERS:
        if user.get_id() == id:
            return user

app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generator')
def generator():
    return render_template('generator.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ajax', methods=["POST"])
def ajax():
    # its not super clean code, but it works
    action = request.form['action']

    if action == 'keywords':
        # retrieve keywords
        keywords = request.form['keywords'].split(',')

        try:
            keywords.remove('')
        except ValueError:
            pass

        if len(keywords) == 0:
            return jsonify({"error": "Please provide at least one keyword"})

        # check keywords for special characters (if so return error)
        for keyw in keywords:
            for char in keyw:
                char_code = ord(char)
                if not ((char_code > 47 and char_code < 58) or (char_code > 63 and char_code < 91) or (char_code > 96 and char_code < 123)):
                    return jsonify({"error": "Please don't use special characters"})

        # Place holder, this is where the code would contact the module for the acctual generating
        id = 0
        while True:
            for user in USERS:
                if user.id == id:
                    id += 1
                    continue
            break
        user = User(keywords, id)
        USERS.append(user)
        onlinenames = user.name.generate()

        login_user(user)

        return jsonify({
            "handler": "generator",
            "onlinenames": onlinenames
        })

    if action == 'online_name':
        online_name = request.form['online_name']

        current_user.name.sel(online_name)

        # check if the user has submitted stupid shit by creating his/her own formData
        for char in online_name:
            char_code = ord(char)
            if not ((char_code > 47 and char_code < 58) or (char_code > 63 and char_code < 91) or (char_code > 96 and char_code < 123) or char_code == 95 or char_code == 32):
                return jsonify({"error": f"Get out of the fucking code u bitch {char_code}"})

        # Place holder, this is where the code would contact the module for the acctual generating
        usernames = current_user.username.generate()

        return jsonify({
            "handler": "generator",
            "usernames": usernames,
            "msg": f"Usernames: {usernames}"
        })

    if action == 'username':
        username = request.form['username']

        current_user.username.sel(username)

        # check if the user has submitted stupid shit by creating his/her own formData
        for char in username:
            char_code = ord(char)
            if not ((char_code > 47 and char_code < 58) or (char_code > 63 and char_code < 91) or (char_code > 96 and char_code < 123) or char_code == 95):
                return jsonify({"error": f"Get out of the fucking code u bitch {char_code}"})

        email = current_user.email.generate()

        return jsonify({
            "handler": "generator",
            "email": email
        })

    return jsonify({
        "error": "Unknown ajax call"
    })

@app.route('/output', methods=["POST"])
def output():
    """ Shows beautifull output for the user """

    current_user.passwords.generate()

    return render_template('output.html', current_user=current_user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)

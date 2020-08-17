from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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

        print(keywords, len(keywords))
        if len(keywords) == 0:
            return jsonify({"error": "Please provide at least one keyword"})

        # check keywords for special characters (if so return error)
        for keyw in keywords:
            for char in keyw:
                char_code = ord(char)
                if not ((char_code > 47 and char_code < 58) or (char_code > 63 and char_code < 91) or (char_code > 96 and char_code < 123)):
                    return jsonify({"error": "Please don't use special characters"})
        
        # Place holder, this is where the code would contact the module for the acctual generating
        onlinenames = ["White spaghetti", "Cumcumber sucker"]

        return jsonify({
            "handler": "generator",
            "onlinenames": onlinenames
        })
    
    if action == 'online_name':
        online_name = request.form['online_name']

        # check if the user has submitted stupid shit by creating his/her own formData
        for char in online_name:
            char_code = ord(char)
            if not ((char_code > 47 and char_code < 58) or (char_code > 63 and char_code < 91) or (char_code > 96 and char_code < 123) or char_code == 95 or char_code == 32):
                return jsonify({"error": f"Get out of the fucking code u bitch {char_code}"})
        
        # Place holder, this is where the code would contact the module for the acctual generating
        usernames = ['WhiteSpaghetti', 'white_spaghet']

        return jsonify({
            "handler": "generator",
            "usernames": usernames,
            "msg": f"Usernames: {usernames}"
        })
    
    if action == 'username':
        username = request.form['username']

         # check if the user has submitted stupid shit by creating his/her own formData
        for char in username:
            char_code = ord(char)
            if not ((char_code > 47 and char_code < 58) or (char_code > 63 and char_code < 91) or (char_code > 96 and char_code < 123) or char_code == 95):
                return jsonify({"error": f"Get out of the fucking code u bitch {char_code}"})

        return jsonify({
            "handler": "generator",
            "email": f"{username}@gmail.com"
        })


    return jsonify({
        "error": "Unknown ajax call"
    })

@app.route('/output', methods=["POST"])
def output():
    """ Shows beautifull output for the user """

    online_name = request.form['name']
    username = request.form['username']
    email = request.form['email']


    # Place holder, this is where the code would contact the module for the acctual generating
    passwords = ["12321", "f*($"]

    return render_template('output.html', online_name=online_name, username=username, email=email, passwords=passwords)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
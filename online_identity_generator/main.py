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
    action = request.form['action']

    if action == 'keywoards':
        return jsonify({
            "msg": "No module interaction yet... "
        })

    return jsonify({
        "error": "Unknown ajax call"
    })
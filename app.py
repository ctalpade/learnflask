from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

courses = [
    {
        'name': 'Python',
        'level': 'Intermediate'
    },
    {
        'name': 'Java',
        'level': 'Advanced'
    },
    {
        'name': 'Flask',
        'level': 'Beginner'
    },
]


@app.route("/api/listtopics")
def list_topics():
    return jsonify(courses)


@app.route("/")
def hello_world():
    return render_template('hello.html',
                           params={
                               'name': 'Chaitanya',
                               'age': 47,
                               'courses': courses
                           })


print(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

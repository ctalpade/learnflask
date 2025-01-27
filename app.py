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

@app.route('/listfiles')
def showResults(requestid):
    files = []
    cwd = None
    try:
        cwd = os.getcwd()
        files = os.listdir(cwd)
    except Exception as e:
        pass
    return 'The current dir is '+str(cwd)+' files in this folder '+str(files)



@app.route("/test1")
def test1():
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()

    return 'this is from test1'


print(__name__)
sq1 = [n * n for n in range(10) if n % 2 == 0]
sq2 = {n: n * n for n in range(10) if n % 2 == 0}
print(sq1)
print(sq2)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

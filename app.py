from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
    {
        'id': 1,
        'title': 'Random Color Generator App',
        'description': 'Generates random color, also provides hex-codes for all colors, made using React-Native.',
        'timeStamp': 'Jan 2024'
    },
    {
        'id': 2,
        'title': 'Haptic Fedback Dice Rolling App',
        'description': 'Double dice rolling feature with a haptic feedback, made using React-Native.',
        'timeStamp': 'Jan 2024'
    },
    {
        'id': 3,
        'title': 'Music Streaming App',
        'description': 'Offline music streaming Application, made using React-Native.',
        'timeStamp': 'Jan 2024'
    },
    {
        'id': 4,
        'title': 'Password Generator App',
        'description': 'Generates Password, strength : Medium, length : Dependable, made using React-Native.',
        'timeStamp': 'Jan 2024'
    },
    {
        'id': 4,
        'title': 'Youtube Comment Search using Python and API',
        'description': 'Search specific word or phrase in any youtube video comments, using Youtube API, done in Python.',
        'timeStamp': 'Feb 2024'
    },
    {
        'id': 4,
        'title': 'Count Word In Youtube Video Transcript',
        'description': 'Count specific word or phrase in any youtube video transcript, if it had any, done in Python.',
        'timeStamp': 'Jan 2024'
    },
    
]

@app.route('/')
def hello_world():
    return render_template('home.html', projects=PROJECTS)

@app.route("/projects")
def list_projects():
    return jsonify(PROJECTS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
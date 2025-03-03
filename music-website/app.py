from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/music/<filename>')
def get_music(filename):
    return send_from_directory('static/music', filename)

if __name__ == '__main__':
    app.run(debug=True)

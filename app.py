from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assets/img/<path:filename>')
def send_images(filename):
    return send_from_directory('assets/img', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

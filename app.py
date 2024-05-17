from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Submitted: Name - {name}, Email - {email}"
    return 'Invalid request'

if __name__ == '__main__':
    app.run(debug=True)

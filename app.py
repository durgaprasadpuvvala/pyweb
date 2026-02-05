# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dynamic_message = "Hello, welcome to the My world!"
    return render_template('index.html', message=dynamic_message)

if __name__ == '__main__':
    # Run the app in debug mode for interactive development
    app.run(debug=True)

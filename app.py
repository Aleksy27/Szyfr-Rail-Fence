from Flask import Flask
from flask import render_template 

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run("localhost", port=3000, debug=True)
from flask import Flask, request, render_template
from rail_fence import encrypt, decrypt 

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

@app.post("/enc")
def enc():
    key = int(request.form["key"])
    text = request.form["text"]
    rail_fence_text = encrypt(text, key)
    return rail_fence_text

@app.post("/dec")
def dec():
    key = int(request.form["key"])
    rail_fence_text = request.form["rail_fence_text"]
    text = decrypt(rail_fence_text, key)
    return text

if __name__ == "__main__":
    app.run("localhost", port=3000, debug=True)

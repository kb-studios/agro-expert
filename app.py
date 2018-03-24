from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def input_data():
    return render_template("input.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
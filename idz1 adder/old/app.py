from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def main_page():
    return render_template("main.html")

if(__name__ == "__main__"):
    app.run(debug=True)
else:
    print("it's not a module!")




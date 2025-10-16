# https://flask.palletsprojects.com/en/stable/

from flask import Flask
from flask import render_template 



app = Flask(__name__)

@app.route("/saludxs")
def página_principal():
    return render_template("index.html")

# Arranque directo del servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
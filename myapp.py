from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text

myapp = Flask(__name__)


@myapp.route("/")
def root_html():
    return render_template("home.html")


if __name__ == "__main__":
    myapp.run(debug=True)

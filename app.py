from flask import Flask, render_template, request

from shashbot import answer_query, setup

DEBUG_MODE = False
app = Flask("ShashBot", template_folder="./templates")
setup()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/chat")
def chat():
    query = request.args.get("query")
    answer = answer_query(query)
    return render_template("search_result.html", query=query, answer=answer)


if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)

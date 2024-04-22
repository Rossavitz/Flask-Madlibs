from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"


@app.route("/")
def get_info():
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route("/story")
def madlib():

    text = story.generate(request.args)

    return render_template("/story.html", text=text)

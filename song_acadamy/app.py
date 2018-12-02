import json
import os

from flask import Flask, render_template, request

from song_acadamy import storage

root_dir = os.path.dirname(os.path.abspath(__file__))
resource_dir = os.path.join(root_dir, 'resources')
tmpl_dir = os.path.join(root_dir, 'templates')
static_dir = os.path.join(root_dir, 'static')
app = Flask("song_academy", template_folder=tmpl_dir, static_folder=static_dir)


@app.route("/")
def get_page():
    return render_template("index.html", title="Välj ditt bord:")


@app.route("/result")
def get_result():
    return render_template("result.html")


@app.route("/questions/<table_id>", methods=["POST"])
def post_question_result(table_id):
    storage.save_response(table_id, request.form)
    return render_template("response.html")


@app.route("/questions/<table_id>", methods=["GET"])
def get_questioner(table_id):
    questions = get_questions()
    title = get_song_name(table_id)
    context = {
        "song_title": title,
        "questions": questions
    }
    return render_template("questioner.html", **context)


def get_questions():
    return [{"id": k, "question": v} for k, v in load_json("questions.json").items()]


def get_song_name(table_id):
    return load_json("songs.json")[table_id]


def load_json(file_name):
    with open(os.path.join(resource_dir, file_name)) as f:
        questions = json.load(f)
    return questions


if __name__ == '__main__':
    app.run(port=8080)

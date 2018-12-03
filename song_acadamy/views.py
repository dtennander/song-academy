from flask import render_template, request

from song_acadamy import app, questions, storage


@app.route("/")
def get_page():
    return render_template("index.html", title="Välj ditt bord:")


@app.route("/song/<song_id>")
def get_song(song_id):
    song_title = questions.get_song_name(song_id)
    lyrics = questions.get_song_lyrics(song_id)
    return render_template("song.html", song_title=song_title, lyrics=lyrics, song_id=song_id)


@app.route("/result")
def get_result():
    return render_template("result.html")


@app.route("/questions/<table_id>", methods=["POST"])
def post_question_result(table_id):
    storage.save_response(int(table_id), request.form)
    return render_template("response.html")


@app.route("/questions/<table_id>", methods=["GET"])
def get_questioner(table_id):
    context = {
        "song_title": questions.get_song_name(int(table_id)),
        "questions": questions.get_questions()
    }
    return render_template("questioner.html", **context)

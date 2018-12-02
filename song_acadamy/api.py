import json

from song_acadamy import app, questions, storage


@app.route("/api/questions")
def get_questions():
    q = {item["id"]: item["question"] for item in questions.get_questions()}
    return json.dumps(q)


@app.route("/api/questions/<question_id>")
def get_question_by_id(question_id):
    return json.dumps(next(item for item in questions.get_questions() if item["id"] == int(question_id)))


@app.route("/api/songs")
def get_songs():
    songs = {i: questions.get_song_name(i) for i in range(1, 10)}
    return json.dumps(songs)


@app.route("/api/songs/<table_id>")
def get_songs_by_id(table_id):
    id = int(table_id)
    return json.dumps({"id": id, "song": questions.get_song_name(id)})


@app.route("/api/results")
def get_results():
    responses = [storage.get_table_responses(i) for i in range(1, 10)]
    return json.dumps(responses)

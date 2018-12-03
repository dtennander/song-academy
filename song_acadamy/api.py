from flask import url_for, jsonify

from song_acadamy import app, questions, storage


@app.route("/api")
def get_api_root():
    return jsonify({
        "description": 'The API provided for song_academy. To reach an individual item go to endpoint/id',
        "endpoints": {
            "questions": url_for("get_questions", _external=True),
            "songs": url_for("get_songs", _external=True),
            "results": url_for("get_results", _external=True)
        },
    })


@app.route("/api/questions")
def get_questions():
    q = {item["id"]: item["question"] for item in questions.get_questions()}
    return jsonify(q)


@app.route("/api/questions/<question_id>")
def get_question_by_id(question_id):
    return jsonify(next(item for item in questions.get_questions() if item["id"] == int(question_id)))


@app.route("/api/songs")
def get_songs():
    songs = {i: {
        "name": questions.get_song_name(i),
        "lyrics": questions.get_song_lyrics(i)} for i in range(1, 10)}
    return jsonify(songs)


@app.route("/api/songs/<table_id>")
def get_songs_by_id(table_id):
    int_id = int(table_id)
    return jsonify({
        "id": int_id,
        "song": {
            "name": questions.get_song_name(int_id),
            "lyrics": questions.get_song_lyrics(int_id)
        }})


@app.route("/api/results")
def get_results():
    responses = [storage.get_table_responses(i) for i in range(1, 10)]
    return jsonify(responses)


@app.route("/api/results/<table_id>")
def get_result_by_id(table_id):
    return jsonify(storage.get_table_responses(int(table_id)))

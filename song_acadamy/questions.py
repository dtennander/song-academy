import json
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
resource_dir = os.path.join(root_dir, 'resources')


def get_questions() -> [dict]:
    return [{"id": int(k), "question": v} for k, v in load_json("questions.json").items()]


def get_song_name(song_id: int) -> str:
    return load_json("songs.json")[str(song_id)]["name"]


def get_song_lyrics(song_id: int) -> str:
    return load_json("songs.json")[str(song_id)]["lyrics"]


def load_json(file_name):
    with open(os.path.join(resource_dir, file_name)) as f:
        questions = json.load(f)
    return questions

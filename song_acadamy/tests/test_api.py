from unittest import TestCase

from mock import patch

from song_acadamy import api, app


class TestApi(TestCase):

    def setUp(self):
        app.config["SERVER_NAME"] = "test.se"

    @patch("song_acadamy.questions.get_questions")
    def test_get_questions(self, get_questions_mock):
        # Given
        the_question = "?"
        get_questions_mock.return_value = [{"id": "1", "question": the_question}]
        # When
        with app.app_context():
            result = api.get_questions()
        # Then
        self.assertEqual({"1": "?"}, result.get_json())

    @patch("song_acadamy.questions.get_questions")
    def test_get_question_by_id(self, get_questions_mock):
        # Given
        the_question = "?"
        get_questions_mock.return_value = [{"id": 1, "question": the_question}]
        # When
        with app.app_context():
            result = api.get_question_by_id("1")
        # Then
        self.assertEqual({"id": 1, "question": "?"}, result.get_json())

    @patch("song_acadamy.questions.get_song_name")
    def test_get_songs(self, get_song_name_mock):
        # Given
        get_song_name_mock.return_value = "hej"
        # When
        with app.app_context():
            result = api.get_songs()
        # Then
        self.assertEqual(
            {"1": "hej",
             "2": "hej",
             "3": "hej",
             "4": "hej",
             "5": "hej",
             "6": "hej",
             "7": "hej",
             "8": "hej",
             "9": "hej"}, result.get_json())

    @patch("song_acadamy.questions.get_song_name")
    def test_get_song_by_id(self, get_song_name_mock):
        # Given
        get_song_name_mock.return_value = "hej"
        # When
        with app.app_context():
            result = api.get_songs_by_id(1)
        # Then
        self.assertEqual({"id": 1, "song": "hej"}, result.get_json())

    @patch("song_acadamy.storage.get_table_responses")
    def test_get_results(self, get_table_responses_mock):
        # Given
        get_table_responses_mock.return_value = {"id": 1, "responses": []}
        # When
        with app.app_context():
            result = api.get_results()
        # Then
        self.assertEqual([
            {"id": 1, "responses": []},
            {"id": 1, "responses": []},
            {"id": 1, "responses": []},
            {"id": 1, "responses": []},
            {"id": 1, "responses": []},
            {"id": 1, "responses": []},
            {"id": 1, "responses": []},
            {"id": 1, "responses": []},
            {"id": 1, "responses": []}], result.get_json())

    @patch("song_acadamy.storage.get_table_responses")
    def test_get_results_by_id(self, get_table_responses_mock):
        # Given
        get_table_responses_mock.return_value = {"id": 1, "responses": []}
        # When
        with app.app_context():
            result = api.get_result_by_id(1)
        # Then
        self.assertEqual({"id": 1, "responses": []}, result.get_json())

    def test_api_root(self):
        # When
        with app.app_context():
            result = api.get_api_root()
        # Then
        endpoints = result.get_json()["endpoints"]
        with app.test_client() as client:
            for url in endpoints.values():
                self.assertIsNotNone(client.get(url).get_json())
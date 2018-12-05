from unittest import TestCase

from mock import patch

from song_acadamy import views, app


class TestViews(TestCase):

    def setUp(self):
        app.config["SERVER_NAME"] = "test.se"

    def verify_rendering(self, endpoint):
        with app.app_context():
            page = endpoint()
        self.assertIsNotNone(page)
        return page

    def test_get_page(self):
        self.verify_rendering(views.get_page)

    def test_get_result(self):
        with app.test_request_context():
            self.verify_rendering(views.get_result)

    @patch("song_acadamy.storage.save_response")
    def test_post_question_result(self, save_mock):
        table_id = 1
        with app.test_client() as client:
            result = client.post("/questions/{}".format(table_id), data="a=1&b=2")
        self.assertIsNotNone(result.data)
        save_mock.assert_called_once()

    @patch("song_acadamy.questions.get_song_name")
    @patch("song_acadamy.questions.get_questions")
    def test_get_questioner(self, song_mock, questions_mock):
        song_mock.return_value = "Hej"
        questions_mock.return_value = [{"id": 1, "question": "vad?"}]
        self.verify_rendering(lambda: views.get_questioner(1))

    @patch("song_acadamy.questions.get_song_name")
    @patch("song_acadamy.questions.get_song_lyrics")
    def test_get_song(self, song_mock, lyrics_mock):
        song_mock.return_value = "Hej"
        lyrics_mock.return_value = "song lyrics"
        page = self.verify_rendering(lambda: views.get_song(1))
        self.assertTrue("song lyrics" in page)
        self.assertTrue("Hej" in page)

from unittest import TestCase

from song_acadamy import questions


class TestQuestions(TestCase):

    def test_get_questions(self):
        # When
        qs = questions.get_questions()
        q = qs[0]
        # Then
        self.assertEqual(len(qs), 3)
        self.assertEqual(int, type(q["id"]))
        self.assertEqual(str, type(q["question"]))

    def test_get_song_name(self):
        # Given
        song_id = 1
        # When
        song = questions.get_song_name(song_id)
        # Then
        self.assertIsNotNone(song)

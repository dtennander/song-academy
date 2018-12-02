from unittest import TestCase

import boto3
from moto import mock_dynamodb2

from song_acadamy import storage

table_name = "song_academy_responses"


@mock_dynamodb2
class TestStorage(TestCase):
    conn = boto3.resource("dynamodb")

    def setUp(self) -> None:
        self.conn.create_table(
            TableName=table_name,
            KeySchema=[{
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }],
            AttributeDefinitions=[{
                'AttributeName': 'id',
                'AttributeType': 'N'
            }],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            })

    def tearDown(self) -> None:
        self.conn.Table(table_name).delete()

    def test_get_response(self):
        # Given
        stored_item = {"id": 1, "lol": "boll"}
        self.conn.Table(table_name).put_item(Item=stored_item)
        # When
        result = storage.get_table_responses(1)
        # Then
        self.assertEqual(result, stored_item)

    def test_store_response(self):
        # Given
        form = {"1": "1", "2": "2"}
        # When
        storage.save_response(1, form)
        results = storage.get_table_responses(1)
        # Then
        self.assertIn(form, results["responses"])

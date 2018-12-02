import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('song_academy_responses')


def save_response(table_id, form):
    id = int(table_id)
    db_response = table.get_item(Key={"id": id})
    if "Item" not in db_response:
        responses = {"id": id, "responses": []}
    else:
        responses = db_response["Item"]

    responses["responses"].append(form)
    table.put_item(Item=responses)

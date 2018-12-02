import boto3

table = boto3.resource('dynamodb').Table('song_academy_responses')


def save_response(table_id, form):
    responses = get_table_responses(table_id)
    responses["responses"].append(form)
    table.put_item(Item=responses)


def get_table_responses(table_id: int):
    db_response = table.get_item(Key={"id": table_id})
    if "Item" not in db_response:
        responses = {"id": table_id, "responses": []}
    else:
        responses = db_response["Item"]
        responses["id"] = int(responses["id"])
    return responses

# The Song Academy
This project was created to allow a group of friends to do a small show/survey during a dinner party.

Feel free to look around and get inspired. This was quite a fast hack so do not use this as a template!

## Requirements
To run and develop this application you need to install its dependencies. This is done by running:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Running tests
To run all tests just run:
```bash
nosetests
```
## Running locally
To run the server locally you need access to a DynamoDb table with the name `song_academy_responses`.
When this is done just run:
```bash
FLASK_APP=song_acadamy flask run
```

## Deployment
This service is deployed to two stages: `dev` and `production`.
To deploy just type:
```bash
zappa deploy <stage>
```
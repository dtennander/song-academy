app: python_deps result_client

result_client: result-client song_acadamy
	cd result-client; make
	cp -rf result-client/build song_acadamy/static/result_client

python_deps: requirements.txt requirements-dev.txt
	. venv/bin/activate
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

deploy: app
	zappa update dev

deploy-production: app
	zappa update production

test: python_deps
	. venv/bin/activate
	nosetests

clean:
	rm -rf song_acadamy/static/result_client
	cd result-client; make clean
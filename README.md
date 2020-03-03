# School Library Tutorial

## initial installation
	git clone <repo-name>
	cd <reponame>
	python3 -m venv venv
	source venv/bin/activate
	pip install Flask

## Switch to the branch
	git reset --hard
	git branch -a
	git checkout <branch-name>

## To reset Database
	rm data.db
	sqlite3 data.db < school-library-schema.sql


## To run the app
	source venv/bin/activate   
	export FLASK_ENV=development
	flask run

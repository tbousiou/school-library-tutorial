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

## Commit changes on local
    git add .
    git commit -m "Put a comment here"

## Switch to master from remote repo
    git fetch
    git checkout origin/master

## To reset Database
	rm data.db
	sqlite3 data.db < school-library-schema.sql


## To run the app on Linux
    source venv/bin/activate
	export FLASK_ENV=development
	flask run

# school-library-tutorial

# initial installation
git clone <repo-name>
cd <reponame>
python3 -m venv venv
source venv/bin/activate


# Switch to the branch
git reset --hard
git branch -a
git checkout <branch-name>

# To run the app
export FLASK_ENV=development
flask run
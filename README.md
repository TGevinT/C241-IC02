# T-Det-D

# Guide for Start Project

## 1. (once) Clone github project to local <br>
Please run the following command in the expected path
 
`git clone https://github.com/TGevinT/T-Det-D.git`

Note: Already install Git in local computer

## 2. Change branch to dev or create new branch <br>
`git checkout dev`

or

`git checkout -b <new_branch>`

Note: Branch main for final result and staging for deployment (don't change the code manualy)

## 3. (once) Create virtual environment <br>
For Windows:
    python -m venv .venv

For macOS/Linux
    python3 -m venv .venv

## 4. Activate the virtual environment<br>
For Windows

`.venv\Scripts\activate`

For macOS/Linux

`source .venv/bin/activate`

If want to deactivate

`deactivate`

## 5. Install requirements <br>
`p`

# Guide for Daily Project

## Check branch <br>
`git branch`

if not in expected branch

`git checkout <expected_branch>`

## Pull Project from staging <br>
`git pull origin staging`

## Save Project to github <br>
### git add
`git add .`

### git commit
`git commit -m '<message for what change in program>'`

best practice commit can see in [here](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)

### git push
`git push`

now the project save in expected branch in github




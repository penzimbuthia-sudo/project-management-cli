# Project Management CLI Tool

## Description

The Project Management CLI Tool is a Python command-line application that helps administrators manage users, projects, and tasks.

The application allows users to:

* Create and manage users
* Create and manage projects
* Create and manage tasks
* Assign projects to users
* Mark tasks as completed
* Store data using JSON files
* Access features through command-line commands

The project demonstrates Object-Oriented Programming (OOP), file handling, command-line interfaces, testing, and package management using Pipenv.

## Features

### User Management

* Add a user
* View all users

### Project Management

* Add a project
* View all projects
* Search projects assigned to a specific user

### Task Management

* Add a task
* View all tasks
* Mark tasks as completed

### Data Persistence

* Save users, projects, and tasks in JSON files
* Load existing data when the application runs

### Object-Oriented Programming

* Inheritance using Person and User classes
* Encapsulation using properties and setters
* Relationships between Users, Projects, and Tasks

## Technologies Used

* Python 3.10+
* argparse
* json
* rich
* pytest
* pipenv

## Project Structure

project-management-cli/

├── main.py

├── Pipfile

├── Pipfile.lock

├── README.md

├── data/

│   ├── users.json

│   ├── projects.json

│   └── tasks.json

├── models/

│   ├── person.py

│   ├── user.py

│   ├── project.py

│   └── task.py

├── utils/

│   └── file_handler.py

└── tests/

├── test_user.py

├── test_project.py

└── test_task.py


## Installation

### Clone the Repository

git clone <your-github-repository-link>

### Navigate to the Project Folder

cd project-management-cli

### Install Pipenv

pip install pipenv

### Install Dependencies

pipenv install


## Running the Application

Run commands using:

pipenv run python main.py


## Available Commands

### Add User
pipenv run python main.py add-user --name "Alex" --email "alex@gmail.com"

### List Users
pipenv run python main.py list-users

### Add Project
pipenv run python main.py add-project --user "Alex" --title "CLI Tool" --description "Python Project" --due-date "2026-07-01"

### List Projects
pipenv run python main.py list-projects

### View Projects for a Specific User
pipenv run python main.py user-projects --user "Alex"

### Add Task
pipenv run python main.py add-task --project "CLI Tool" --title "Create User Class"

### List Tasks
pipenv run python main.py list-tasks
### Complete Task
pipenv run python main.py complete-task --title "Create User Class"


## Running Tests
Run all tests using:
pipenv run pytest


## Data Storage

Application data is stored in JSON files:

* users.json
* projects.json
* tasks.json

These files are located inside the `data` folder.


## Known Limitations

* Data validation is basic.
* Duplicate users, projects, or tasks can be added.
* IDs reset when the application restarts.
* Authentication and user roles are not implemented.


## Future Improvements

* Add update and delete functionality.
* Prevent duplicate records.
* Improve validation.
* Add user authentication.
* Add project contributors.
* Add task deadlines and priorities.



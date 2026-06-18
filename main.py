import argparse
from rich import print

from utils.file_handler import load_data, save_data

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

def add_user(args):

    users = load_data(USERS_FILE)

    user = {
        "name": args.name,
        "email": args.email
    }

    users.append(user)

    save_data(USERS_FILE, users)

    print("[green]User added successfully[/green]")


def list_users(args):

    users = load_data(USERS_FILE)

    if not users:
        print("[red]No users found[/red]")
        return

    for user in users:
        print(user)

def update_user(args):

    users = load_data(USERS_FILE)

    found = False

    for user in users:

        if user["email"] == args.email:

            user["name"] = args.new_name

            found = True
            break

    if not found:
        print("[red]User not found[/red]")
        return

    save_data(USERS_FILE, users)

    print("[green]User updated successfully[/green]")

def delete_user(args):

    users = load_data(USERS_FILE)

    new_users = []

    found = False

    for user in users:

        if user["email"] == args.email:
            found = True
        else:
            new_users.append(user)

    if not found:
        print("[red]User not found[/red]")
        return

    save_data(USERS_FILE, new_users)

    print("[green]User deleted successfully[/green]")

def add_project(args):

    projects = load_data(PROJECTS_FILE)

    project = {
        "user": args.user,
        "title": args.title,
        "description": args.description,
        "due_date": args.due_date
    }

    projects.append(project)

    save_data(PROJECTS_FILE, projects)

    print("[green]Project added successfully[/green]")

def list_projects(args):

    projects = load_data(PROJECTS_FILE)

    if not projects:
        print("[red]No projects found[/red]")
        return

    for project in projects:
        print(project) 

def update_project(args):

    projects = load_data(PROJECTS_FILE)

    found = False

    for project in projects:

        if project["title"] == args.title:

            project["description"] = args.description
            project["due_date"] = args.due_date

            found = True
            break

    if not found:
        print("[red]Project not found[/red]")
        return

    save_data(PROJECTS_FILE, projects)

    print("[green]Project updated successfully[/green]")

def delete_project(args):

    projects = load_data(PROJECTS_FILE)

    new_projects = []

    found = False

    for project in projects:

        if project["title"] == args.title:
            found = True
        else:
            new_projects.append(project)

    if not found:
        print("[red]Project not found[/red]")
        return

    save_data(PROJECTS_FILE, new_projects)

    print("[green]Project deleted successfully[/green]")

def add_task(args):

    tasks = load_data(TASKS_FILE)

    task = {
        "project": args.project,
        "title": args.title,
        "status": "Pending"
    }

    tasks.append(task)

    save_data(TASKS_FILE, tasks)

    print("[green]Task added successfully[/green]")           

def complete_task(args):

    tasks = load_data(TASKS_FILE)

    for task in tasks:
        if task["title"] == args.title:
            task["status"] = "Completed"

    save_data(TASKS_FILE, tasks)

    print("[green]Task completed[/green]")

def list_tasks(args):
    tasks = load_data(TASKS_FILE)

    if not tasks:
        print("[red]No tasks found[/red]")
        return
    
    for task in tasks:
        print(task)

def user_projects(args):
    projects = load_data(PROJECTS_FILE)

    found = False

    for project in projects:
        if project["user"] == args.user:
            print(project)
            found = True

    if not found:
        print("[red]No projects found[/red]")


parser = argparse.ArgumentParser(description="Project Management CLI")

subparsers = parser.add_subparsers()

add_user_parser = subparsers.add_parser("add-user")
add_user_parser.add_argument("--name", required=True)
add_user_parser.add_argument("--email", required=True)
add_user_parser.set_defaults(func=add_user)

list_user_parser = subparsers.add_parser("list-users")
list_user_parser.set_defaults(func=list_users)

update_user_parser = subparsers.add_parser("update-user")

update_user_parser.add_argument("--email", required=True)
update_user_parser.add_argument("--new-name", required=True)

update_user_parser.set_defaults(func=update_user)

delete_user_parser = subparsers.add_parser("delete-user")
delete_user_parser.add_argument("--email", required=True)

delete_user_parser.set_defaults(func=delete_user)

project_parser = subparsers.add_parser("add-project")

project_parser.add_argument("--user", required=True)
project_parser.add_argument("--title", required=True)
project_parser.add_argument("--description", required=True)
project_parser.add_argument("--due-date", required=True)

project_parser.set_defaults(func=add_project)

list_projects_parser = subparsers.add_parser("list-projects")

list_projects_parser.set_defaults(func=list_projects)

update_project_parser = subparsers.add_parser("update-project")

update_project_parser.add_argument("--title", required=True)
update_project_parser.add_argument("--description", required=True)
update_project_parser.add_argument("--due-date", required=True)

update_project_parser.set_defaults(func=update_project)
delete_project_parser = subparsers.add_parser("delete-project")
delete_project_parser.add_argument("--title", required=True)

delete_project_parser.set_defaults(func=delete_project)

task_parser = subparsers.add_parser("add-task")

task_parser.add_argument("--project", required=True)
task_parser.add_argument("--title", required=True)

task_parser.set_defaults(func=add_task)

complete_parser = subparsers.add_parser( "complete-task")
complete_parser.add_argument("--title", required=True)

complete_parser.set_defaults(func=complete_task)

list_tasks_parser = subparsers.add_parser("list-tasks")
list_tasks_parser.set_defaults(func=list_tasks)

user_projects_parser = subparsers.add_parser("user-projects")

user_projects_parser.add_argument("--user",required=True)

user_projects_parser.set_defaults(
    func=user_projects
)
args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
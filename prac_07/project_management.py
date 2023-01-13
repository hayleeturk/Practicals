"""
CP1404 Practical 7
Project management program
Estimated time: 2 hours
Actual time:
"""

from prac_07.project import Project
import datetime
from operator import attrgetter

FILENAME = "projects.txt"
MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate " \
       "project\n(Q)uit"


def main():
    """Load and save a data file and use a list of Project objects."""
    print(MENU)
    menu_choice = input(">>>").upper()
    projects = []
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Enter file name: ")
            projects = load_projects(filename, projects)
        elif menu_choice == "S":
            save_projects(filename, projects)
        elif menu_choice == "D":
            projects.sort(key=attrgetter("date"))
            completed_projects = determine_status(projects)
            display_projects(projects, completed_projects)
        elif menu_choice == "F":
            filtered_projects = filter_by_date(projects)
            display_filtered_projects(filtered_projects)
        elif menu_choice == "A":
            get_new_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        print(MENU)
        menu_choice = input(">>>").upper()
    print("Finished")


def load_projects(filename, projects):
    """Load projects from specified file."""
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            date = parts[1]
            priority = int(parts[2])
            cost = float(parts[3])
            percentage = parts[4]
            my_project = Project(name, date, priority, cost, percentage)
            projects.append(my_project)
        return projects


def determine_status(projects):
    """Create new list of completed projects."""
    completed_projects = []
    for project in projects:
        if project.is_complete():
            projects.remove(project)
            completed_projects.append(project)
    return completed_projects


def display_projects(projects, completed_projects):
    """Display data for completed and incomplete projects, sorted by priority."""
    print("Incomplete projects:")
    for project in sorted(projects):
        print(project)
    print("Completed projects:")
    for completed_project in sorted(completed_projects):
        print(completed_project)


def get_new_project(projects):
    """Take user input to add new project."""
    name = input("Name: ").title()
    date = get_date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    percentage = int(input("Percentage complete: "))
    new_project = Project(name, date, priority, cost, percentage)
    projects.append(new_project)


def get_date():
    """Get start date from user and return formatted date. """
    date_choice = input("Set start date as today? (Y/N): ").upper()
    if date_choice == "Y":
        date = datetime.datetime.now()
    else:
        date = check_valid_date("Start date (d/m/yyyy): ")
    return date


def update_project(projects):
    """Update a chosen projects percentage and priority"""
    for i, project in enumerate(projects, 1):
        print(i, project)
    project_choice = get_valid_project(projects)
    print(projects[project_choice])
    new_percentage = int(input("New percentage: "))
    while new_percentage == "":
        new_percentage = int(input("New percentage: "))
    projects[project_choice].percentage = new_percentage
    new_priority = int(input("New priority: "))
    while new_priority == "":
        new_priority = int(input("New priority: "))
    projects[project_choice].priority = new_priority


def save_projects(filename, projects):
    """Save projects to chosen file."""
    filename = input("Enter file name: ")
    with open(filename, "w", encoding="utf-8") as out_file:
        print(f"Name\tStart\tDate\tPriority\tCost\tEstimate\tCompletion\tPercentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.percentage}",
                  file=out_file)


def filter_by_date(projects):
    """Display only projects that start after a specified date, sorted by date."""
    filtered_date = check_valid_date("Show projects that start after date (dd/mm/yyyy): ")
    filtered_date = str_to_date(filtered_date)
    for project in projects:
        project.date = str_to_date(project.date)  # converts date strings to objects
    filtered_projects = [project for project in projects if project.date >= filtered_date]
    return filtered_projects


def str_to_date(date):
    """Convert date string to date object."""
    date_object = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    return date_object


def display_filtered_projects(filtered_projects):
    """Display sorted, filtered projects."""
    for project in sorted(filtered_projects, key=attrgetter("date")):
        project.date = date_to_str(project.date)
        print(project)


def date_to_str(date):
    """Convert date object to string."""
    return date.strftime("%d/%m/%Y")


def check_valid_date(prompt):
    """Check date is valid."""
    is_valid = False
    while not is_valid:
        date = input(prompt)
        try:
            str_to_date(date)
            is_valid = True
        except ValueError:
            print("Invalid date")
    return date


def get_valid_project(projects):
    """Get valid project number."""
    project_choice = int(input("Project choice: ")) - 1
    while project_choice < 1 or project_choice > len(projects) - 1:
        print("Invalid project choice")
        project_choice = int(input("Project choice: ")) - 1
    return project_choice


main()

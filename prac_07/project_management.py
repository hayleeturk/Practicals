"""
CP1404 Practical 7
Project management program
Estimated time: 2 hours
Actual time: 6 Hours
"""

import datetime
from operator import attrgetter
from prac_07.project import Project

FILENAME = "projects.txt"
MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate " \
       "project\n(Q)uit"


def main():
    """Load and save a data file and use a list of Project objects."""
    print(MENU)
    projects = []
    load_projects(projects, FILENAME)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            get_valid_filename(projects)
        elif menu_choice == "S":
            save_projects(projects)
        elif menu_choice == "D":
            projects.sort(key=attrgetter("priority"))
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
    print("Thank you for using custom-built project management software.")


def load_projects(projects, filename):
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
    priority = get_valid_number("Priority: ", 1, 10)
    cost = get_valid_price()
    percentage = get_valid_number("Percent complete: ", 0, 100)
    new_project = Project(name, date, priority, cost, percentage)
    projects.append(new_project)


def get_date():
    """Get start date from user and return formatted date. """
    date_choice = input("Set start date as today? (Y/N): ").upper()
    if date_choice == "Y":
        date = date_to_str(datetime.datetime.now())
    else:
        get_valid_date("Start date (d/m/yyyy): ")
        date = date_to_str(datetime.datetime.now())
    return date


def update_project(projects):
    """Update a chosen projects percentage and priority"""
    for i, project in enumerate(projects, 1):
        print(i, project)
    project_choice = get_valid_project(projects)
    print(projects[project_choice])
    new_percentage = get_valid_number("Percent complete: ", 0, 100)
    projects[project_choice].percentage = new_percentage
    new_priority = get_valid_number("Priority: ", 1, 10)
    projects[project_choice].priority = new_priority


def save_projects(projects):
    """Save projects to chosen file."""
    filename = get_valid_string()
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart\tDate\tPriority\tCost\tEstimate\tCompletion\tPercentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.percentage}",
                  file=out_file)


def filter_by_date(projects):
    """Display only projects that start after a specified date, sorted by date."""
    filtered_date = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
    filtered_date = str_to_date(filtered_date)
    for project in projects:
        project.date = str_to_date(project.date)  # converts date strings to objects
    filtered_projects = [project for project in projects if project.date >= filtered_date]
    for project in projects:
        project.date = date_to_str(project.date)
    return filtered_projects


def str_to_date(date):
    """Convert date string to date object."""
    date_object = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    return date_object


def display_filtered_projects(filtered_projects):
    """Display sorted, filtered projects."""
    for project in sorted(filtered_projects, key=attrgetter("date")):
        print(project)


def date_to_str(date):
    """Convert date object to string."""
    return date.strftime("%d/%m/%Y")


def get_valid_date(prompt):
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


def get_valid_number(prompt, minimum, maximum):
    """Get a valid integer from user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            while number < minimum or number > maximum:
                print("Invalid number")
                number = int(input(prompt))
            is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


def get_valid_filename(projects):
    """Check filename is valid."""
    is_valid_filename = False
    while not is_valid_filename:
        filename = get_valid_string()
        try:
            load_projects(projects, filename)
            is_valid_filename = True
        except FileNotFoundError:
            print("File does not exist")


def get_valid_string():
    """Get a valid string from user."""
    filename = input("Enter filename: ")
    while filename == "":
        print("Filename cannot be blank")
        filename = input("Enter filename: ")
    return filename


def get_valid_price():
    """Check price is a valid number."""
    is_valid_price = False
    while not is_valid_price:
        try:
            cost = float(input("Cost estimate: "))
            while cost < 0:
                print("Cost must be >= $0")
                cost = float(input("Cost estimate: "))
            is_valid_price = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return cost


if __name__ == "__main__":
    main()

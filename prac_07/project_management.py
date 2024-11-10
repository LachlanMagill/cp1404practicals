from project import Project
from datetime import datetime

Menu = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""

def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            header = file.readline().strip()
            for line_number, line in enumerate(file, 2):
                line = line.strip()
                parts = line.split('\t')
                if len(parts) == 5:
                    try:
                        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                        projects.append(project)
                    except ValueError as e:
                        print(f"Error in line {line_number}: {e} (Skipping line)")
                else:
                    print(f"Warning: Line {line_number} does not have exactly 5 fields. Skipping line.")
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return projects

def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete, key=lambda x: x.priority):
        print(f"  {project}")

def filter_projects_by_date(projects, date_str):
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    filtered_projects = [project for project in projects if project.start_date > date_obj]
    return sorted(filtered_projects, key=lambda x: x.start_date)

def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")

    return Project(name, start_date, priority, cost_estimate, completion_percentage)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]

    new_percentage = input(f"New Percentage ({project.completion_percentage}): ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)

    new_priority = input(f"New Priority ({project.priority}): ")
    if new_priority:
        project.priority = int(new_priority)

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def main():
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    while True:
        print(Menu)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_projects_by_date(projects, date_str)
            for project in filtered_projects:
                print(project)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {filename}? (y/n): ").lower()
            if save_choice == 'y':
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

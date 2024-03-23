import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%"

    def update(self, percent_complete='', priority=''):
        if percent_complete:
            self.percent_complete = int(percent_complete)
        if priority:
            self.priority = int(priority)

    def is_after_date(self, date):
        project_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        filter_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        return project_date > filter_date

def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            next(file)  # Skip header line
            for line in file:
                name, start_date, priority, cost_estimate, percent_complete = line.strip().split('\t')
                project = Project(name, start_date, int(priority), float(cost_estimate), int(percent_complete))
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {file_name}")
    except FileNotFoundError:
        print(f"File {file_name} not found. Starting with an empty project list.")
    return projects

def main():
    file_name = 'projects.txt'
    projects = load_projects(file_name)

if __name__ == "__main__":
    main()



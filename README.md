# Employee Task Manager

Employee Task Manager is a command-line application built using Python and SQLAlchemy, designed to manage employees, projects, and tasks within an organization.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Manage Employees:**
  - Add new employees with their names and departments.
  - View existing employees.
  - Update employee details.
  - Delete employees from the database.

- **Manage Projects:**
  - Add new projects with names and descriptions.
  - View existing projects.
  - Update project details.
  - Delete projects from the database.

- **Manage Tasks:**
  - Add new tasks with descriptions and statuses.
  - View existing tasks.
  - Update task statuses.
  - Delete tasks from the database.


## Prerequisites

- Python 3.x
- SQLAlchemy
- SQLite (comes bundled with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/employee-task-manager.git
   cd task-manager
Install dependencies:

bash

pip install -r requirements.txt
Initialize the SQLite database:

bash

python -m lib.models.models

## Usage
Run the application:

bash

python cli.py
Select options from the menu to manage employees, projects, tasks, or exit the program.

## Contributing
Contributions are welcome! Here's how you can contribute:

## License
This project is licensed under the MIT License - see the LICENSE file for details.
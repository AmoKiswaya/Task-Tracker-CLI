# Task Tracker CLI  Project

Task Tracker CLI is a command line interface built in python for managing tasks via the terminal. Arguments such as "add" for adding tasks, "list" for listing tasks optionally filtered by status, "update" for updating an exisiting task based and "delete" for deleting a task by ID. 


### Development Installation

For development, install in editable mode:
```bash
git clone https://github.com/AmoKiswaya/Task-Tracker-CLI.git
cd Task-Tracker-CLI
pip install -e . 
```

## Usage
```bash
# Add a new task
task-tracker add "Visit bookstore"
# Output
✅ Task successfully added!
ID: 8
Description: Visit bookstore
Status: todo

# Update a task
task-tracker update 1 -d "Visit Paris" -s done
# Output
✅ Task 1 updated successfully
Updated task: ID: 1
Description: Visit Paris
Status: done
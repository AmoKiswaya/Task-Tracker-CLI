import argparse
from taskmanager import TaskManager 

def main():
    parser = argparse.ArgumentParser(
        description="Task Tracker CLI"
    )

    subparsers = parser.add_subparsers(dest="command") 

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description") 

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status",
        choices=["todo", "in-progress", "done"],
        help="Filter tasks by status"
    )

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("--description", help="New description")
    update_parser.add_argument(
        "--status",
        choices=["todo", "in-progress", "done"]
    )

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        task = manager.add_task(args.description)
        print(f"Added task: {task}") 

    elif args.command == "list":
        tasks = manager.list_tasks(args.status)
        if not tasks:
            print("No tasks found.") 
        for task in tasks:
            print(task)

    elif args.command == "update":
        task = manager.update_task(
            args.id,
            description=args.description,
            status=args.status
        )
        print(f"Updated task: {task}") 

    elif args.command == "delete":
        manager.delete_task(args.id)
        print(f"Deleted task {args.id}")

    else:
        parser.print_help() 
        

if __name__ == "__main__":
    main() 
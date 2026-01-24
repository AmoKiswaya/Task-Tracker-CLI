import argparse
import json
from task_tracker.taskmanager import TaskManager 


def print_json(data):
    print(json.dumps(data, indent=4))

def main():
    parser = argparse.ArgumentParser(
        prog="TaskTrackerCLI",
        description="Task Tracker CLI for managing tasks through the terminal"
    )

    subparsers = parser.add_subparsers(dest="command") 

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description") 
    add_parser.add_argument(
        "--json",
        action="store_true",
        help="Output tasks as JSON"
    )

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status",
        choices=["todo", "in-progress", "done"],
        help="Filter tasks by status"
    )
    list_parser.add_argument(
        "--json",
        action="store_true",
        help="Output tasks as JSON"
    )

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("-d", "--description", type=str, help="New description")
    update_parser.add_argument(
        "-s",
        "--status",
        type=str,
        choices=["todo", "in-progress", "done"]
    )
    update_parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="Output task as JSON"
    )

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        task = manager.add_task(args.description)
        print("\n✅ Task successfully added!") 

        if args.json:
            print_json(task.to_dict())
        else:
            print(task)

    elif args.command == "list":
        tasks = manager.list_tasks(args.status)

        if args.json:
            print_json([task.to_dict() for task in tasks])
        else:    
            if not tasks:
                print("No tasks found.") 
            for task in tasks:
                print(task)

    elif args.command == "update":
        try:
            task = manager.update_task(
                args.id,
                description=args.description,
                status=args.status
            )
            print(f"✅ Task {task.id} updated successfully")
        except ValueError as e:
            print(e)
            return
        
        if args.json:
            print_json(task.to_dict())
        else:   
            print(f"Updated task: {task}") 

    elif args.command == "delete":
        manager.delete_task(args.id)
        print(f"Deleted task {args.id}")

    else:
        parser.print_help() 
        

if __name__ == "__main__":
    main() 
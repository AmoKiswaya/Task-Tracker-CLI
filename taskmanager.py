from task_tracker import Task
import json

class TaskManager:

    class Options:
        all = "all"
        done = "done"
        todo = "todo"
        in_progress = "in-progress"

    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self._tasks = {} 

    def add_task(self):
        pass

    def delete_task(self, index):
        pass

    def list_tasks(self):
        pass 
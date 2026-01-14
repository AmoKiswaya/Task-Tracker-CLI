from datetime import datetime
import json


class Task:
    task_id = 0


    def __init__(self, description, *args, **kwargs):
        self.id 
        self.description = description
        self.status
        self.createdAt
        self.updatedAt

    def task_id_generate(tasks):
        """
        Generate a unique task ID that persists across program runs.
        """
        ids = [
            task["id"] for task in tasks if isinstance(task.get("id"), int)
        ]
        return max(ids, default=0) + 1
    
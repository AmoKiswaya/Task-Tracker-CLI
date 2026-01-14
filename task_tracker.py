from datetime import datetime
import json


class Task:
    # task_id = 0


    def __init__(self, description="", tasks=None, status="todo", *args, **kwargs):
        self.id = self.task_id_generate(tasks) 
        self.description = description
        self.status = status
        self.createdAt = f"{datetime.now():%Y-%m-%dT%H:%M:%S}"
        self.updatedAt = f"{datetime.now():%Y-%m-%dT%H:%M:%S}"

    @staticmethod
    def task_id_generate(tasks):
        """
        Generates a unique task ID based on existing tasks.

        Args: 
            tasks (list): List of task dictionaries.
        """
        ids = [
            task["id"] for task in tasks if isinstance(task.get("id"), int)
        ]
        return max(ids, default=0) + 1
    

    def to_dict(self):
        """
        Converts the Task object to a dictionary for JSON storage.
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
    
    def update(self, description=None, status=None):
        """
        Updates task properties and the updatedAt timestamp.
        """

        if description is not None:
            self.description = description

        if status is not None:
            self.status = status

        self.updatedAt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S") 
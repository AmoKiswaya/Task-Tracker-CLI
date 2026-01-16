from task_tracker import Task
import json

class TaskManager:
    __file_path = "tasks.json"

    class Options:
        all = "all"
        done = "done"
        todo = "todo"
        in_progress = "in-progress"

    def __init__(self):
        self._tasks = {} 
        self.load_tasks()
        

    def load_tasks(self):
        """Load tasks from JSON file into self._tasks"""
        try:
            with open(TaskManager.__file_path, "r") as file:
                task_list = json.load(file)
                for task_id, task_data in task_list.items():
                    task_obj = Task.from_dict(task_data)
                    self._tasks[int(task_id)] = task_obj
        except FileNotFoundError:
            self._tasks = {}
        except json.JSONDecodeError:
            self._tasks = {} 

    def task_id_generate(self):
        """
        Generates a unique task ID based on existing tasks.
        """

        if not self._tasks:
            return 1
        return max(self._tasks.keys()) + 1
        
        # ids = [
        #     task["id"] for task in tasks if isinstance(task.get("id"), int)
        # ]
        # return max(ids, default=0) + 1


    def add_task(self, description: str):
        """
        Create a new Task with a unique ID and store it.
        """
        new_id = self.task_id_generate()
        task = Task(task_id=new_id, description=description)
        self._tasks[new_id] = task
        self.save_tasks()
        return task

    def delete_task(self, index):
        pass

    def list_tasks(self):
        pass 

    def save_tasks(self):
        """
        Save tasks to JSON file.
        """
        data = {}

        for task_id, task in self._tasks.items():
            data[task_id] = task.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(data, file)


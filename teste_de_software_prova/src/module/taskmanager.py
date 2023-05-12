from src.module.task import Task

class TaskManager:
    
    def __init__(self):
        self.task_list = []
        
    def add_task(self, task: Task):
        self.task_list.append(task)
        
    def list_tasks(self):
        return self.task_list
    
    def mark_task_done(self, id: int):
        for task in self.task_list:
            if task.get_id() == id:
                task.set_done(True)
    
    def remove_task(self, id: int):
        for task in self.task_list:
            if task.get_id() == id:
                self.task_list.remove(task)
    
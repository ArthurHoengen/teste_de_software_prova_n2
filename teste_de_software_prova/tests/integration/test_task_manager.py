import pytest

from src.module.taskmanager import TaskManager
from src.module.task import Task

class TestTaskManager:
    
    @pytest.fixture
    def task_1(self):
        return Task(1, "Terminar a prova", False)
    
    @pytest.fixture
    def task_2(self):
        return Task(2, "Terminar os testes", False)

    def test_task_manager_list(self, task_1):
        task_manager = TaskManager()
        task_manager.add_task(task_1)
        task_list = task_manager.list_tasks()
        assert task_list.count(task_1) == 1
        assert len(task_list) == 1
    
    def test_task_manager_add(self, task_1):
        task_manager = TaskManager()
        task_manager.add_task(task_1)
        task_list = task_manager.list_tasks()
        assert task_list.count(task_1) == 1
        assert len(task_list) == 1

    def test_task_manager_task_done(self, task_1):
        task_manager = TaskManager()
        task_manager.add_task(task_1)
        task_manager.mark_task_done(1)
        assert task_1.get_done() == True
        
    def test_task_manager_task_remove(self, task_1, task_2):
        task_manager = TaskManager()
        task_manager.add_task(task_1)
        task_manager.add_task(task_2)
        task_manager.remove_task(1)
        task_list = task_manager.list_tasks()
        assert task_list.count(task_1) == 0
        assert len(task_list) == 1
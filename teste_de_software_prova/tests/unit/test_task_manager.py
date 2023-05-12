import pytest

from src.module.taskmanager import TaskManager

class TestTaskManager:
    
    @pytest.fixture
    def task_1(self):
        return None

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
    
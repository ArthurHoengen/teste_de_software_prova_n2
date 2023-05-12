import pytest

from src.module.task import Task

class TestTask:
    @pytest.fixture
    def task(self):
        return Task(1, "Terminar a prova", False)

    def test_task_getters(self, task):
        assert task.get_id() == 1
        assert task.get_description() == "Terminar a prova"
        assert task.get_done() == False
        
    def test_task_setters(self, task):
        task.set_id(2)
        task.set_description("Acabar esse teste")
        task.set_done(True)
        
        assert task.get_id() == 2
        assert task.get_description() == "Acabar esse teste"
        assert task.get_done() == True
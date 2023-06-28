import pytest
import uuid
from datetime import datetime

from api.domain.list.todo_list import TodoList
from api.domain.task.task_entity import Task
 

class TestTodoList:
    
    def test_list_name_string(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("lista de compras","checkbox", uuid.uuid4().hex, [])
        todoList.addTasks(task)
        assert todoList.name == "lista de compras"
    
    def test_list_name_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("","checkbox", uuid.uuid4().hex, [])
        todoList.addTasks(task)
        with pytest.raises(ValueError, match=r"Name is required"):
            todoList.name
            
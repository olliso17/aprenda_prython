import uuid
from datetime import datetime
import pytest

from api.domain.list.list_entity import ListEntity
from api.domain.task.task_entity import Task


class TestListEntity:
    def list_name_string(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        listEntity = ListEntity("lista de compras","checkbox", uuid.uuid4().hex, [])
        listEntity.addTasks(task)
        assert listEntity.name == "lista de compras"
    
    def list_name_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        listEntity = ListEntity("lista de compras","checkbox", uuid.uuid4().hex, [])
        listEntity.addTasks(task)
        with pytest.raises(ValueError, match=r"Name is required"):
            listEntity.name
            
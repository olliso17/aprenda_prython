import uuid
from datetime import date

from api.domain.list.todo_list import TodoList
from api.domain.task.task_entity import Task

data = date.today()

task = Task("teste","testando a entidade", True, uuid.uuid4().hex, data)


listEntity1 = TodoList("lista de compras","checkbox",uuid.uuid4().hex, [])
listEntity = TodoList("lista de compras","checkbox",uuid.uuid4().hex, [])
listEntity.addTasks(task)


for lisTask in listEntity.tasks:
    print(lisTask.title)
    